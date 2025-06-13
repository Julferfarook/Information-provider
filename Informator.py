import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI

# 🔐 Hardcoded Gemini API Key (Not recommended for production)
GOOGLE_API_KEY = "AIzaSyCsINRQVql0DWC3uZiWmA47ZLwS-EGkdPE"  # Replace with your actual API key

# 🌐 Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # Fast model variant
    temperature=0.3,
    google_api_key=GOOGLE_API_KEY
)

# 🔎 Add DuckDuckGo Search Tool
search_tool = DuckDuckGoSearchRun()

# 🤖 Initialize Agent with Tool
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False  # Disable verbose logging
)

# 🎨 Streamlit UI
st.set_page_config(page_title="🌍 Real-Time Q&A (Gemini + Web)", page_icon="🔎")
st.title("🌍 Real-Time Q&A App")
st.markdown("Ask about recent news, current events, or factual information. Powered by **Google Gemini + DuckDuckGo**.")

# 🧠 Input + Button
user_question = st.text_input("❓ What do you want to know?")
if st.button("🔍 Get Answer"):
    if not user_question.strip():
        st.warning("⚠️ Please enter a question to proceed.")
    else:
        try:
            with st.spinner("Thinking..."):
                answer = agent.run(user_question)
            st.success("✅ Answer Generated!")
            st.markdown("### 🧠 Gemini's Response:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ Error: {e}")

# 📝 Footer
st.markdown("---")
st.caption("⚡ Built with Streamlit · Google Gemini · DuckDuckGo · LangChain")
