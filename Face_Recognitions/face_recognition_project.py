import face_recognition
import cv2
import os
import numpy as np

# Load images and names from the 'images' folder
def load_images_from_folder(folder_path):
    known_face_encodings = []
    known_face_names = []

    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)
        name, ext = os.path.splitext(file_name)

        # Check if the file is an image
        if ext.lower() in ['.jpg', '.jpeg', '.png']:
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:  # If face encodings are found
                known_face_encodings.append(encodings[0])
                known_face_names.append(name)

    return known_face_encodings, known_face_names

# Recognize faces in a live camera feed
def recognize_faces(known_face_encodings, known_face_names, video_source=0):
    capture = cv2.VideoCapture(video_source)

    if not capture.isOpened():
        print("Error: Cannot open camera or video")
        return

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare the face with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance if match is found
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                 # Draw a rectangle around the face and display the name
                top, right, bottom, left = [v * 4 for v in face_location]  # Scale back to original size
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                name="unknown"
                 # Draw a rectangle around the face and display the name
                top, right, bottom, left = [v * 4 for v in face_location]  # Scale back to original size
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 20, 0), 2)

            
            

        # Display the resulting frame
        cv2.imshow('Face Recognition', frame)

        # Break the loop on pressing ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    capture.release()
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    images_folder = "images"
    known_face_encodings, known_face_names = load_images_from_folder(images_folder)
    recognize_faces(known_face_encodings, known_face_names)
