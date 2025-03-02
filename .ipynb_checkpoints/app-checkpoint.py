import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key

def get_recipe_recommendations(ingredients, dietary_restrictions=None, meal_type=None):
    """
    Get recipe recommendations based on available ingredients and preferences.
    
    Args:
        ingredients (list): List of available ingredients
        dietary_restrictions (str, optional): Any dietary restrictions
        meal_type (str, optional): Type of meal (breakfast, lunch, dinner, etc.)
        
    Returns:
        str: Recipe recommendations
    """
    # Construct the prompt
    prompt = f"I have the following ingredients: {', '.join(ingredients)}. "

    if dietary_restrictions:
        prompt += f"I have these dietary restrictions: {dietary_restrictions}. "

    if meal_type:
        prompt += f"I'm looking for a {meal_type} recipe. "

    prompt += "Please suggest 3 recipes I can make with these ingredients, including brief instructions for each."

    # Call the OpenAI API
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful cooking assistant that suggests recipes based on available ingredients."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=1000,
    temperature=0.7)

    return response.choices[0].message.content

def main():
    print("🍳 Welcome to the AI Recipe Recommender! 🍳")
    print("Tell me what ingredients you have, and I'll suggest some recipes.")

    # Get user input
    ingredients_input = input("\nEnter your available ingredients (comma-separated): ")
    ingredients = [i.strip() for i in ingredients_input.split(",")]

    dietary_restrictions = input("\nAny dietary restrictions? (e.g., vegetarian, gluten-free, etc. - press Enter if none): ")
    if dietary_restrictions.strip() == "":
        dietary_restrictions = None

    meal_type = input("\nWhat type of meal are you looking for? (breakfast, lunch, dinner, snack, etc. - press Enter if any): ")
    if meal_type.strip() == "":
        meal_type = None

    print("\nGenerating recipe recommendations...")

    # Get recommendations
    recommendations = get_recipe_recommendations(ingredients, dietary_restrictions, meal_type)

    # Display recommendations
    print("\n🍽️ RECIPE RECOMMENDATIONS 🍽️\n")
    print(recommendations)
    print("\nEnjoy your cooking! 👨‍🍳👩‍🍳")

if __name__ == "__main__":
    main() 