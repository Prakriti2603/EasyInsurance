import google.generativeai as genai

# ✅ Paste your Gemini API key here
genai.configure(api_key="AIzaSyBrRuOi8iVsM5gZXqplu504S6HKplpsMw0")  # Replace with your actual key

# ✅ Use a code-friendly model that works without billing
model = genai.GenerativeModel("models/code-bison-001")

def get_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"⚠️ Gemini Error: {str(e)}"
