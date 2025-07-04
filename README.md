# 🤖 Web-Controlled Robotic Arm Interface

A lightweight and interactive *Flask web application* that allows users to control a 4-DOF (Degree of Freedom) robotic arm in real-time using sliders via serial communication with an *Arduino*. Perfect for prototyping, demos, and educational robotics projects!

---

## 🚀 Features

- 🌐 Intuitive Web UI with smooth slider controls
- 🔄 Real-time serial communication with Arduino
- ⚙ Controls 4 servos (Base, Shoulder, Elbow, Gripper)
- 💡 Minimal setup, beginner-friendly codebase

---

📸 Screenshots
Web UI
![WhatsApp Image 2025-06-30 at 14 31 40_013c070b](https://github.com/user-attachments/assets/31aac451-2a44-46d2-a25e-175d163e8f08)



## 🧰 Tech Stack

| Frontend        | Backend        | Hardware         |
|-----------------|----------------|------------------|
| HTML, CSS       | Flask (Python) | Arduino + Servos |

---

## 📁 Project Structure

web_app/
├── app.py             # Flask backend - handles web requests and sends data to Arduino via serial
├── templates/
│   └── index.html     # Web UI - contains sliders for controlling servo angles
└── static/            # (Optional) - for static assets like CSS files or images


## 🛠 Setup Instructions

### ✅ Prerequisites

- Python 3.x
- Flask (pip install flask)
- Arduino with 4 connected servos
- pyserial library (pip install pyserial)

### 📦 Clone the Repository

git clone https://github.com/your-username/robotic-arm-web-controller.git
cd robotic-arm-web-controller
🔌 Connect Your Arduino
Upload an Arduino sketch to read 4 servo angles via Serial input (e.g., 90 45 120 60\n)

Connect servos to correct pins and power them externally if needed.

▶ Run the App
python app.py
Access the UI at http://localhost:5000 in your browser.

🧪 Arduino Code

```bash
#include <Servo.h>

Servo s1, s2, s3, s4;

void setup() {
  Serial.begin(9600);
  s1.attach(10); s2.attach(9); s3.attach(2); s4.attach(13);
}

void loop() {
  if (Serial.available()) {
    int a1 = Serial.parseInt();
    int a2 = Serial.parseInt();
    int a3 = Serial.parseInt();
    int a4 = Serial.parseInt();

    if (Serial.read() == '\n') {
      s1.write(a1);
      s2.write(a2);
      s3.write(a3);
      s4.write(a4);
    }
  }
}
