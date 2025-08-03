from ibm_watson_machine_learning.foundation_models import Model
from dotenv import load_dotenv
import os
import json
import re

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
URL = os.getenv("URL")

print("DEBUG: API_KEY =", API_KEY[:6] + "..." if API_KEY else None)
print("DEBUG: PROJECT_ID =", PROJECT_ID)
print("DEBUG: URL =", URL)

if not API_KEY or not PROJECT_ID or not URL:
    raise Exception("❌ API_KEY, PROJECT_ID, or URL not found. Check .env file.")

model = Model(
    model_id="ibm/granite-3-3-8b-instruct",
    credentials={"apikey": API_KEY, "url": URL},
    project_id=PROJECT_ID,
)

def generate_profile(text):
    prompt = f"""Extract a structured JSON faculty profile from the following resume text:
{text}
The JSON must have these keys: name, email, phone, education, experience, research_interests, publications, skills.
Ensure the JSON is valid and complete.
    """
    params = {"decoding_method": "greedy", "max_new_tokens": 800}
    response = model.generate(prompt=prompt, params=params)

    raw_output = response.get("results", [{}])[0].get("generated_text", "")
    print("\n🔍 Raw model output:\n", raw_output)

    # Try to extract the first valid JSON object using regex
    match = re.search(r"\{[\s\S]+\}", raw_output)
    if not match:
        raise ValueError("❌ No JSON object found in model response.")

    json_text = match.group(0)

    try:
        profile_data = json.loads(json_text)
        return profile_data
    except json.JSONDecodeError as e:
        raise ValueError(f"❌ Error parsing JSON: {e}\nExtracted Text:\n{json_text}")





