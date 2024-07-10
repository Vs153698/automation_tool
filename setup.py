from setuptools import setup

APP = ['main.py']  # Your main Python script
DATA_FILES = ['recorder.py', 'player.py','gui.py']  # Include necessary files and directories
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pynput', 'pyautogui', 'tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
