from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import HumanMessagePromptTemplate
from langchain_groq import ChatGroq


prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content='You are a helpful assistant.'),
    HumanMessagePromptTemplate.from_template('{input}'),
])

chat = ChatGroq(
    model='llama3-8b-8192',
    temperature=0,
    max_tokens=8192,
    # api_key='',  # Optional if not set as an environment variable
)

chat_groq_chain = prompt | chat | StrOutputParser()
