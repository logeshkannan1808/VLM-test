# 🎯 Multimodal File Analyzer (Image, Video, Audio, Text)

A Python-based multimodal analyzer powered by **Google Gemini (genai)**
that can:

-   🖼 Analyze Images\
-   🎬 Analyze Videos (via frame extraction)\
-   🎙 Transcribe & Summarize Audio\
-   📄 Summarize Text Files

------------------------------------------------------------------------

## 🚀 Features

-   Uses **Gemini 2.5 Flash model**
-   Extracts frames from videos using OpenCV
-   Uploads audio files for transcription
-   Supports custom questions per input
-   Simple CLI interface

------------------------------------------------------------------------

## 📦 Requirements

Install dependencies:

``` bash
pip install -r requirements.txt
```

### requirements.txt

    google-genai
    Pillow
    opencv-python

------------------------------------------------------------------------

## 🔑 Setup

### 1️⃣ Get Gemini API Key

Get your API key from Google AI Studio.

### 2️⃣ Set Environment Variable

#### Windows (PowerShell)

``` powershell
setx GEMINI_API_KEY "your_api_key_here"
```

#### Mac/Linux

``` bash
export GEMINI_API_KEY="your_api_key_here"
```

------------------------------------------------------------------------

## ▶️ How to Run

``` bash
python main.py
```

You will be prompted:

    Choose input type: image | video | audio | text

Example:

    Type: image
    File path: sample.jpg
    Question (press Enter to skip):

------------------------------------------------------------------------

## 🖼 Image Analysis

-   Provides summary
-   Can answer custom questions

------------------------------------------------------------------------

## 🎬 Video Analysis

-   Extracts frames every 3 seconds
-   Maximum 6 frames (configurable)
-   Summarizes video content

------------------------------------------------------------------------

## 🎙 Audio Analysis

-   Uploads audio file to Gemini
-   Transcribes content
-   Provides summary
-   Can answer specific questions about audio

------------------------------------------------------------------------

## 📄 Text File Analysis

-   Reads `.txt` file
-   Summarizes content
-   Answers contextual questions

------------------------------------------------------------------------

## 🛠 Project Structure

    .
    ├── main.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙ Models Used

All analysis uses:

    models/gemini-2.5-flash

------------------------------------------------------------------------

## ⚠ Notes

-   Large video files may take longer
-   Internet connection required
-   API usage costs may apply
-   Ensure valid API key is set

------------------------------------------------------------------------

## 👨‍💻 Author

Built with ❤️ using Google Gemini
