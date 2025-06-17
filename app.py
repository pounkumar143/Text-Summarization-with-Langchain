import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarizer", page_icon=":books:, layout = centered")
st.time_input('Text summarizer using langchain and Groq')
st.markdown("Paste your content and get a concise summary")

text_input=st.text_area("Enter your text here to summarize", height=300)
if st.button("Summarize"):
    if text_input.strip():
            with st.spinner("Summarizing your text..."):
                summary = summarize_text(text_input)
                st.subheader("Summary:")
                st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")