import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert speech to text from an audio file
def audio_file_to_text(file_path):
    # Load the audio file
    with sr.AudioFile(file_path) as source:
        # Adjust for ambient noise and record
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.record(source)
        
        # Recognize speech using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print("Text from audio: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Function to convert speech to text from microphone
def microphone_to_text():
    # Use microphone as source
    with sr.Microphone() as source:
        print("Please speak...")
        
        # Adjust for ambient noise and listen
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        
        # Recognize speech using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print("Text from microphone: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Example usage:
# Convert speech from an audio file to text
audio_file_to_text('path_to_audio_file.wav')

# Convert speech from the microphone to text
# microphone_to_text()
