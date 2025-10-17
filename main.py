import pyttsx3
import speech_recognition as sr
import datetime
import pyautogui
import webbrowser
import psutil
import os
import subprocess

# ------------------ INIT ------------------
engine = pyttsx3.init()

def speak(text):
    """Speak text aloud"""
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-US")
        print(f"Command: {query}")
        return query.lower()
    except:
        print("Could not recognize command.")
        return ""

# ------------------ COMMANDS ------------------
commands = {
    "take screenshot": [
        "screenshot",
        "take a screenshot",
        "capture screen"
    ],
    "open youtube": [
        "open youtube",
        "play youtube"
    ],
    "open chrome": [
        "open chrome",
        "open google chrome"
    ],
    "open vscode": [
        "open vscode",
        "open code",
        "open visual studio code"
    ],
    "what time": [
        "what time",
        "time",
        "what's the time"
    ],
    "what battery": [
        "battery",
        "what's my battery",
        "battery percentage"
    ],
    "help": [
        "help",
        "commands",
        "what can i say"
    ]
}

# ------------------ FUNCTIONS ------------------
def take_screenshot():
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img = pyautogui.screenshot()
    img.save(filename)
    speak(f"Screenshot saved as {filename}")
    print(f"Screenshot saved: {filename}")

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("YouTube opened")

def open_chrome():
    try:
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("Chrome opened")
    except:
        speak("Chrome not found")

def open_vscode():
    try:
        subprocess.Popen(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        speak("VS Code opened")
    except:
        speak("VS Code not found")

def report_time():
    now = datetime.datetime.now()
    speak(f"The current time is {now.hour}:{now.minute:02d}")
    print(f"Current time: {now.hour}:{now.minute:02d}")

def report_battery():
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery level is {battery.percent} percent")
        print(f"Battery: {battery.percent}%")
    else:
        speak("Battery not found")
        print("Battery not found")

def list_commands():
    cmds = ", ".join(commands.keys())
    speak(f"You can say the following commands: {cmds}")
    print(f"Commands: {cmds}")

# ------------------ MAIN LOOP ------------------
while True:
    query = listen()
    if not query:
        continue

    if any(phrase in query for phrase in commands["take screenshot"]):
        take_screenshot()
    elif any(phrase in query for phrase in commands["open youtube"]):
        open_youtube()
    elif any(phrase in query for phrase in commands["open chrome"]):
        open_chrome()
    elif any(phrase in query for phrase in commands["open vscode"]):
        open_vscode()
    elif any(phrase in query for phrase in commands["what time"]):
        report_time()
    elif any(phrase in query for phrase in commands["what battery"]):
        report_battery()
    elif any(phrase in query for phrase in commands["help"]):
        list_commands()
    elif "exit" in query or "quit" in query:
        speak("Program closed")
        break
    else:
        speak("Command not recognized")
        print("Command not recognized")
