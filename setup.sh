#!/data/data/com.termux/files/usr/bin/bash

echo "=========================================="
echo "  KING_BLESS Voice Assistant Setup"
echo "=========================================="

# Update packages
echo "[1/5] Updating packages..."
pkg update -y && pkg upgrade -y

# Install required packages
echo "[2/5] Installing Python and dependencies..."
pkg install -y python python-pip
pkg install -y clang
pkg install -y libjpeg-turbo libpng
pkg install -y ffmpeg
pkg install -y termux-api

# Install Python packages
echo "[3/5] Installing Python libraries..."
pip install --upgrade pip
pip install speechrecognition
pip install pyaudio

# Grant permissions
echo "[4/5] Setting up permissions..."
termux-microphone-record

# Create desktop shortcut
echo "[5/5] Creating startup script..."
cat > $HOME/start-kingbless.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd $HOME
python main.py
EOF

chmod +x $HOME/start-kingbless.sh

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start KING_BLESS Voice Assistant:"
echo "1. Run: chmod +x setup.sh"
echo "2. Run: ./setup.sh (if not done)"
echo "3. Run: python main.py"
echo "4. Or run: ./start-kingbless.sh"
echo ""
echo "Note: Make sure to grant microphone permission"
echo "      when prompted by Termux"
echo "=========================================="