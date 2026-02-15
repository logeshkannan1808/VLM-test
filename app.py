from google import genai
from PIL import Image
import cv2
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

IMAGE_MODEL = "models/gemini-2.5-flash"
AUDIO_MODEL = "models/gemini-2.5-flash"
TEXT_MODEL  = "models/gemini-2.5-flash"


def analyze_image(path, question=None):
    image = Image.open(path)

    prompt = (
        "Give a clear summary of this image."
        if question is None
        else question
    )

    response = client.models.generate_content(
        model=IMAGE_MODEL,
        contents=[prompt, image],
    )

    return response.text

# -----------------------
# Video Analysis (frames)
# -----------------------
def extract_frames(video_path, every_n_seconds=3, max_frames=6):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps * every_n_seconds)

    frames = []
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % interval == 0:
            frame_rgb = frame[:, :, ::-1]
            frames.append(Image.fromarray(frame_rgb))

            if len(frames) >= max_frames:
                break

        count += 1

    cap.release()
    return frames

def analyze_video(path, question=None):
    frames = extract_frames(path)

    prompt = (
        "Summarize the video based on these frames."
        if question is None
        else question
    )

    response = client.models.generate_content(
        model=IMAGE_MODEL,
        contents=[prompt] + frames,
    )

    return response.text

# -----------------------
# Audio Analysis
# -----------------------
def analyze_audio(path, question=None):
    audio_file = client.files.upload(file=path)

    prompt = (
        "Transcribe and summarize this audio."
        if question is None
        else question
    )

    response = client.models.generate_content(
        model=AUDIO_MODEL,
        contents=[prompt, audio_file],
    )

    return response.text

# -----------------------
# Text File Analysis
# -----------------------
def analyze_text_file(path, question=None):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    prompt = (
        f"Summarize the following text:\n\n{content}"
        if question is None
        else f"{question}\n\n{content}"
    )

    response = client.models.generate_content(
        model=TEXT_MODEL,
        contents=prompt,
    )

    return response.text

# -----------------------
# Main Selector
# -----------------------
def analyze(input_type, path, question=None):
    if input_type == "image":
        return analyze_image(path, question)
    elif input_type == "video":
        return analyze_video(path, question)
    elif input_type == "audio":
        return analyze_audio(path, question)
    elif input_type == "text":
        return analyze_text_file(path, question)
    else:
        raise ValueError("Invalid input type")

# -----------------------
# Example Usage
# -----------------------
if __name__ == "__main__":
    print("Choose input type: image | video | audio | text")
    input_type = input("Type: ").strip().lower()
    path = input("File path: ").strip()
    question = input("Question (press Enter to skip): ").strip()

    question = question if question else None

    result = analyze(input_type, path, question)
    print("\nRESULT:\n")
    print(result)
