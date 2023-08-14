# IMPORT
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def load_prompt():
    with open("prompt.txt", "r") as text_file:
        prompt = text_file.read()
    return prompt


def ask_OpenAI(question, openai_api_key):
    chat = ChatOpenAI(temperature=0.0, openai_api_key=openai_api_key)
    prompt = load_prompt()
    prompt_template = ChatPromptTemplate.from_template(template=prompt)
    messages = prompt_template.format_messages(
        question=question
    )
    response = chat(messages)
    return response.content
