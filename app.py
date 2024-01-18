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
        # Generate topics using GPT
        chat_chain = LLMChain(prompt=PromptTemplate.from_template(topic_system_message), llm=chat_model)
        topics = chat_chain.run(TITLE=title)
        st.session_state['generated_headers'] = topics

# Editable text area for headers
st.write("Next, edit the generated skeleton as needed, or regenerate the skeleton entirely if you don't like this structure.")
st.write("(Note: please don't replace or modify the markdown (###, **, etc) or '{TYPE}s' notation)")
edited_headers = st.text_area("**Generated skeleton:**", value=st.session_state.get('generated_headers', ''), height=400)

# Generate blog posts for selected TypeFinder types
if st.button("**Generate blog posts for selected TypeFinder types**"):
    my_bar = st.progress(0)
    all_blogs_content = ""
    for i, typefinder in enumerate(typefinders):
        # Update progress bar
        my_bar.progress(i / len(typefinders))
        
        # Generate the blog post
        chat_chain = LLMChain(prompt=PromptTemplate.from_template(system_message), llm=chat_model)
        blog = chat_chain.run(TITLE=title, HEADERS=edited_headers, TYPE=typefinder, LOWER_TYPE=typefinder.lower())
        
        # Save the initial blog post in the session state
        st.session_state[f"blog_{typefinder}"] = blog

        # Create an expander for each blog with a feedback mechanism
        with st.expander(f"Blog for {typefinder}"):
            st.markdown(st.session_state[f"blog_{typefinder}"], unsafe_allow_html=True)

            # Feedback text area
            feedback = st.text_area(f"Feedback for {typefinder} blog:", key=f"feedback_{typefinder}", height=100)

            # Submit button for feedback
            if st.button(f"Submit Feedback for {typefinder}", key=f"feedback_btn_{typefinder}"):
                # Placeholder for LLM logic with feedback
                # Implement logic to process the feedback and update the blog
                updated_blog = "<LLM logic to process feedback and update blog>"

                # Update the session state with the updated blog content
                st.session_state[f"blog_{typefinder}"] = updated_blog

                # Display the updated blog
                st.markdown(updated_blog, unsafe_allow_html=True)

    # Compile all blogs in a single string for downloading
    for typefinder in typefinders:
        all_blogs_content += f"<h1>Blog for {typefinder}</h1>\n{st.session_state[f'blog_{typefinder}']}<hr>"

    # Download button for the compiled blogs in HTML format
    bytes_data = all_blogs_content.encode()
    st.download_button(label="Download Blogs as HTML", data=bytes_data, file_name=f"{title}.html", mime="text/html")

    # Reset progress bar
    my_bar.empty()
