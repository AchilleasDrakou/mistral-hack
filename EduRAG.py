import os
import streamlit as st
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from Project.retriever import format_results, reform, rerag
from langchain.memory import ConversationBufferWindowMemory
from Project.vector_pipeline import connect_db
from Project.prompts import custom_answer_prompt_template
from langchain.prompts import PromptTemplate

# Streamlit UI
st.title("💬 EduRAG")
st.caption("🚀 Get ESSEC info without the headache")


# Set the API keys
mistral_api_key = os.getenv("MISTRAL_API")
groq_api_key = os.getenv("GROQ_API")

# Define the system prompt template
system_prompt_template = "You are a helpful chatbot for a university student. Provide relevant information to help students, but do not include the student's question in your response."

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

if "mistral_client" not in st.session_state:
    st.session_state.mistral_client = MistralClient(api_key=mistral_api_key)

if "groq_chat" not in st.session_state:
    st.session_state.groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="mixtral-8x7b-32768"
    )

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(k=10, memory_key="chat_history", return_messages=True)

# Sidebar option to select the model
model_options = ["Groq 7B", "Mistral Large"]
selected_model = st.sidebar.selectbox("Select Model", model_options)

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "human", "content": prompt})
    st.chat_message("user").write(prompt)

    connection, cursor = connect_db()

    # Create a conversation chain using the LangChain LLM (Language Learning Model)
    reformed_query = reform(prompt, st.session_state.groq_chat)
    reraged = rerag(reformed_query, 'edu', cursor=cursor)
    context = format_results(reraged)
    answer_prompt = PromptTemplate(template=custom_answer_prompt_template, input_variables=['context', 'query'])
    formatted_prompt = answer_prompt.format(query=prompt, context=context)

    if selected_model == "Groq 7B":
        llm_groq=st.session_state.groq_chat
        response = llm_groq.invoke(formatted_prompt).content

        st.session_state.messages.append({"role": "AI", "content": response})
        st.chat_message("assistant").write(response)
    else:
        model = "mistral-large-latest"
        messages = [
            ChatMessage(role="system", content=system_prompt_template),
            ChatMessage(role="user", content=formatted_prompt)
        ]
        stream_response = st.session_state.mistral_client.chat_stream(model=model, messages=messages)

        response_container = st.empty()
        full_response = ""
        for chunk in stream_response:
            if chunk.choices[0].delta.content:
                chunk_content = chunk.choices[0].delta.content
                full_response += chunk_content
                response_container.markdown(full_response)

        st.session_state.messages.append({"role": "AI", "content": full_response})


