# Please note that you can not run your add-on from within IDE - you will get errors. 
# Add-ons need to be run from within Anki, which is covered in the A Basic Add-on section.

import openai, os
from dotenv import load_dotenv

load_dotenv()

# Your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_prompt(word):
    try:
        # Generate sample sentence with a word
        sampleSentence = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust the model if necessary
            messages=[
                {
                "role": "user",
                "content": f"Give me a sample sentence (max. 7 words) in Hungarian that uses the word I provided that a B1 learner of the language would understand. The word is: {word}. Return only the Hungarian sentence.",
                }   
            ],
            max_tokens=60
        )
        
        # Extract the text of the generated sentence
        sentence = sampleSentence.choices[0].message.content

        translated_sentence=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role":"user",
                    "content":f"Translate this Hungarian sentence to English: \"{sentence}\""
                }
            ]
        )
        
        translated_sentence=translated_sentence.choices[0].message.content

        # Use this sentence to create an image prompt
        imagePrompt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust the model if necessary
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI trained to assist with generating creative and detailed descriptions for images. When provided with a sentence, you will create a vivid, detailed prompt that can be used to generate an image."
                },
                {
                "role": "user",
                "content": f"I want to turn this Hungarian sentence into a detailed image prompt for DALL-E (max 25 words). The sentence is: \"{sentence}\ which translates to \"{translated_sentence}\". Create a descriptive prompt based on this. Please return only the prompt."
                }   
            ],
            max_tokens=60
        )
        
        # Extract the text of the image prompt
        prompt_for_image = imagePrompt.choices[0].message.content

        return sentence, translated_sentence, prompt_for_image
    except openai.error.OpenAIError as e:
        # Handle errors from the OpenAI API
        print(f"An error occurred: {e}")
        return None, None, None

word = input("Gimme the Hungarian word: ")
sentence, translated_sentence, prompt_for_image = generate_prompt(word)
if sentence and prompt_for_image:
    print("Sentence:", sentence)
    print("Translated sentence:", translated_sentence)
    print("Image Prompt:", prompt_for_image)

# Function to generate an image from a prompt using DALL-E
def generate_image_url(prompt):
    try:
        # Generate an image using DALL-E
        # Note: This assumes you are using the correct parameters for the Image creation endpoint.
        # Check the latest API documentation for any changes.
        response = openai.Image.create(prompt=prompt, n=1)

        # Extract the URL of the generated image
        image_url = response.data[0].url

        # Return the sentence, image prompt, and image URL
        return image_url
    except openai.error.OpenAIError as e:
        # Handle errors from the OpenAI API
        print(f"An error occurred: {e}")
        return None

# Example usage:
image_url = generate_image_url(prompt_for_image)
if image_url:
    print("Image URL:", image_url)