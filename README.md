# Mistral-Hackathon-2024

# Student Advisor Chatbot

![Project Banner](https://via.placeholder.com/800x200.png?text=Student+Advisor+Chatbot)


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)

## Introduction
The **Student Advisor Chatbot** is a robust solution designed to assist students with administrative queries using Retrieval-Augmented Generation (RAG) technology. It serves as a virtual advisor, providing timely and accurate information, making the administrative process more efficient and student-friendly.

## Features
- **Uses Mistral large model/Groq**: Groq helps in faster inference speeds, whilst Mistral gives a slightly accurate answer, based on user's need.
- **Information Retrieval**: Utilizes RAG to fetch relevant information from a vast knowledge base.
- **User-Friendly Interface**: Easy to interact with, providing a seamless user experience.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Roshan-Velpula/Mistral-Hackathon-2024.git

2. Create and activate a virtual environment
    **In MacOS:**
    ```bash
    virtualenv .venv
    source .venv/bin/activate

3. **In Windows:**
    ```bash
    virtualenv .venv
    .venv\Scripts\activate

4. Install the required packages(Note:change directory to 'Project folder')
    ```bash
    pip install -r requirements.txt

5. Run the Streamlit application
    ```bash
    streamlit run EduRAG.py


