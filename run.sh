#!/bin/bash

# Dragon Priestess Mermaid School - Techno Magical Landing Page Runner
# 🐉🧜‍♀️✨

echo "🌟 Awakening the Dragon Priestess Mermaid School..."
echo "🔮 Preparing the mystical web portal..."

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Python not found. Please install Python to run the server."
    exit 1
fi

echo "✨ Using $PYTHON_CMD to serve the temple..."

# Make the server script executable
chmod +x server.py

# Run the server
$PYTHON_CMD server.py
