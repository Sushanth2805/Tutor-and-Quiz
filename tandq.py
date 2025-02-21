import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit Secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Function to get AI response
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response else "Error: No response received."

# Function to generate quiz
def generate_quiz(topic):
    prompt = f"Generate a multiple-choice quiz on {topic} with 4 options and indicate the correct answer."
    return ask_gemini(prompt)

# UI
st.title("📚 AI Educational Assistant")
st.sidebar.header("🔍 Features")
option = st.sidebar.radio("Select an option", ["AI Tutor", "Generate Quiz"])

if option == "AI Tutor":
    st.header("💡 Ask AI Your Questions")
    user_question = st.text_input("Enter your question:")
    if st.button("Get Answer") and user_question:
        answer = ask_gemini(user_question)
        st.write("### 🤖 AI Response:")
        st.write(answer)

elif option == "Generate Quiz":
    st.header("📝 AI-Generated Quiz")
    topic = st.text_input("Enter a topic:")
    if st.button("Generate") and topic:
        quiz = generate_quiz(topic)
        st.write("### 🎯 Quiz on", topic)
        st.write(quiz)

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit and Gemini AI")
