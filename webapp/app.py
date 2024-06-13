from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import logging
from openai import OpenAI


app = Flask(__name__) 
CORS(app)  # This will enable CORS for all routes

# Configure your OpenAI API key

client = OpenAI(api_key="API KEY HERE")
message_list = [{"role": "system", "content": "You are a medical learning assistant, skilled in explaining complex medical concepts to teach medical students."}]


# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['message']

    try:
        # response = openai.Completion.create(
        #     engine="text-davinci-003",  # Adjust the engine if necessary
        #     prompt=user_input,
        #     max_tokens=150
        # )
        # reply = response.choices[0].text.strip()

        message_list.append({"role": "user", "content": user_input})

        completion = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-0125:seniorprojectrd::9ZDqFLbU",
            messages=message_list
        )
        response = completion.choices[0].message.content
        message_list.append({"role": "assistant", "content": response})
        return jsonify({'response': response})
    
    except Exception as e:
        logging.error(f"Error: {e}", exc_info=True)
        return jsonify({'response': 'An error occurred on the server.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
