import face_recognition
import cv2

# This is a demo of running face recognition on a video file and saving the results to a new video file.


# Open the input movie file
input_video = cv2.VideoCapture("corrie_street.mp4")
length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
codec = int(input_video.get(cv2.CAP_PROP_FOURCC))
fps = int(input_video.get(cv2.CAP_PROP_FPS))
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
output_video = cv2.VideoWriter('output.mp4', codec, fps, (frame_width,frame_height))

# Load some sample pictures and learn how to recognize them.
emma = face_recognition.load_image_file("emma.jpeg")
emma = face_recognition.face_encodings(emma)[0]

liz = face_recognition.load_image_file("liz.JPG")
liz = face_recognition.face_encodings(liz)[0]

cathy = face_recognition.load_image_file("Cathy.JPG")
cathy = face_recognition.face_encodings(cathy)[0]

male_image = face_recognition.load_image_file("steve.jpg")
male_face_encoding = face_recognition.face_encodings(male_image)[0]

known_faces = [
    emma,
    liz,
    cathy,
    male_face_encoding
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []

frame_number = 0
counts = [0,0,0,0]
print 
while True:
    # Grab a single frame of video
    ret, frame = input_video.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "emma"
            frameNo = counts[0]
            counts[0] = counts[0] + 1
            text = name + ": " + str(frameNo)

        elif match[1]:
            name = "liz"
            frameNo = counts[1]
            counts[1] = counts[1] + 1
            text = name + ": " + str(frameNo)

        elif match[2]:
            name = "cathy"
            frameNo = counts[2]
            counts[2] = counts[2] + 1
            text = name + ": " + str(frameNo)

        elif match[3]:
            name = "steve"
            frameNo = counts[3]
            counts[3] = counts[3] + 1
            text = name + ": " + str(frameNo)
        

        face_names.append(name)

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, text, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_video.write(frame)

# All done!
output_video.release()
input_video.release()
cv2.destroyAllWindows()