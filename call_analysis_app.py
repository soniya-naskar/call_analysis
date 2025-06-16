import whisper
import os
import nltk
import librosa
import numpy as np
from keybert import KeyBERT
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

# Initialize models
print("Loading models...")
whisper_model = whisper.load_model("base")  # you can use 'small' or 'medium' if you have more resources
kw_model = KeyBERT('sentence-transformers/all-MiniLM-L6-v2')
nltk.download('vader_lexicon')
sentiment_analyzer = SentimentIntensityAnalyzer()
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small", framework="pt")

# Helper Functions

def transcribe_audio(file_path):
    print("Transcribing...")
    result = whisper_model.transcribe(file_path)
    return result['text'], result['segments']

def analyze_sentiment(text):
    return sentiment_analyzer.polarity_scores(text)

def extract_keywords(text):
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=5)
    return [kw[0] for kw in keywords]

def summarize_text(text):
    if len(text.split()) < 50:
        return text  # too short to summarize
    summary = summarizer(text, max_length=60, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def process_segments(segments):
    analysis = []
    for seg in segments:
        seg_text = seg['text']
        start = seg['start']
        end = seg['end']
        sentiment = analyze_sentiment(seg_text)
        keywords = extract_keywords(seg_text)
        analysis.append({
            'start': start,
            'end': end,
            'text': seg_text,
            'keywords': keywords,
            'sentiment': sentiment
        })
    return analysis

def print_analysis(analysis):
    for seg in analysis:
        print(f"\nTime: {seg['start']:.2f}s - {seg['end']:.2f}s")
        print(f"Text: {seg['text']}")
        print(f"Keywords: {seg['keywords']}")
        print(f"Sentiment: {seg['sentiment']}")

def main(audio_path):
    full_transcript, segments = transcribe_audio(audio_path)
    print("\n--- Full Transcription ---\n")
    print(full_transcript)
    
    segment_analysis = process_segments(segments)
    print("\n--- Segment-wise Analysis ---")
    print_analysis(segment_analysis)
    
    summary = summarize_text(full_transcript)
    print("\n--- Summary ---\n")
    print(summary)

# Run
if __name__ == "__main__":
    # Place your call recording (wav/mp3) in the same folder and update the file name
    audio_file = "audio_samples\\call_sample.wav"  
    if not os.path.exists(audio_file):
        print(f"Audio file {audio_file} not found!")
    else:
        main(audio_file)
