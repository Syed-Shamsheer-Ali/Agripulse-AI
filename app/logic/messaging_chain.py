from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

msg_prompt = PromptTemplate.from_template("""
Generate a short farmer-friendly message in {language}.
Market: {market}, Crop: {crop}, Price: {price} per {unit}, Updated: {time}
Limit 150 characters.
""")

msg_chain = LLMChain(llm=llm, prompt=msg_prompt)

def generate_message(market, crop, price, unit, time, language="English"):
    return msg_chain.run(market=market, crop=crop, price=price, unit=unit, time=time, language=language)