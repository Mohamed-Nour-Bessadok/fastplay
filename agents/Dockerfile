FROM python:3.12.3

WORKDIR /agents

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

ENV PYTHONPATH=/agents

EXPOSE 8000

CMD ["uvicorn", "agents:app", "--host", "0.0.0.0", "--port", "8000"]

