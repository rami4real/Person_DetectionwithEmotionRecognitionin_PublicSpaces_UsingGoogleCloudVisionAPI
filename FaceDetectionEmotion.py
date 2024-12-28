def face_emotion_detection(image, filename, output_folder, face_confidence_threshold=0.4):
    os.makedirs(output_folder, exist_ok=True)
    mtcnn = MTCNN(keep_all=True, device="cpu")
    boxes, confidences = mtcnn.detect(image)
    if boxes is not None and confidences is not None:
        for i, (box, confidence) in enumerate(zip(boxes, confidences)):
            if confidence > face_confidence_threshold:
                x1, y1, x2, y2 = box.astype(int)
                face = image[y1:y2, x1:x2]
                if face is not None and face.size > 0:
                    result = DeepFace.analyze(face, actions=["emotion"], enforce_detection=False)
                    if isinstance(result, list):
                        result = result[0]  # Get the first element if it's a list
                    emotion = result.get("dominant_emotion", "unknown")  
                    output_filename = f"{filename.split('.')[0]}_face_{i}_{emotion}.jpg"
                    output_path = os.path.join(output_folder, output_filename)
                    cv2.imwrite(output_path, face)  # Save the cropped face
                    print(f"Face saved with emotion: {output_path}")
    else:
        print(f"No faces detected in {filename}.")
input_folder = "outputcameratest" 
output_folder = "faces5"  
model = YOLO("yolov8n.pt")
yolo_confidence_threshold = 0.7  
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    results = model(image_path)
    image = cv2.imread(image_path)
    if results:
        for result in results:
            for detection in result.boxes:
                if detection.cls == 0 and detection.conf >= yolo_confidence_threshold:
                    xmin, ymin, xmax, ymax = detection.xyxy[0]

                    person_crop = image[int(ymin):int(ymax), int(xmin):int(xmax)]
                    face_emotion_detection(person_crop, image_file, output_folder, face_confidence_threshold=0)
