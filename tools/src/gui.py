# IMPORTS
import streamlit as st
import ai

__version__ = "0.1.1.2"
app_name = "Ask Euler, your math tutor"

# BOILERPLATE
st.set_page_config(layout='centered', page_title=f'{app_name} {__version__}')
ss = st.session_state

# HANDLER


# COMPONENT
def enter_api_key():
    openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key:', type='password')
    print(openai_api_key)
    ss.api_key = openai_api_key

def show_title():
    st.title("Ask Euler - your math tutor")


def ask_ai():
    with st.form('AskEuler-form'):

        question = st.text_input('**Question**? :sunglasses::', '')
        answer = st.form_submit_button('Answer')
        if answer:
            openai_api_key = ss.get('api_key')
            print('keys')
            print(openai_api_key)
            if not openai_api_key.startswith('sk-'):
                st.warning('Please enter your OpenAI API key!', icon='⚠')
            st.info(ai.ask_OpenAI(question, openai_api_key).split("Clues")[0])
            st.info(ai.ask_OpenAI(question, openai_api_key).split("Clues")[1][2:])


enter_api_key()
show_title()
ask_ai()


