#!/bin/bash
set -e

VENV_DIR=".venv-transcriber"

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    "$VENV_DIR/bin/pip" install --upgrade pip
    "$VENV_DIR/bin/pip" install openai-whisper
fi

"$VENV_DIR/bin/python" transcribe.py "$1"

