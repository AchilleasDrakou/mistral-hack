# Mistral-Hackathon-2024
This was part of a 24-hour hackathan based in Paris.
The app is avaialable on [Streamlit](https://campusbolt.streamlit.app/).

# CampusBOLT

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Contributors](#contributors)

## Introduction
The **CampusBOLT** is a robust solution designed to assist students with administrative queries using RAG and LLMs. It serves as a virtual advisor, providing timely and accurate information, making the administrative process more efficient and student-friendly.

## Features
- **Uses Mistral large model/Groq**: User can select between Groq for faster inference speeds, or Mistral for more thorough answers.
- **Information Retrieval**: Utilizes RAG to fetch relevant information from a vast knowledge base.
- **User-Friendly Interface**: Easy to interact with, providing a seamless user experience.
- **Multi-Lingual Support**: Responds to the user query in their language
- **Ticket Generation**: Summarizes the conversation and generates a support ticket to the admin team automatically if the user needs more help

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
    streamlit run CampusBOLT.py


## Contributors
1. Achilleas Drakou - [LinkedIn](https://www.linkedin.com/in/drakou/)
2. Irene Sunny - [LinkedIn](https://www.linkedin.com/in/irenesunny/), [Github](https://github.com/IreneSunny96)
3. Poongkundran Thamaraiselvan - [LinkedIn](https://www.linkedin.com/in/poongkundran-thamaraiselvan/), [GitHub](https://github.com/Poonge1598)
4. Roshan Velpula - [LinkedIn](https://www.linkedin.com/in/roshan-velpula/), [GitHub](https://github.com/Roshan-Velpula)

