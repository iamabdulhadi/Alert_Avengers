
import os
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_sql_agent(db_path: str):
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)
    return agent_executor

if __name__ == '__main__':
    # This part is for testing the agent directly
    agent = get_sql_agent("banking.db")
    query = "How many customers are there?"
    print(f"\nQuery: {query}")
    response = agent.invoke({"input": query})
    print(f"Response: {response['output']}")

    query = "Show me the balance for John Doe's savings account."
    print(f"\nQuery: {query}")
    response = agent.invoke({"input": query})
    print(f"Response: {response['output']}")


