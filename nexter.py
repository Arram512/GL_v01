import speech_recognition as sr 
import pyttsx3
import sys
import subprocess, pyautogui

pyautogui.FAILSAFE = False

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk('Слушаю')

def command():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1) as source:
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language = 'en-EN').lower()
        print(f'[log] Услыхал: {task}')
    except:
        #talk('Неопознанная команда ')
        task = command()

    return task

def working(task):
    if 'page' in task:
        pyautogui.press('space')
    elif 'next' in task:
        
        pyautogui.click(1366, 768)
        pyautogui.press('space')
        pyautogui.press('space')
        pyautogui.press('space')
        pyautogui.click(823, 180)





while True:
    working(command())

    