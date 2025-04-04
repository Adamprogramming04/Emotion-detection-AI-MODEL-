import cv2
from deepface import DeepFace
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to grayscale for better face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    try:
        # Analyze emotions
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        
        # Extract dominant emotion
        dominant_emotion = analysis[0]['dominant_emotion']
        
        # Display emotion on frame
        cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Provide audio feedback
        if dominant_emotion == "happy":
            speak("You look happy! Keep smiling!")
        elif dominant_emotion == "sad":
            speak("You look sad. Hope things get better soon!")
        elif dominant_emotion == "angry":
            speak("You look angry. Maybe take it easy?")
        
    except Exception as e:
        print("No face detected or error:", e)
    
    # Show video feed
    cv2.imshow("Emotion Detection", frame)
    
    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
