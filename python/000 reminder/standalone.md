Build a standalone Linux executable:
```
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install pyinstaller
pyinstaller --version
```
in venv you need to install the dependencies again, in this case:
```
pip install pyqt6 markdown pyinstaller
```

```
pyinstaller --onefile --windowed mdview.py
```
The executable will be:

`dist/mdviewer`
