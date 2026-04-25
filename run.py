#!/usr/bin/env python3
"""
Simple startup script for the Essay AI Agent
Run this script to start the Flask server and open the web app
"""

import os
import sys
import webbrowser
from pathlib import Path

# Check if .env file exists
env_file = Path('.env')
if not env_file.exists():
    print("❌ Error: .env file not found!")
    print("Please create a .env file with your OpenAI API key.")
    print("See README.md for instructions.")
    sys.exit(1)

# Check if HUGGINGFACE_API_KEY is set
if not os.getenv('HUGGINGFACE_API_KEY'):
    print("⚠️  Warning: HUGGINGFACE_API_KEY environment variable not set")
    print("Make sure it's defined in your .env file")

print("🚀 Starting Essay AI Agent...")
print("📱 Opening http://127.0.0.1:5000 in your browser...\n")

# Open browser
webbrowser.open('http://127.0.0.1:5000')

# Run Flask app
try:
    from app import app
    app.run(debug=True, host='127.0.0.1', port=5000)
except Exception as e:
    print(f"❌ Error starting server: {e}")
    sys.exit(1)
