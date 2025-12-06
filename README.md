# KING_BLESS Voice Assistant for Android Termux

A voice-controlled assistant that can open websites and apps on Android using Termux.

## Features
- Voice recognition for commands
- Open websites (YouTube, Google, Facebook, etc.)
- Open Android apps (WhatsApp, Camera, Gallery, etc.)
- Time and date queries
- Easy to extend with new commands

## Installation

1. **Install Termux** from Google Play Store
2. **Run these commands in Termux:**

```bash
# Update packages
pkg update && pkg upgrade

# Install required packages
pkg install python git

# Clone or create the files
git clone [https://github.com/pokuahnyarko-pixel/Kingbless-VOICE-ASSISTANT-created-by-KINGSLEY-NYARKO-.git]

# Make setup script executable
chmod +x setup.sh

# Run setup script
./setup.sh
