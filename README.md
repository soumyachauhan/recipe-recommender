# AI Recipe Recommender

An intelligent web application that recommends recipes based on the ingredients you have available, dietary restrictions, and meal preferences. Powered by DeepSeek AI.

<!-- ![Recipe Recommender Screenshot](https://i.imgur.com/example-screenshot.jpg) -->

## Features

- **Ingredient-Based Recommendations**: Get recipe ideas based on ingredients you already have
- **Dietary Restriction Support**: Filter recipes according to your dietary needs (vegetarian, gluten-free, etc.)
- **Meal Type Selection**: Specify what kind of meal you're looking to prepare
- **Detailed Instructions**: Receive complete recipes with ingredients, steps, and cooking times
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **AI Integration**: DeepSeek API via OpenRouter
- **Deployment**: Vercel

## Getting Started

### Prerequisites

- Python 3.7 or higher
- An OpenRouter API key with access to DeepSeek models

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/recipe-recommender.git
   cd recipe-recommender
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```bash
   python web_app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

1. Enter the ingredients you have available, separated by commas
2. Optionally specify any dietary restrictions
3. Optionally select a meal type
4. Click "Get Recipe Recommendations"
5. View the generated recipes with instructions

## Deployment

This application is configured for deployment on Vercel:

1. Push your code to GitHub
2. Import the repository in Vercel
3. Set the environment variables in Vercel's dashboard
4. Deploy

## How It Works

The application uses natural language processing to:
1. Understand your available ingredients and preferences
2. Generate appropriate recipe suggestions
3. Format the output in a user-friendly way

The AI model considers ingredient combinations, cooking techniques, and dietary requirements to provide personalized recommendations.

## Customization

You can adjust the AI parameters in `web_app.py`:

- `temperature`: Controls creativity (0.0-1.0)
- `max_tokens`: Controls response length

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Powered by DeepSeek AI models
- Built with Flask 