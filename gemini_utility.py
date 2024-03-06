import os
import json
import google.generativeai as genai

working_dir = os.path.dirname(os.path.abspath(__file__))

# path of config_data file
config_file_path = f"{working_dir}/config.json"
config_data = json.load(open("config.json"))

# loading the GOOGLE_API_KEY
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

#configuring the google api key
genai.configure(api_key=GOOGLE_API_KEY)

def load_gemini_pro_model():
    # Load the model
    gemini_pro_model=genai.GenerativeModel("gemini_pro")
    return gemini_pro_model