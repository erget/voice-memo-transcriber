#!/usr/bin/env python3

import sys
import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU*")

def transcribe_ogg(file_path):
    model = whisper.load_model("base")  # or "small", "medium", etc.
    result = model.transcribe(file_path)
    print(result["text"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: transcribe.py <audio_file.ogg>")
        sys.exit(1)
    
    ogg_file = sys.argv[1]
    transcribe_ogg(ogg_file)

