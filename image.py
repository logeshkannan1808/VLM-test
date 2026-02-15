from google import genai
from PIL import Image
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def analyze_image(image_path, question=None):
    image = Image.open(image_path)

    prompt = (
        "Give a clear summary of this image."
        if question is None
        else question
    )

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=[prompt, image],
    )

    return response.text

if __name__ == "__main__":
    print("IMAGE SUMMARY:")
    print(analyze_image("sample.jpg"))

    print("\nIMAGE QUESTION:")
    print(analyze_image("sample.jpg", "What objects are visible in the image?"))
