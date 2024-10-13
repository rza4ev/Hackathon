import cv2
import torch
from geopy.distance import geodesic
from shapely.geometry import Point, Polygon

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Open video source (file or camera)
cap = cv2.VideoCapture('park_area_video.mp4')

# Define GIS data (parking zones as polygons)
park_zones = [
    Polygon([(40.4093, 49.8671), (40.4095, 49.8675), (40.4091, 49.8677), (40.4089, 49.8673)]),  # example coordinates
    # Add more park zones here
]

# Process video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Object detection using YOLO
    results = model(frame)
    
    # Analyze detected objects
    for result in results.xyxy[0]:
        x1, y1, x2, y2, conf, class_id = result
        label = model.names[int(class_id)]  # Object label
        
        if label == 'car' or label == 'parking space':  # Check for cars or parking spots
            # Example of detected location (e.g., from GPS data)
            detected_location = Point(40.4094, 49.8673)
            
            # Check if detected object is inside a parking zone
            for park_zone in park_zones:
                if park_zone.contains(detected_location):
                    print(f"Detected within parking zone: {detected_location}")
                else:
                    print("Outside parking zone")

    # Draw detections on the video frame
    for det in results.xyxy[0]:
        x1, y1, x2, y2, conf, class_id = det
        label = f"{model.names[int(class_id)]} {conf:.2f}"
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    
    # Display processed video frame
    cv2.imshow('Park Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
