import openai, os
from dotenv import load_dotenv

load_dotenv()

# Your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Function to generate an image from a prompt using DALL-E
def generate_image_url(prompt):
    try:
        # Generate an image using DALL-E
        response = openai.Image.create(prompt=prompt, n=1)

        # Extract the URL of the generated image
        image_url = response['data'][0]['url']

        return image_url
    except openai.error.OpenAIError as e:
        # Handle errors from the OpenAI API
        print(f"An error occurred: {e}")

# Example usage:
prompt = "a two-story pink house shaped like a shoe"
image_url = generate_image_url(prompt)
print(f"Generated image URL: {image_url}")
