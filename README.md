# 📞 Call Analysis Application

This project is a simple **Call Analysis Application** that takes a short call recording as input, produces a full transcription, identifies and timestamps key topics, detects sentiment shifts, and generates a concise summary of the conversation.

---

## 🚀 Features

- ✅ Audio transcription using OpenAI Whisper (open-source model)
- ✅ Topic extraction using KeyBERT
- ✅ Sentiment analysis using NLTK VADER
- ✅ Summarization using HuggingFace Transformers (T5-small model)
- ✅ Fully open-source implementation

---

## 🗂️ Project Structure

call_analysis/
│
├── call_analysis_app.py # Main application code
├── requirements.txt # Python dependencies
├── audio_samples/ # Folder containing input audio files
│ └── call_sample.wav # Sample call recording (in .wav format)
├── ffmpeg.exe # (for Windows quick fix, ffmpeg binary)
├── Call_Analysis_Report.docx # Project report
└── README.md # Project documentation (this file)


---

## 📥 Installation

### 1️⃣ Clone the repository or copy project files.

### 2️⃣ Create and activate virtual environment:

```bash
# Create virtual env
python -m venv call_analysis_env

# Activate on Windows
call_analysis_env\Scripts\activate

3️⃣ Install dependencies:
pip install -r requirements.txt

✅ Make sure you have ffmpeg available.
✅ Easiest: place ffmpeg.exe directly into the project folder.

🔧 Whisper model installation
Install Whisper via:

pip install git+https://github.com/openai/whisper.git

or

pip install whisper

🎤 Input Audio
Input audio files should be in .wav or .mp3 format.

Whisper works best with 16kHz sample rate.

You can test using provided sample: audio_samples/call_sample.wav

💻 Usage
Run the application from terminal:

python call_analysis_app.py

📝 Sample Output
Full transcription printed

Segment-wise:

Timestamps

Extracted keywords

Sentiment scores

Overall summary generated using T5

--- Full Transcription ---

 All of our demos went very well. We had great meetings with partners and potential prospects, and we had incredible presentations to our broader 
thought leadership audience.

--- Segment-wise Analysis ---

Time: 0.00s - 3.84s
Text:  All of our demos went very well.
Keywords: ['demos went', 'demos', 'went']
Sentiment: {'neg': 0.0, 'neu': 0.715, 'pos': 0.285, 'compound': 0.3384}

Time: 3.84s - 11.16s
Text:  We had great meetings with partners and potential prospects, and we had incredible presentations
Keywords: ['great meetings', 'incredible presentations', 'presentations', 'meetings partners', 'partners potential']
Sentiment: {'neg': 0.0, 'neu': 0.656, 'pos': 0.344, 'compound': 0.743}

Time: 11.16s - 13.36s
Text:  to our broader thought leadership audience.
Keywords: ['thought leadership', 'leadership audience', 'broader thought', 'leadership', 'broader']
Sentiment: {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

--- Summary ---

 All of our demos went very well. We had great meetings with partners and potential prospects, and we had incredible presentations to our broader s to our broader thought leadership audience.

⚠ Common Issues
FileNotFoundError → Install or place ffmpeg.exe properly.

Whisper warnings about FP16 → Safe to ignore when running on CPU.

Long processing times → Whisper is compute-intensive on CPU.

📚 Models Used
Task	Library / Model
Transcription	OpenAI Whisper (base model)
Keyword Extraction	KeyBERT + sentence-transformers
Sentiment Analysis	NLTK VADER
Summarization	HuggingFace T5-small
Audio Processing	pydub, librosa

🙏 Acknowledgements
OpenAI Whisper

HuggingFace Transformers

NLTK

KeyBERT

PyDub

🧑 Author
Soniya Naskar

