import os
import json
import base64
from flask import Flask, render_template, jsonify
from openai import OpenAI
from dotenv import load_dotenv

# 1. Load the variables from the .env file
load_dotenv()

app = Flask(__name__)

# 2. Get the key and verify it exists
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ ERROR: OPENAI_API_KEY not found. Check your .env file!")

# 3. Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Configuration: Path to your image inside the assets folder
IMAGE_PATH = "assets/leaflet.png"
OUTPUT_JSON = "data.json"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extract_with_openai(image_path):
    base64_image = encode_image(image_path)
    print("AI is analyzing the leaflet... please wait.")
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract all products and prices from this leaflet. Return ONLY a JSON list of objects with 'id', 'name', and 'price'."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                ],
            }
        ],
        response_format={ "type": "json_object" }
    )
    
    content = response.choices[0].message.content
    data = json.loads(content)
    # Return the list of products
    return data.get("products", data) if isinstance(data, dict) else data

@app.route('/')
def index():
    if not os.path.exists(OUTPUT_JSON):
        data = extract_with_openai(IMAGE_PATH)
        with open(OUTPUT_JSON, 'w') as f:
            json.dump(data, f, indent=4)
    else:
        with open(OUTPUT_JSON, 'r') as f:
            data = json.load(f)
            
    return render_template('index.html', data=data)

if __name__ == '__main__':
    print("Starting server at http://127.0.0.1:5000/")
    app.run(debug=True)