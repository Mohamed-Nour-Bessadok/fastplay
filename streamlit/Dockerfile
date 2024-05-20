FROM python:3.12.3

WORKDIR /streamlit

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

ENV PYTHONPATH=/streamlit

EXPOSE 8501

CMD ["streamlit", "run", "chatbot.py"]
