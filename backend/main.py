from PIL import Image
import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key="AIzaSyC1_L895LwUqVMcP22OFIP2eVt4WkFjd78")

# Load the image from a file
image_path = 'image.png'
image = Image.open(image_path)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')

# Create a prompt with both text and the image
prompt = "what is the ingredient of this recipe? I would the result in a table (without header) with first column the ingridient in italian and the second the quantity. If you dont find any recipe get me this string \"NO RECIPE FOUND\""
response = model.generate_content([prompt, image])

# Print the model's response
print(response.text)