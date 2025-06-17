from langchain_groq import ChatGroq

def get_groq_llm():
    return ChatGroq(
        model="llama3-8b-8192",
        groq_api_key ="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",
        temperature=0.7
        )

