import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Simple Rule-Based Chatbot")
st.markdown("Ask me anything! I'm a basic chatbot built with if-else rules.")

# Take user input
user_input = st.text_input("You: ")


# Response logic
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"
    elif "your name" in user_input:
        return "I'm a simple chatbot made with Streamlit."
    elif "how are you" in user_input:
        return "I'm good, thank you! How can I help?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "You can ask me simple questions like 'hello', 'how are you', etc."
    else:
        return "I'm not sure how to respond to that."


# Display response
if user_input:
    st.text_area("Bot:", chatbot_response(user_input), height=100)
