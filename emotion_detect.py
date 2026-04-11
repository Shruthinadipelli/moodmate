import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model('model/emotion_model.h5')

# Emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def detect_emotion():
    cap = cv2.VideoCapture(0)

    detected_emotion = "No face detected"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]

                # Resize to match model
                face = cv2.resize(face, (48, 48))

                # Convert to RGB (MobileNet expects 3 channels)
                face = cv2.cvtColor(face, cv2.COLOR_GRAY2RGB)

                # Normalize
                face = face / 255.0

                # Reshape
                face = np.reshape(face, (1, 48, 48, 3))

                # Predict
                prediction = model.predict(face, verbose=0)
                confidence = np.max(prediction)

                if confidence < 0.5:
                    detected_emotion = "Not sure"
                else:
                    detected_emotion = emotion_labels[np.argmax(prediction)]

                # Draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Put text
                cv2.putText(frame, detected_emotion, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        else:
            detected_emotion = "No face detected"

        # Show webcam
        cv2.imshow("Emotion Detection", frame)

        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return detected_emotion