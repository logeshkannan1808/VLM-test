# 🎯 Multimodal File Analyzer (Image, Video, Audio, Text)

A Python-based multimodal analyzer powered by **Google Gemini (genai)**
that can:

-   🖼 Analyze Images\
-   🎬 Analyze Videos (via frame extraction)\
-   🎙 Transcribe & Summarize Audio\
-   📄 Summarize Text Files

------------------------------------------------------------------------

# 🚀 Complete Setup Guide (From Scratch)

## 1️⃣ Clone the Repository

``` bash
git clone https://github.com/logeshkannan1808/VLM-test.git
cd VLM-test
```

If this is your local project, you can skip cloning and just navigate to
the project folder.

------------------------------------------------------------------------

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

``` bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

``` bash
python3 -m venv venv
source venv/bin/activate
```

------------------------------------------------------------------------

## 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### requirements.txt

    google-genai
    Pillow
    opencv-python

------------------------------------------------------------------------

# 🔑 Setting GEMINI_API_KEY in Windows

## ✅ Method 1 --- PowerShell (Permanent)

Open **PowerShell as Administrator**:

``` powershell
setx GEMINI_API_KEY "your_api_key_here"
```

Close the terminal and open a new one.

### Check if it is set:

``` powershell
echo $env:GEMINI_API_KEY
```

------------------------------------------------------------------------

## ✅ Method 2 --- Command Prompt (CMD)

Set:

``` cmd
setx GEMINI_API_KEY "your_api_key_here"
```

Check (open new CMD window):

``` cmd
echo %GEMINI_API_KEY%
```

------------------------------------------------------------------------

## ✅ Temporary (Session Only)

PowerShell:

``` powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

CMD:

``` cmd
set GEMINI_API_KEY=your_api_key_here
```

⚠️ Temporary variables disappear after closing terminal.

------------------------------------------------------------------------

## ✅ GUI Method (Permanent)

1.  Press Win + R\
2.  Type `sysdm.cpl`\
3.  Go to **Advanced** → **Environment Variables**\
4.  Click **New** under User Variables
    -   Name: GEMINI_API_KEY\
    -   Value: your_api_key_here\
5.  Click OK\
6.  Restart terminal

------------------------------------------------------------------------

## 🧪 Test in Python

``` python
import os
print(os.environ.get("GEMINI_API_KEY"))
```

If it prints your key → Setup successful.

------------------------------------------------------------------------

# ▶️ How to Run the Project

``` bash
python main.py
```

You will see:

    Choose input type: image | video | audio | text

Example:

    Type: image
    File path: sample.jpg
    Question (press Enter to skip):

------------------------------------------------------------------------

# 🖼 Image Analysis

-   Provides summary\
-   Can answer custom questions

------------------------------------------------------------------------

# 🎬 Video Analysis

-   Extracts frames every 3 seconds\
-   Maximum 6 frames (configurable)\
-   Summarizes video content

------------------------------------------------------------------------

# 🎙 Audio Analysis

-   Uploads audio file to Gemini\
-   Transcribes content\
-   Provides summary\
-   Supports custom questions

------------------------------------------------------------------------

# 📄 Text File Analysis

-   Reads `.txt` file\
-   Summarizes content\
-   Answers contextual questions

------------------------------------------------------------------------

# 🛠 Project Structure

    .
    ├── main.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# ⚠ Notes

-   Internet connection required\
-   Large videos may take longer\
-   Ensure GEMINI_API_KEY is correctly set\
-   API usage costs may apply

------------------------------------------------------------------------

# 👨‍💻 Built With

Google Gemini (genai) + Python
