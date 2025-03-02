from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
import markdown
import re

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with DeepSeek API configuration
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get("OPENROUTER_API_KEY"),
)

app = Flask(__name__)

def get_recipe_recommendations(ingredients, dietary_restrictions, meal_type):
    """
    Get recipe recommendations based on available ingredients and preferences.
    
    Args:
        ingredients (list): List of available ingredients
        dietary_restrictions (list): List of dietary restrictions
        meal_type (str): Type of meal (breakfast, lunch, dinner, etc.)
        
    Returns:
        str: Recipe recommendations
    """
    # Format the ingredients, dietary restrictions, and meal type into a prompt
    ingredients_str = ", ".join(ingredients)
    dietary_str = ", ".join(dietary_restrictions) if dietary_restrictions else "None"
    
    system_message = "You are a helpful cooking assistant that provides recipe recommendations based on available ingredients. Format your response using proper Markdown with ## for recipe titles and * for bullet points. Do not use ### for headings."
    user_message = f"I have the following ingredients: {ingredients_str}. My dietary restrictions are: {dietary_str}. I want to make a {meal_type if meal_type else 'meal'}. Please suggest 3 recipes I can make with these ingredients, including instructions and cooking time."
    
    try:
        # Call DeepSeek API using OpenAI-compatible interface
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",  # Using DeepSeek-R1 model
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        # Extract the response content
        content = response.choices[0].message.content
        
        # Convert markdown to HTML
        html_content = markdown.markdown(content)
        
        return html_content
    except Exception as e:
        print(f"Error generating recipe recommendations: {e}")
        return "Sorry, I couldn't generate recipe recommendations. Please try again later."

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    
    if request.method == 'POST':
        # Get form data
        ingredients_input = request.form.get('ingredients', '')
        ingredients = [i.strip() for i in ingredients_input.split(",")]
        
        dietary_input = request.form.get('dietary', '')
        dietary_restrictions = [d.strip() for d in dietary_input.split(",")] if dietary_input.strip() else None
        
        meal_type = request.form.get('meal_type', '')
        if not meal_type.strip():
            meal_type = None
            
        # Get recommendations
        recommendations = get_recipe_recommendations(ingredients, dietary_restrictions, meal_type)
    
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True) 