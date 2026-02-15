import ollama
from PIL import Image
import base64
import io

def image_to_base64(image_path):
    img = Image.open(image_path).convert("RGB")
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode()

def analyze_image(image_path, question=None):
    image_b64 = image_to_base64(image_path)

    prompt = (
        "Summarize this image clearly."
        if question is None
        else f"Answer this question based on the image: {question}"
    )

    response = ollama.chat(
        model="qwen3-vl",
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [image_b64],
            }
        ],
    )

    return response["message"]["content"]

# Example usage
if __name__ == "__main__":
    print("IMAGE SUMMARY:")
    print(analyze_image("sample.jpg"))

    print("\nIMAGE QUESTION:")
    print(analyze_image("sample.jpg", "What objects are visible in the image?"))
