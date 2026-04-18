from deep_translator import GoogleTranslator
from gtts import gTTS
import os

def translate_text(text, target_lang):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

def speak_text(text, lang, filename="speech.mp3"):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    # This opens the file in default media player (Windows)
    os.system(f"start {filename}")

def main():
    print("1: Kannada → English")
    print("2: English → Kannada")

    choice = input("Choose option from 1 or 2: ")
    text = input("Enter text: ")

    if choice == "1":
        translated = translate_text(text, "en")
        print("Translated:", translated)
        speak_text(translated, "en")

    elif choice == "2":
        translated = translate_text(text, "kn")
        print("Translated:", translated)
        speak_text(translated, "kn")

    else:
        print("Invalid choice selected. Please choose either 1 or 2.")

if __name__ == "__main__":
    main()