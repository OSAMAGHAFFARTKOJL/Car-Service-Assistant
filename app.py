import streamlit as st
#from langflow.load import run_flow_from_json
import os
from openai import OpenAI

# Set the environment variable
os.environ['OPENAI_API_KEY'] = 'sk-proj-m2AYoibJtfEsCNoLEYnLT3BlbkFJPkvscZvqtfgqJC68RxYZ'

# Function to generate response
def generate_response(user_input):
    # Retrieve the API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

    # Instantiate the client with the API key
    client = OpenAI(api_key=api_key)

    # Create a chat completion
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" for GPT-4
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    # Access the response content
    return chat_completion.choices[0].message.content

# Streamlit app
def main():
    st.title("Car Servicing Assistant")
    user_input = st.text_input("Enter your question:")
    if st.button("Submit"):
        try:
            results = run_flow_from_json("CSA_Robot.json", input_value=user_input)
            st.write("Flow Results:", results)
        except Exception as e:
            response = generate_response(user_input)
            st.write(response)

if __name__ == "__main__":
    main()
