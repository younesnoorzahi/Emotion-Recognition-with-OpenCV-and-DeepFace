import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

how_many_time = []
sad = 0
happy = 0
angry = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']
        cv2.putText(frame, f"Emotion: {emotion}", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if emotion == 'sad':
            sad = sad + 1
        elif emotion == 'happy': 
            happy = happy + 1  
        elif emotion == 'angry': 
            angry = angry + 1      
    except:
        pass

    cv2.imshow("Emotion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f'angry => {angry}')
print(f'happy => {happy}')
print(f'sad => {sad}')
