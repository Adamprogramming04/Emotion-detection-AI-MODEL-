# Emotion Detection with Voice Feedback

This project uses OpenCV, DeepFace, and pyttsx3 to detect facial emotions (happy, sad, and angry) and provide real-time voice feedback based on the detected emotion.

## Features
- **Real-time emotion detection** using DeepFace.
- **Live webcam feed** processed with OpenCV.
- **Voice feedback** using pyttsx3 based on detected emotions.
- **Three detected emotions**: Happy, Sad, and Angry.

## Requirements
Ensure you have Python installed, then install the required libraries:
```sh
pip install opencv-python deepface pyttsx3 numpy
```

## How to Run
1. Connect a webcam to your computer.
2. Run the Python script:
   ```sh
   python emotion_detection.py
   ```
3. The script will detect your facial expression and provide voice feedback.
4. Press `q` to exit the program.

## Voice Feedback
- **Happy** → "You look happy! Keep smiling!"
- **Sad** → "You look sad. Hope things get better soon!"
- **Angry** → "You look angry. Maybe take it easy?"

## Notes
- If no face is detected, the program will continue running and wait for a face.
- You can modify the phrases in the script to customize voice responses.

## License
This project is open-source. Feel free to modify and improve!

## Future Improvements
- Add support for more emotions (e.g., surprise, fear, neutral).
- Improve accuracy with deep learning models.
- Implement a graphical user interface (GUI).

