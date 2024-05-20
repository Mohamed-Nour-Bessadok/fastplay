from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain.agents import tool
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from endpoints import parse_departmental_awards, parse_employee_awards
from dotenv import load_dotenv
import logging

load_dotenv()

@tool
def get_departmental_awards(type: str, award: str):
    """Use this tool to look up the department or employee that received a specific award.
    award is :"1st Place", "2nd Place", or "3rd Place".
    type is either "department" or "employee".
    """
    if type == "department":
        return parse_departmental_awards(award)
    elif type == "employee":
        return parse_employee_awards(award)
    else:
        return None

def chatbot(input, chat_history):
    tools = [get_departmental_awards]
    prompt = hub.pull("hwchase17/openai-tools-agent")
    llm = ChatOpenAI()
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    """chain = prompt | agent_executor | StrOutputParser()
    return chain.stream({
        "input": input,
        "chat_history": chat_history
    })"""
    return agent_executor.invoke({"input": input, "chat_history": chat_history}) 




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chatbot")
async def chatbot_endpoint(request: Request):
    data = await request.json()
    input = data.get("input")
    chat_history = data.get("chat_history", [])
    if input is None:
        raise HTTPException(status_code=400, detail="Input parameter is required")
    try:
        response = chatbot(input, chat_history)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request")
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)