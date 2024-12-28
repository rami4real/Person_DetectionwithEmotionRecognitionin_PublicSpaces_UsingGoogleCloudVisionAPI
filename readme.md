# Détection de Personne, avec reconnaissance d’émotion dans un espace   
Publique en explorant Google Cloud Vision API
en english

## Overview
This project leverages the Google Vision API and custom image processing algorithms to detect faces and emotions in images captured by a security camera. The system processes and analyzes the data to provide interpretable results, such as the count of unique individuals and their emotional states.

![System Architecture](media/ConceptionArchitecture.png)

## Our Solution
Our solution involves:
- Capturing images from a security camera.
- Extracting frames to detect individuals and faces.
- Analyzing faces for emotion detection and saving the data.
- Counting unique individuals across frames to provide insights on activity and emotional states.

![Solution Design](media/ConceptionSolution.png)

---

## Software Environment

### Development Tools
- **Anaconda**: Manages Python environments and simplifies package installation.
- **Jupyter Notebook**: Facilitates interactive code development and documentation.

### Technologies Used
- **Python**: Main programming language for implementation.
- **OpenCV (cv2)**: Processes images and handles computer vision operations.
- **Ultralytics YOLO**: Performs real-time object detection.
- **MTCNN**: Detects faces in images.
- **FaceNetPyTorch**: Extracts facial features for identification.
- **DeepFace**: Analyzes emotions and validates facial uniqueness.
- **Google Vision API**: Handles object recognition, face detection, and OCR.
- Other libraries like **numpy** and **shutil** for numerical operations and file handling.

---

## Development Details

### System Integration
During development, we integrated various components:
1. Connected to a surveillance camera to capture real-time video streams.
2. Extracted image frames and stored them for analysis.
3. Used detection algorithms to identify individuals and analyze their emotions.
4. Implemented a unique counter for tracking distinct individuals.

### Key Processes
#### 1. Frame Extraction from Camera
The script captures and crops images from a specified camera region of interest (ROI), ensuring valid and non-empty cropped images before saving them.

**File:** `extract.py`

#### 2. Using Google Cloud Vision API
Processes images to detect individuals and their emotions, saving results with filenames based on dominant emotions.

**File:** `GoocglecloudAPI.py`

#### 3. Emotion Detection and Person Counting
- **Face Detection and Emotion Analysis:** YOLO and MTCNN detect faces, while DeepFace analyzes emotions.
  - **File:** `FaceDetectionemotion.py`

- **Unique Person Counting:** MTCNN and InceptionResnetV1 detect faces and generate embeddings for identifying unique individuals.
  - **File:** `estmatinguniquepeoplecount.py`

---

## Testing and Validation
Our solution demonstrated better performance than Google Vision API in specific tests, indicating robustness under various conditions.

![Test Results](media/Tests.png)

---

## File Structure
- `media/ConceptionArchitecture.png`: System architecture diagram.
- `media/ConceptionSolution.png`: Solution design illustration.
- `media/Tests.png`: Test and validation results.
- `extract.py`: Script for extracting frames from the camera.
- `GoocglecloudAPI.py`: Script utilizing Google Cloud Vision API.
- `FaceDetectionemotion.py`: Script for face detection and emotion analysis.
- `estmatinguniquepeoplecount.py`: Script for counting unique individuals.

---

## Future Work
- Optimize algorithms for faster processing.
- Enhance detection accuracy under varying lighting and environmental conditions.
- Integrate real-time monitoring and alert systems.

---

## Contact
For further information, feel free to reach out to the project team.
