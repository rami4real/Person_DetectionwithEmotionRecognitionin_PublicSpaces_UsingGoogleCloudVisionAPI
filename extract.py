def extract_frames_from_camera(output_folder, frame_rate=1, x=0, y=0, w=100, h=100, camera_source=0):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    while True:
        cap = cv2.VideoCapture(camera_source)
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Error: Could not retrieve frame from source.")
            break
        height, width, _ = frame.shape  
        if x + w > width or y + h > height:
            print(f"Invalid ROI: {x=}, {y=}, {w=}, {h=}. Frame size: {width}x{height}")
            return
        cropped_frame = frame[y:y + h, x:x + w] 
        if cropped_frame.size == 0:
            print("Error: Cropped frame is empty.")
            return
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_filename = os.path.join(output_folder, f"frame_{current_time}.jpeg")
        cv2.imwrite(output_filename, cropped_frame)
        print(f"Saved {output_filename}")
        cap.release()
    print("Finished extracting frames.") 
output_folder = 'camera_frames'
camera_url = 'rtsp:'
extract_frames_from_camera(output_folder, frame_rate=1, x=100, y=0, w=1100, h=1080, camera_source=camera_url)
