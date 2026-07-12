# 🌸 Virtual Flower Bloom & Growth Control using Computer Vision

A fun and interactive Computer Vision project that allows users to control a virtual flower using hand gestures. The project uses **Python, OpenCV, and MediaPipe** to detect hand movements in real-time and manipulate the flower based on pinch gestures.

With just your hands, you can make the flower grow bigger or bloom naturally — no keyboard or mouse required! ✨

---

## 🚀 Features

- 🌱 Real-time hand tracking using MediaPipe
- ✋ Left-hand pinch gesture controls flower growth
- 🌸 Right-hand pinch gesture controls flower blooming
- 🎥 Live webcam-based interaction
- 🖥️ Real-time OpenCV visualization
- 🎮 Touchless human-computer interaction

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV** - Image processing and webcam handling
- **MediaPipe** - Hand detection and landmark tracking
- **NumPy** - Mathematical calculations and coordinate handling

---

## 🧠 How It Works

The project uses MediaPipe's Hand Tracking module to detect hand landmarks from the webcam feed.

The distance between specific finger landmarks is calculated to identify a pinch gesture.

### 🌱 Left Hand Gesture
- When the user performs a pinch gesture with the **left hand**:
  - The flower stem grows
  - The flower size increases

### 🌸 Right Hand Gesture
- When the user performs a pinch gesture with the **right hand**:
  - The flower starts blooming
  - Petals expand gradually

The gestures are mapped into real-time changes in the virtual flower animation.

---

## 📂 Project Structure

GestureBloom/
│
├── main.py              # Main execution file
├── flower.py            # Flower growth and bloom logic
├── assets/
│   └── flower.png       # Flower image resources
│
├── requirements.txt     # Dependencies
└── README.md            # Documentation

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/dexterrrrrrrrrrrrrrrrrrrrr/GestureBloom.git
```
Navigate to the project folder
```
cd GestureBloom
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python main.py
