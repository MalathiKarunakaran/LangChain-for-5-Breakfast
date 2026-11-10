from pathlib import Path
import sys

from dotenv import dotenv_values
from langchain_openai import ChatOpenAI

# Read the key straight from .env next to this file — ignores shell exports.
env = dotenv_values(Path(__file__).with_name(".env"))
api_key = (env.get("OPENAI_API_KEY") or "").strip()

if not api_key.startswith("sk-"):
    sys.exit("No valid OPENAI_API_KEY in .env. Put it on one line: OPENAI_API_KEY=sk-...")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

prompt = (
    "Give exactly 5 healthy breakfast ideas.\n"
    "Healthy means: high in protein or fibre, whole grains or millets, "
    "little added sugar, not deep-fried.\n"
    "Format: a numbered list 1 to 5, one idea per line, under 12 words each.\n"
    "No title, no introduction, no closing sentence. Output only the 5 lines."
)

reply = llm.invoke(prompt)
print(reply.content)
