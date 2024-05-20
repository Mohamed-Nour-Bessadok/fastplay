# fastplay

Chatbot application using FastAPI and streamlit.

Using agents (with langchain) the chatbot is able to retrieve informations from a .txt file.

#How to use:

Step 1:

Set openai_api_key in .env file:
```OPENAI_API_KEY = your open ai key```

Step 2:

To run in a machine running Docker:
```docker-compose up --build```

Step 3:

To visit the FastAPI documentation of the resulting service, visit http://localhost:8000/docs with a web browser.
To visit the streamlit UI, visit http://localhost:8501.
