# Speech Recognition Chatbot

## Overview
This Python script implements a simple speech recognition chatbot using the `speech_recognition` library. It listens to user input through a microphone and recognizes spoken words, allowing for voice interaction. The program continues until the user says a command to exit.

## Features
- **Voice Input**: Utilizes the microphone to capture audio.
- **Speech Recognition**: Converts spoken words to text using Google’s speech recognition service.
- **Exit Commands**: Listens for specific commands to terminate the conversation.
- **Error Handling**: Handles situations where the speech is not recognized, prompting the user to try again.

## Requirements
- Python 3.x
- `speech_recognition` library
- `pyaudio` library
