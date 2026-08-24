from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects
    results = model(frame)

    for result in results:

        for box in result.boxes:

            # Class number
            cls = int(box.cls[0])

            # 0 = person in COCO dataset
            if cls == 0:

                # Get bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                width = x2 - x1
                height = y2 - y1

                # Avoid division by zero
                if height != 0:

                    ratio = width / height

                    # Simple fall detection
                    if ratio > 1.2:
                        label = "FALL DETECTED"
                    else:
                        label = "NORMAL"

                    # Draw bounding box
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    # Display result
                    cv2.putText(
                        frame,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )

    # Display video
    cv2.imshow("Real-Time Fall Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()