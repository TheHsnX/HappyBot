from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
import os


llm = ChatOllama(
    model="deepseek-r1:1.5b",
    temperature=0.8,
)




messages = [
    ("system", "You are a coding assistant. Provide Python code first, then a short explanation."),
    ("human", "Write a Python script to print 'Hello World'."),
    ("assistant", "```python\nprint('Hello World')\n```\nThis script prints 'Hello World' to the console."),
    ("human", "Write a Python program for a Stone Paper Scissors game."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)
