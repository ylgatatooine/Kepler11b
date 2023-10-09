📸🙂😢😕😲 Imagine if your webcam could tell you whether you look happy, sad, confused, or surprised! 

Over the weekend, I embarked on a journey into the world of face recognition and emotion detection using OpenCV (Open Computer Vision Library), along with PyTorch or TensorFlow. It was a fun experience to dive into these technologies and quickly put together a program that both surprised and entertained me. 🤯

Here are a few key takeaways from my weekend hacking:

1. OpenCV works seamlessly with webcams, especially when focusing on a single person in the frame. The accuracy of the results is impressive.

2. When it comes to checking multiple faces in a single picture, the accuracy and success rate don't always align perfectly. When the success rate is high, there are false positives. It's a reminder of the complex nature of facial recognition.

3. Emotion, age, and gender detection, while entertaining, are still a work in progress. Even when I'm visibly happy, AI often identifies a wide range of emotions from happy to sad, with varying age and gender estimations.

4. The potential applications of face recognition are many. However, privacy, security, and accuracy have to be addressed properly first. Useful applications are surfacing. E.g. AI automatically identifies marathon runners in real-time during a live event, then tags marathon runners on event photos for them to purchase. It is just one example. 

The image is a screen capture of webcam feed capture. Some AI module has higher accuracy in telling my emotion than telling my gender. LOL. 

Have you ever experimented with face recognition or computer vision technologies? Share your thoughts and experiences in the comments below! 👇 #ComputerVision #OpenCV #FaceRecognition #EmotionDetection #AI #TechExploration #Innovation

``` Python

import sys
path_to_module = "/Users/lianggangyu/miniconda/lib/python3.11/site-packages"
sys.path.append(path_to_module)

import cv2

emotions = ["afraid", "angry", "disgusted", "happy",  "neutral", "sad", "surprised"]

facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# resize the image to 350x350 pixels
def resize_face(face):  
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(face, (350, 350))
    return face

stream = cv2.VideoCapture(0)

while(True):
    
    try: 
        # Capture webcam frame-by-frame
        (grabbed, frame) = stream.read()

        # Identify faces in the frame
        faces = facecascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=6)

        # Guessing the gender of the face, using a classifier from Facilier 
        gender_recognizer = cv2.face.FisherFaceRecognizer_create()
        gender_recognizer.read('./src/models/gender_classifier_model.xml')

        # Reading the emotion on the face, using a classifier from Facilier 
        emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
        emotion_recognizer.read('./src/models/emotion_classifier_model.xml')

        # Identify the largest face
        face = max(faces,key=lambda item:item[2]*item[3])    

        (x, y, w, h) = face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_face = frame[y:y+h, x:x+w]

        # Guess emotion 
        predicted_emotion = emotion_recognizer.predict(resize_face(roi_face))
        emotion = emotions[predicted_emotion[0]]
        text = emotion

        # Read gender
        predicted_gender = gender_recognizer.predict(resize_face(roi_face))  
        gender = "male" if predicted_gender[0] == 1 else "female"
        text += " " + gender

        # display the emotion and gender
        cv2.putText(image, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

        # Show the image
        cv2.imshow("Image", frame)
            
    except ValueError:
        print("Oops! No face found. Try again...")

# Cleanup
stream.release()

```
