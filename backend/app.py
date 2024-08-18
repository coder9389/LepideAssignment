from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import magic
import os
import PyPDF2

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def extract_text_from_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text
    except Exception as e:
        print("Error extracting text from PDF:", str(e))
        return ""

def summarize_text(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following text."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print("Error summarizing text:", str(e))
        return "Error summarizing text"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        file_content = file.read()
        print("File content length:", len(file_content))  # Log the length of received file

        # Determine file type
        mime = magic.Magic(mime=True)
        file_type = mime.from_buffer(file_content)
        print("Detected file type:", file_type)  # Log detected file type

        if file_type == 'application/pdf':
            text = extract_text_from_pdf(file)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        # Use the OpenAI API to summarize the content
        summary = summarize_text(text)
        print("Generated summary:", summary)  # Log the generated summary

        return jsonify({'summary': summary}), 200
    except Exception as e:
        print("Error:", str(e))  # Log any exceptions
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
