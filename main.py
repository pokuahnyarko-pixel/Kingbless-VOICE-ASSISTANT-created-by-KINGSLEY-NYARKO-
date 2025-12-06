#!/usr/bin/env python3
"""
KING_BLESS Voice Assistant for Android Termux
"""
import speech_recognition as sr
import webbrowser
import os
import sys
import subprocess
import time
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

class KingBlessAssistant:
    def __init__(self):
        self.name = "KING_BLESS"
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.commands = {
            'open youtube': self.open_youtube,
            'open whatsapp': self.open_whatsapp,
            'open google': self.open_google,
            'open facebook': self.open_facebook,
            'open instagram': self.open_instagram,
            'open twitter': self.open_twitter,
            'open gmail': self.open_gmail,
            'open maps': self.open_maps,
            'open calculator': self.open_calculator,
            'open camera': self.open_camera,
            'open gallery': self.open_gallery,
            'open settings': self.open_settings,
            'open browser': self.open_browser,
            'open termux': self.open_termux,
            'what time is it': self.tell_time,
            'what is the date': self.tell_date,
            'exit': self.exit_program,
            'quit': self.exit_program,
            'stop': self.exit_program,
        }
        
        print(f"\n{'='*50}")
        print(f"   WELCOME TO {self.name} VOICE ASSISTANT")
        print(f"{'='*50}")
        print("Commands available:")
        for cmd in self.commands.keys():
            print(f"  • {cmd}")
        print(f"{'='*50}\n")
    
    def listen(self):
        """Listen for voice commands"""
        with self.microphone as source:
            print("🎤 Listening... (Speak now)")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("✓ Processing your command...")
                return audio
            except sr.WaitTimeoutError:
                print("✗ No speech detected")
                return None
    
    def recognize_speech(self, audio):
        """Convert speech to text"""
        try:
            text = self.recognizer.recognize_google(audio).lower()
            print(f"🗣 You said: {text}")
            return text
        except sr.UnknownValueError:
            print("✗ Could not understand audio")
            return None
        except sr.RequestError:
            print("✗ Speech recognition service unavailable")
            return None
    
    def open_url(self, url):
        """Open URL in browser using Termux"""
        try:
            # Try using termux-open-url first (for websites)
            subprocess.run(['termux-open-url', url], check=True)
            print(f"✓ Opening: {url}")
            return True
        except:
            # Fallback to am start for Android apps
            try:
                subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', url], check=True)
                print(f"✓ Opening: {url}")
                return True
            except Exception as e:
                print(f"✗ Failed to open {url}: {e}")
                return False
    
    def open_app(self, app_package):
        """Open Android app using package name"""
        try:
            subprocess.run(['am', 'start', '-n', app_package], check=True)
            print(f"✓ Opening app: {app_package}")
            return True
        except Exception as e:
            print(f"✗ Failed to open app: {e}")
            return False
    
    def open_youtube(self):
        """Open YouTube"""
        return self.open_url('https://youtube.com')
    
    def open_whatsapp(self):
        """Open WhatsApp"""
        return self.open_app('com.whatsapp/.HomeActivity')
    
    def open_google(self):
        """Open Google"""
        return self.open_url('https://google.com')
    
    def open_facebook(self):
        """Open Facebook"""
        return self.open_url('https://facebook.com')
    
    def open_instagram(self):
        """Open Instagram"""
        return self.open_url('https://instagram.com')
    
    def open_twitter(self):
        """Open Twitter"""
        return self.open_url('https://twitter.com')
    
    def open_gmail(self):
        """Open Gmail"""
        return self.open_url('https://mail.google.com')
    
    def open_maps(self):
        """Open Google Maps"""
        return self.open_url('https://maps.google.com')
    
    def open_calculator(self):
        """Open Calculator app"""
        return self.open_app('com.google.android.calculator/com.android.calculator2.Calculator')
    
    def open_camera(self):
        """Open Camera app"""
        return self.open_app('com.android.camera2/com.android.camera.CameraLauncher')
    
    def open_gallery(self):
        """Open Gallery app"""
        return self.open_app('com.android.gallery3d/.app.MainActivity')
    
    def open_settings(self):
        """Open Settings app"""
        return self.open_app('com.android.settings/.Settings')
    
    def open_browser(self):
        """Open Browser app"""
        return self.open_app('com.android.chrome/com.google.android.apps.chrome.Main')
    
    def open_termux(self):
        """Bring Termux to foreground"""
        try:
            subprocess.run(['am', 'start', '-n', 'com.termux/com.termux.app.TermuxActivity'], check=True)
            print("✓ Opening Termux")
            return True
        except Exception as e:
            print(f"✗ Failed to open Termux: {e}")
            return False
    
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"🕐 Current time is: {current_time}")
        return True
    
    def tell_date(self):
        """Tell current date"""
        current_date = datetime.now().strftime("%B %d, %Y")
        print(f"📅 Today's date is: {current_date}")
        return True
    
    def exit_program(self):
        """Exit the program"""
        print(f"\n👋 Goodbye! {self.name} is shutting down...")
        sys.exit(0)
    
    def execute_command(self, command_text):
        """Execute the recognized command"""
        for cmd, func in self.commands.items():
            if cmd in command_text:
                return func()
        
        print("✗ Command not recognized")
        print("💡 Try: 'open youtube', 'open whatsapp', etc.")
        return False
    
    def run(self):
        """Main loop"""
        print("🎤 Speak a command or type 'exit' to quit\n")
        
        while True:
            # Listen for voice input
            audio = self.listen()
            
            if audio:
                # Recognize speech
                text = self.recognize_speech(audio)
                
                if text:
                    # Execute command
                    self.execute_command(text)
            
            print("-" * 40)
            time.sleep(1)

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['speechrecognition', 'pyaudio']
    
    print("🔍 Checking dependencies...")
    
    try:
        import speech_recognition
        print("✓ speech_recognition is installed")
    except ImportError:
        print("✗ speech_recognition not installed")
        return False
    
    try:
        import pyaudio
        print("✓ pyaudio is installed")
    except ImportError:
        print("✗ pyaudio not installed")
        print("  Run: pip install pyaudio")
        return False
    
    # Check Termux permissions
    print("\n🔍 Checking Termux permissions...")
    try:
        subprocess.run(['termux-microphone-record'], capture_output=True)
        print("✓ Microphone permission granted")
    except:
        print("⚠  Microphone permission might be needed")
        print("  Run: termux-microphone-record")
    
    return True

def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    os.system("pip install speechrecognition pyaudio")
    print("✓ Dependencies installed")

if __name__ == "__main__":
    # Check if running on Termux
    if not os.path.exists('/data/data/com.termux/files/home'):
        print("⚠  Warning: This script is designed for Termux on Android")
        print("   Some features may not work properly\n")
    
    # Check dependencies
    if not check_dependencies():
        response = input("\nDo you want to install missing dependencies? (y/n): ")
        if response.lower() == 'y':
            install_dependencies()
        else:
            print("Some features may not work without dependencies")
    
    # Start the assistant
    assistant = KingBlessAssistant()
    
    try:
        assistant.run()
    except KeyboardInterrupt:
        print(f"\n\n👋 {assistant.name} stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check your microphone permissions and try again")