import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def analyze_cart(cart):

    prompt = f"""
    Analyze this shopping cart and suggest insights.

    {cart}
    """

    response = model.generate_content(prompt)

    return response.text