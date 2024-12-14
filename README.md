## Requirements
- Python 3.7 or higher
- OpenAI Python Library (`openai`)
- Flask

## Installation
1. Clone this repository
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Install/Upgrade pip
   ```bash
   py -m pip install --upgrade pip

3. Create a virtual environment if necessary
   ```bash
   python -m venv venv

4. Install requirements
   ```bash
   pip install flask openai

5. Set up your OpenAI API key: Replace "your-api-key" in configurations.py with your actual OpenAI API key
   ```bash
   #define your OpenAIApiKey within ""
   OPENAI_API_KEY="your-api-key"

## Usage
1. Run the Flask application
   ```bash
   python AppStart.py

2. Open your browser and navigate to
   ```bash
   http://127.0.0.1:5000/
   
3. Enter a query in the provided text box, submit it, and view the model's response