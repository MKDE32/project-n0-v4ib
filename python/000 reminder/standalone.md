Build a standalone Linux executable:
```
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate







pip install pyinstaller
pyinstaller --onefile --windowed mdviewer.py
```
The executable will be:

`dist/mdviewer`
