from gtts import gTTS
import os
# Optional: To play the generated speech directly
# from playsound import playsound

# Function to convert text to speech and save it to an audio file
def text_to_speech(text, language='en', slow=False, output_file="output.mp3"):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=slow)
    
    # Save the speech to a file
    tts.save(output_file)
    print(f"Speech saved to {output_file}")

    # Optional: Play the audio file
    # playsound(output_file)

# Example usage:
text = "Hello, welcome to the Text to Speech demo using Python!"
text_to_speech(text, language='en', slow=False)
