mtcnn = MTCNN(keep_all=True, device='cuda' if torch.cuda.is_available() else 'cpu')
resnet = InceptionResnetV1(pretrained='vggface2').eval()
def get_face_embeddings_and_crops(image):
    try:
        faces, probs = mtcnn(image, return_prob=True)
    except RuntimeError as e:
        print(f"RuntimeError during face detection: {e}")
        return None, None
    if faces is not None and len(faces) > 0:
        embeddings = resnet(faces)
        return embeddings, faces
    return None, None
def face_matches(embedding1, embedding2, threshold=0.95):
    distance = (embedding1 - embedding2).norm().item()
    return distance < threshold
input_folder = "faces4"
output_folder = "ff2"
os.makedirs(output_folder, exist_ok=True)
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
face_encodings = {}
unique_faces = 0
for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    embeddings, face_crops = get_face_embeddings_and_crops(image_rgb)
    if embeddings is not None and face_crops is not None:
        for embedding, face_crop in zip(embeddings, face_crops):
            match_found = False
            for known_file, known_embedding in face_encodings.items():
                if face_matches(known_embedding, embedding):
                    match_found = True
                    break
            if not match_found:
                face_encodings[image_file] = embedding
                unique_faces += 1
                out_image_path = os.path.join(output_folder, image_file)
                shutil.copy(image_path, out_image_path)
print(f"Total number of unique faces detected: {unique_faces}")
