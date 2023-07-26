import streamlit as st
from langchain.llms import LlamaCpp
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


st.set_page_config(page_title="Hashtag Generator", page_icon="#️⃣", layout="wide", )
st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1612538498456-e861df91d4d0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80");
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)

# set prompt template
prompt_template = """You are a human who is trying to sell an item on an e-commerce platform and you need to come up with five hashtags that best describe the item.
Come up with five hashtags based on the item's title that will help you reach a larger amount of buyers and get more engagement.
Note that hashtags should not include item conditions like repair needed and brand new.
Organize the five hashtags using bullet points.
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(prompt_template)

human_template = """List five hashtags for this item: {title}"""
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
llm = LlamaCpp(
    model_path="./models/llama-2-13b-chat.ggmlv3.q4_0.bin",
    temperature=0.72,
    repeat_penalty=1.1,
    max_tokens=2048,
    top_p=0.73,
    top_k=0,
    seed=2023,
    callback_manager=callback_manager,
    verbose=True,
)
llm_chain = LLMChain(llm=llm, prompt=chat_prompt)

st.title("Enter item's title to get #️⃣ recommendations")
input_title = st.text_input("enter the title here", placeholder="Nike Court Royal",)
if input_title:
    response = llm_chain.run(title=input_title)
    st.write(response)
