import torch
from ultralytics import YOLO

# Check if GPU is available
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the model
model = YOLO("./models/best.pt")

# Perform inference on the video using GPU if available
results = model.predict('./input_videos/input_video.mp4', save=True, device=device)

# Print the first result
print(results[0])

# Iterate through the boxes and print each one
for box in results[0].boxes:
    print(box)
