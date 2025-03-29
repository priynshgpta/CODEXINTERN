import speech_recognition as sr
import pyttsx3
import webbrowser

def voice_assistant():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    with sr.Microphone() as source:
        print("Microphone is open, adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            print("Audio captured, processing...")
            command = recognizer.recognize_google(audio)
            print("Command:", command)
            engine.say("You said " + command)
            engine.runAndWait()
            
            # Perform a web search if the command contains the word "search"
            if "search" in command.lower():
                search_query = command.lower().replace("search", "").strip()
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                print(f"Searching for: {search_query}")
                engine.say(f"Searching for {search_query}")
                engine.runAndWait()
                
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error connecting to speech recognition service: {e}")
        except AttributeError as e:
            print(f"Attribute error: {e}")

if __name__ == "__main__":
    voice_assistant()