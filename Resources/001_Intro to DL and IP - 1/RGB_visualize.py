import cv2
import numpy as np
import pyautogui

def main():
    cap = cv2.VideoCapture(0)  # 0 for default webcam
    
    
    # # Set optional capture resolution (optional)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Split the image into B, G, and R channels
        b, g, r = cv2.split(frame)

        # Create a larger image to hold all channels horizontally
        height, width, _ = frame.shape
        print("Frame shape:", frame.shape)
        print("B channel shape:", b.shape)
        print("G channel shape:", g.shape)
        print("R channel shape:", r.shape)
        print("Combined image shape:", (height, width * 3, 3))
        combined_image = np.zeros((height, width * 3, 3), dtype=np.uint8)

        # Place the channels horizontally
        combined_image[:, :width] = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])
        combined_image[:, width:2*width] = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])
        combined_image[:, 2*width:] = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])
        
        # Dynamically resize to fit screen width while preserving aspect ratio
        screen_width, screen_height = pyautogui.size()
        scale_w = screen_width / combined_image.shape[1]
        scale_h = screen_height / combined_image.shape[0]
        scale = min(scale_w, scale_h)

        new_width = int(combined_image.shape[1] * scale)
        new_height = int(combined_image.shape[0] * scale)

        resized_combined = cv2.resize(combined_image, (new_width, new_height))
        
        cv2.imshow("Combined Frame (B | G | R)", resized_combined)
        
        # Display the combined image
        # cv2.imshow("Combined Frame (B | G | R)", combined_image)
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()