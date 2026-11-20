from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

normalize_prompt = PromptTemplate.from_template("""
Extract crop price info from this raw feed:
{raw_data}

Return JSON with:
crop_name, market_name, region, price_value, price_unit, timestamp, source_id
""")

normalize_chain = LLMChain(llm=llm, prompt=normalize_prompt)

def normalize_feed(raw_data: str):
    return normalize_chain.run(raw_data=raw_data)