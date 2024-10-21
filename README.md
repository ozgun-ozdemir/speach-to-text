# Speech Recognition
This Python script implements a speech recognition feature that listens for user input through a microphone, transcribes it, and allows voice interaction until an exit command is given.

## Features
- **Voice Input**: Utilizes the microphone to capture audio.
- **Speech Recognition**: Converts spoken words to text using Google’s speech recognition service.
- **Exit Commands**: Listens for specific commands to terminate the conversation.
- **Error Handling**: Handles situations where the speech is not recognized, prompting the user to try again.

## Requirements
- Python 3.x
- `speech_recognition` library
- `pyaudio` library
