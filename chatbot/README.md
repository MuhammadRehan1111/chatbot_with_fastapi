# AI Chatbot Backend using FastAPI

## Project Overview

This project implements an AI-powered chatbot backend using **FastAPI** and integrates it with an external **LLM (Gemini API)**.
The backend receives a prompt from the user, sends it to the AI model, and returns the generated response.

A **Streamlit frontend** is also included to provide a simple user interface for interacting with the chatbot.

---

## System Workflow

User → Streamlit UI → FastAPI Backend → Gemini API → Response → User

---

## Project Structure

```
chatbot_project
│
├── app
│   ├── main.py
│   ├── schemas.py
│   ├── routes.py
│   ├── llm_service.py
│   └── config.py
│
├── frontend
│   └── streamlit_app.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Technologies Used

* FastAPI
* Streamlit
* Gemini API
* Python
* Pydantic
* Requests
* python-dotenv

---

## Installation

1. Clone the repository or download the project.

2. Navigate to the project directory:

```
cd chatbot_project
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

You can obtain the API key from:

https://aistudio.google.com/app/apikey

---

## Running the Backend

Start the FastAPI server using:

```
uvicorn app.main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

Swagger documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Run the Streamlit application:

```
streamlit run frontend/streamlit_app.py
```

The frontend will open in the browser at:

```
http://localhost:8501
```

---

## API Endpoint

### POST /chat

Send a prompt to the AI model.

Request example:

```
{
 "prompt": "Explain machine learning in simple terms"
}
```

Response example:

```
{
 "reply": "Machine learning is a method where computers learn patterns from data to make predictions."
}
```

---

## Input Validation

The API validates user input using **Pydantic**:

* Prompt must be required
* Prompt must not be empty
* Maximum length is **300 characters**

Invalid inputs return **422 validation errors**.

---

## Error Handling

The system handles several error scenarios:

| Scenario             | Status Code |
| -------------------- | ----------- |
| Invalid request body | 422         |
| Empty prompt         | 400         |
| AI API failure       | 500         |

---

## Features

* FastAPI based backend
* Integration with Gemini AI model
* Secure API key management using `.env`
* Input validation using Pydantic
* Proper HTTP error handling
* Streamlit chatbot user interface

---

## Author

Rehan
