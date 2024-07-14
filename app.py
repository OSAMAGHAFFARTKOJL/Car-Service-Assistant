import streamlit as st
#from langflow.load import run_flow_from_json
import os
import openai  # Correct import for the openai package

# Set the environment variable (done within Google Colab, or set externally)
os.environ['OPENAI_API_KEY'] = 'sk-proj-m2AYoibJtfEsCNoLEYnLT3BlbkFJPkvscZvqtfgqJC68RxYZ'

try:
    results = run_flow_from_json("/content/CSA Robot.json", input_value="Hello, World!")
    st.write("Flow Results:", results)
except:
    # Retrieve the API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

    # Instantiate the client with the API key
    openai.api_key = api_key

    def generate_response(user_input):
        # Create a chat completion
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for GPT-4
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        # Access the response content
        return response.choices[0].message['content']

    # Streamlit UI
    st.title("Car Servicing Assistant")

    user_input = st.text_input("Enter your question:")
    if st.button("Submit"):
        response = generate_response(user_input)
        st.write( response)
