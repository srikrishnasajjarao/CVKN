import cv2
import numpy as np

def classify_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    
    # Define threshold for day vs. night
    if brightness > 75:
        return "day"  # Bright frames = day
    else:
        return "night"  # Dark frames = night

def analyze_video(video_path):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None

    # Get total frame count and FPS
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps  # Duration in seconds
    print(f"Total frames: {total_frames}")
    print(f"FPS: {fps}")
    print(f"Duration: {duration:.2f} seconds")
    
    # Count frames in each category
    day_count = 0
    night_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Classify frame
        category = classify_frame(frame)
        if category == "day":
            day_count += 1
        else:
            night_count += 1
    
    # Print frame counts
    print(f"Day frames: {day_count}")
    print(f"Night frames: {night_count}")

    cap.release()

    # Calculate percentages
    total = day_count + night_count
    day_percent = (day_count / total) * 100 if total > 0 else 0
    night_percent = (night_count / total) * 100 if total > 0 else 0

    return {
        "day": day_percent,
        "night": night_percent
    }

# Example usage
video_path = "Data/sunset.mp4" 
result = analyze_video(video_path)
if result:
    print("Output:")
    print(f"Day: {result['day']:.2f}%")
    print(f"Night: {result['night']:.2f}%")