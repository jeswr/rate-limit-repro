from dotenv import load_dotenv
load_dotenv()

from langchain_community.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0)

with get_openai_callback() as cb:
  model.batch([f"[{i}] How many occurences of hello world are in the following sentence:" + "hello world " * 2000 for i in range(100)])
  print(f"Total Cost (USD): ${cb.total_cost}")
