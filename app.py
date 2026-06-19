import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("AI Chatbot")

st.write(f"Total messages: {len(st.session_state.messages)}")

user_message = st.text_area(
    "Ask Anything"
)
# print("New___")

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

if st.button("Send"):
    if(user_message.strip() == ""):
        st.warning("Please enter text")
    else:   
        st.session_state.messages.append(
        {
         "role": "user",
         "content": user_message   
        }
        )

        # print(f"messages : {st.session_state.messages}")
       
        response = client.responses.create(
            model="gpt-5.4",
            input=st.session_state.messages
        )
         # st.write(type(response))
        # st.write(response.output_text)
        st.session_state.messages.append(
        {
         "role": "assistant",
         "content": response.output_text   
        }
        )   
        st.rerun()
    
for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user"):   # inserts user emoji
                    st.write(message['content'])
            else:
                with st.chat_message("assistant"): # inserts assistant emoji
                    st.write(message['content'])

  # showUser_message = st.session_state.messages[-2]["content"]
        # showAssistant_message = st.session_state.messages[-1]["content"]
        # st.write(f"User: {showUser_message}")
        # st.write(f"Assistant: {showAssistant_message}")

        # for message in st.session_state.messages:
        #     if message["role"] == "user":
        #         st.write(f"User: {message['content']}")
        #     else:
        #         st.write(f"Assistant: {message['content']}")                