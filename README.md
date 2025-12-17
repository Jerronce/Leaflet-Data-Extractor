Leaflet Product Extractor 

A full-stack Python application that extracts structured product data from retail leaflets using **AI Vision (OpenAI GPT-4o)** and displays it in an interactive web interface.

 Features
* **AI-Powered Extraction:** Uses GPT-4o to identify product names and prices from images.
* **Interactive UI:** A Flask-based web dashboard with clickable product rows.
* **Data Persistence:** Saves extracted results to `data.json` for fast subsequent loads.

 Tech Stack
* **Backend:** Python, Flask
* **AI:** OpenAI API (Vision Model)
* **Frontend:** HTML5, CSS3, JavaScript
* **Data Handling:** JSON, Pandas

 Installation & Setup
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Add your OpenAI API Key to a `.env` file: `OPENAI_API_KEY=your_key_here`.
5. Run the app: `python app.py`.
