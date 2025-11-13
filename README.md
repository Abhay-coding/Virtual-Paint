<h1 align="center">🎨 Virtual Paint using OpenCV</h1>

<p align="center">
  <b>A real-time virtual painting app built with <a href="https://opencv.org/">OpenCV</a> and <a href="https://www.python.org/">Python</a>.</b><br>
  Draw in the air using colored objects tracked via your webcam!
</p>

---

## 🌈 Features

✅ **Real-time object tracking**  
🎨 **Color detection using HSV values**  
🧠 **Contour-based color identification**  
✏️ **Draw virtual trails like a digital pen**  
⚙️ **Adjustable color ranges using HSV color picker**

---

## 🧰 Tech Stack

| Component | Details |
|------------|----------|
| 💻 Language | Python 3.x |
| 🧩 Libraries | `OpenCV`, `NumPy` |

---

## ⚙️ How It Works

1. Webcam captures each frame.  
2. Image is converted to **HSV color space**.  
3. The program isolates specific colors using HSV thresholds.  
4. Contours are detected to track object position.  
5. A trail is drawn based on movement of that color.

---

## 🪄 Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone git@github.com:Abhay-coding/Virtual-Paint.git
cd Virtual-Paint


### 1️⃣ Clone this repository
```bash
git clone git@github.com:Abhay-coding/Virtual-Paint.git
cd Virtual-Paint
