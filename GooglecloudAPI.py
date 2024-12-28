os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "token.json"
client = vision.ImageAnnotatorClient()
input_folder = "outputcameratest"  
output_folder = "faces3"  emotions
os.makedirs(output_folder, exist_ok=True)
person_confidence_threshold = 0.75  
face_confidence_threshold = 0.95  
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    image = cv2.imread(image_path)
    image_content = cv2.imencode('.jpg', image)[1].tobytes()
    gcv_image = vision.Image(content=image_content)
    response = client.object_localization(image=gcv_image)
    localized_objects = response.localized_object_annotations
    i = 0
    for obj in localized_objects:
        if obj.name == "Person" and obj.score >= person_confidence_threshold:
            vertices = obj.bounding_poly.normalized_vertices
            xmin = int(vertices[0].x * image.shape[1])
            ymin = int(vertices[0].y * image.shape[0])
            xmax = int(vertices[2].x * image.shape[1])
            ymax = int(vertices[2].y * image.shape[0])
            i += 1
            person_crop = image[ymin:ymax, xmin:xmax]
            person_content = cv2.imencode('.jpg', person_crop)[1].tobytes()
            person_gcv_image = vision.Image(content=person_content)
            face_response = client.face_detection(image=person_gcv_image)
            if face_response.face_annotations:
                for face_annotation in face_response.face_annotations:
                    face_confidence = face_annotation.detection_confidence
                    if face_confidence >= face_confidence_threshold:
                        emotions = {
                            "joy": face_annotation.joy_likelihood,
                            "sorrow": face_annotation.sorrow_likelihood,
                            "anger": face_annotation.anger_likelihood,
                            "surprise": face_annotation.surprise_likelihood,
                        }
                        dominant_emotion = max(emotions, key=emotions.get)
                        output_file_name = f"{i}_{image_file[:-4]}_{dominant_emotion}.jpg"
                        output_path = os.path.join(output_folder, output_file_name)
                        cv2.imwrite(output_path, person_crop)
