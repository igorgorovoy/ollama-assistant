import streamlit as st
import requests

OLLAMA_API_URL = "http://localhost:11434/api/"
import json



def send_message(message):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3",
        "prompt": message
    }
    response = requests.post("http://localhost:11434/api/generate", json=data, headers=headers)

    try:
        responses = []
        for line in response.text.split("\n"):
            if line.strip():
                json_response = json.loads(line)
                if "response" in json_response:
                    responses.append(json_response["response"])
        return " ".join(responses)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"


def main():
    st.title("Local Ollama 3 Chat App")

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            response = send_message(user_input)
            st.text_area("Ollama 3:", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()