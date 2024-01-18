import streamlit as st
import requests
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
import io
from system_messages import *

# Initialize the chat model
chat_model = ChatOpenAI(openai_api_key=st.secrets['API_KEY'], model_name='gpt-4-1106-preview', temperature=0.2, max_tokens=4096)

# Initialize session state for blogs
for typefinder in ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]:
    if f"blog_{typefinder}" not in st.session_state:
        st.session_state[f"blog_{typefinder}"] = ""

if 'generated_headers' not in st.session_state:
    st.session_state['generated_headers'] = ""

# Streamlit UI setup
st.title("MBTI Blog Post Generator")

st.write("**This tool will generate blogs for selected MBTI types given a fixed topic.** When you write your title, **use the placeholder 'Xs'** for where the types (eg, INTPs, ENFJs) will go.")
st.write("*Examples: The Best Paying Careers for Xs, Best Jobs for Xs That Don't Require a College Degree, etc.*")

# Multiselect widget for MBTI type selection
typefinders = st.multiselect("Choose MBTI Types:", ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"])

# Input for blog title
title = st.text_input("Blog Title:")

# Generate blog skeleton
if st.button("Generate Skeleton for This Blog"):
    with st.spinner("Generating blog skeleton, please standby..."):
        chat_chain = LLMChain(prompt=PromptTemplate.from_template(topic_system_message), llm=chat_model)
        topics = chat_chain.run(TITLE=title)
        st.session_state['generated_headers'] = topics

# Editable text area for headers
st.write("Next, edit the generated skeleton as needed, or regenerate the skeleton entirely if you don't like this structure.")
edited_headers = st.text_area("Generated skeleton:", value=st.session_state['generated_headers'], height=400)

# Function to generate a single blog post
def generate_blog_post(typefinder):
    chat_chain = LLMChain(prompt=PromptTemplate.from_template(system_message), llm=chat_model)
    return chat_chain.run(TITLE=title, HEADERS=edited_headers, TYPE=typefinder, LOWER_TYPE=typefinder.lower())

# Generate blog posts for selected TypeFinder types
if typefinders:
    if st.button("**Generate blog posts for selected TypeFinder types**"):
        with st.spinner("Writing blog...this will take a minute or two"):
            for i, typefinder in enumerate(typefinders):
                st.session_state[f"blog_{typefinder}"] = generate_blog_post(typefinder)

# Display blogs and feedback mechanism
for typefinder in typefinders:
    if st.session_state[f"blog_{typefinder}"]:
        with st.expander(f"Blog for {typefinder}"):
            st.markdown(st.session_state[f"blog_{typefinder}"], unsafe_allow_html=True)
            
            # Individual blog download button
            blog_html = st.session_state[f"blog_{typefinder}"].encode()
            st.download_button(label="Download this Blog as HTML", data=blog_html, file_name=f"{typefinder}_blog.html", mime="text/html")
            
            # Feedback section
            feedback = st.text_area(f"Write any feedback or points of improvement for this draft of the {typefinder} blog (note that this will take another minute or two to process):", key=f"feedback_{typefinder}", height=100)
            if st.button(f"Submit Feedback", key=f"feedback_btn_{typefinder}"):
                with st.spinner("Integrating your feedback into the blog...this will take a minute or two"):
                    chat_chain = LLMChain(prompt=PromptTemplate.from_template(feedback_system_message), llm=chat_model)
                    updated_blog = chat_chain.run(original=st.session_state[f"blog_{typefinder}"], feedback=feedback)
                    st.session_state[f"blog_{typefinder}"] = updated_blog
                    st.experimental_rerun()
                st.success("Feedback processed and blog updated.")
