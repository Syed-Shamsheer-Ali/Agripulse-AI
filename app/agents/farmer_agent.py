from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, Tool
from langchain.prompts import PromptTemplate

# Initialize the language model
llm = ChatOpenAI(model="gpt-4o-mini")

# Define the prompt for the farmer agent
farmer_prompt = PromptTemplate.from_template("""
You are a helpful assistant for farmers. Answer their questions about crop prices, market trends, and provide advice based on the information provided.
Question: {question}
""")

# Define tools that the agent can use
tools = [
    Tool(
        name="Get Price Information",
        func=lambda crop_id, market_id: f"Fetching price for crop {crop_id} in market {market_id}.",
        description="Useful for getting the latest price information."
    ),
    Tool(
        name="Provide Market Advice",
        func=lambda crop_name: f"Providing advice for {crop_name}.",
        description="Useful for giving advice on crop management."
    )
]

# Create the agent executor
farmer_agent = AgentExecutor(
    llm=llm,
    tools=tools,
    prompt=farmer_prompt,
    verbose=True
)

def interact_with_farmer(question: str):
    return farmer_agent.run(question=question)