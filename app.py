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


st.set_page_config(page_title="Hashtag Generator", page_icon="#️⃣#️⃣#️⃣#️⃣", layout="wide", )
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
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(prompt_template)

human_template = """List five hashtags for this item: {title}"""
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
llm = LlamaCpp(
    # model_path="./models/llama-2-13b.ggmlv3.q4_0.bin",
    model_path="./models/llama-2-13b-chat.ggmlv3.q4_0.bin",
    temperature=0.7,
    repeat_penalty=1.176,
    max_tokens=2048,
    top_p=0.1,
    top_k=40,
    seed=2023,
    callback_manager=callback_manager,
    verbose=True,
)
llm_chain = LLMChain(llm=llm, prompt=chat_prompt)

st.title("#️⃣#️⃣#️⃣#️⃣")
input_title = st.text_input("enter listing's title", placeholder="Nike Court Royal",)
if input_title:
    response = llm_chain.run(title=input_title)
    st.write(response)
