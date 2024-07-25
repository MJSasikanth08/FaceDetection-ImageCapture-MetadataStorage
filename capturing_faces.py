import cv2
import os
from datetime import datetime
import mysql.connector
from PIL import Image

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sasikanth!@#@123",
    database="metadata"
)
cursor = db.cursor()

# Initialize OpenCV's face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces, save them, and read metadata
def detect_faces_and_save(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    captures = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in captures:
        face = frame[y:y+h, x:x+w]
        # Save face image
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        face_filename = f"face_{timestamp}.jpg"
        cv2.imwrite(face_filename, face)
        # Read metadata
        metadata = extract_metadata(face_filename)
        # Store metadata in MySQL
        cursor.execute("INSERT INTO captures (filename, metadata) VALUES (%s, %s)", (face_filename, str(metadata)))
        db.commit()

# Function to extract metadata using Pillow
def extract_metadata(image_path):
    with Image.open(image_path) as img:
        metadata = {
            "format": img.format,
            "mode": img.mode,
            "size": img.size,
            "exif": img.info.get("exif", None)
        }
        return metadata

# Main function to capture frames from webcam
def capture_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        detect_faces_and_save(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_frames()
