from google import genai
import os
import base64

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

text = """
Retrieval-Augmented Generation, commonly known as RAG, is an AI architecture that
combines information retrieval with large language models. Instead of relying only
on a model’s internal knowledge, RAG retrieves relevant documents from external
sources such as databases, vector stores, or knowledge bases.

The retrieved information is then provided as context to the language model, which
generates more accurate, up-to-date, and trustworthy responses. RAG is widely used
in chatbots, enterprise search, question answering systems, and document analysis
applications.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Read this text aloud clearly:\n{text}"
)

audio_bytes = base64.b64decode(
    response.candidates[0].content.parts[0].inline_data.data
)

with open("rag_sample_audio.mp3", "wb") as f:
    f.write(audio_bytes)

print("✅ MP3 created: rag_sample_audio.mp3")
