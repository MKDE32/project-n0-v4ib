# Build a standalone Linux executable:
# venv & pyinstaller
```
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install pyinstaller
pyinstaller --version
```

# dependencies venv
```
pip install pyqt6 markdown pyinstaller
```

# build standalone
```
pyinstaller --onefile --windowed mdview.py
```

# dependencies system
```
sudo apt install libxcb-cursor0
```

The executable will be:  
`dist/mdviewer`










