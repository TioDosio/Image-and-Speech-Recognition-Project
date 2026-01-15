# Image-and-Speech-Recognition-Project

Image-and-Speech-Recognition-Project is a multimodal application that combines computer vision and speech recognition to detect face mask usage and interact with users via voice.

## Theme

Face mask detection with three categories: with mask, without mask, and incorrect mask, augmented with speech-based interaction for commands and feedback.

## Features

- **Face** mask classification into:
  - With mask  
  - Without mask  
  - Incorrect mask  
- Speech recognition component to handle spoken commands and confirmations.  
- Integrated pipeline where visual detection results can be narrated or controlled via voice.  

## Project Structure

Adjust this section to match your actual folders and filenames:

- `models/`: Trained image classification model for mask detection and any speech-model configuration files.
- `src/` or `app/`: Main application scripts (image capture, preprocessing, inference, audio recording, and speech-to-text logic).
- `data/`: Sample images or datasets organized by mask category.
- `requirements.txt`: Python dependencies for the vision and speech libraries.

## Installation

1. Create and activate a Python 3.8+ virtual environment.
2. Install dependencies (example set, adapt to your project):  
   - `opencv-python` for camera and image processing.
   - `tensorflow` or `torch` for loading and running the mask detection model.
   - `SpeechRecognition` and `pyaudio` (or another microphone backend) for speech input.
3. Ensure your system microphone is configured and accessible so speech recognition can capture audio correctly.

```bash
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

1. Start the main application (update the filename if different):

   ```bash
   python main.py
   ```

2. Allow the application to access your camera and microphone if prompted.  
3. Present faces to the camera; the system will classify mask usage and may produce spoken feedback or react to your voice commands, depending on how the interaction loop is configured.  

If the project includes a separate speech-only demo script, you can run it (for example):  

```bash
python speech_module.py
```

## Possible Improvements

- Train on a larger and more diverse mask dataset to improve robustness across lighting and demographics.  
- Add multilingual speech recognition and offline engines (e.g., local models) for privacy and reliability.  
- Provide a simple GUI or web dashboard for deployment at entrances, offices, or public spaces.
