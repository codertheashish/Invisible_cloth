# Invisible_cloth
Real-time Invisible Cloak effect using Python and OpenCV that replaces a colored cloth with the background to create a seamless invisibility illusion. Beginner-friendly computer vision project demonstrating color detection, masking, and real-time video processing.

# 🧥 Invisible Cloak (Python + OpenCV)

A real-time **Invisible Cloak effect** built using Python and OpenCV.
This project detects a specific cloth color (teal/blue) and replaces it with the background, creating a Harry Potter-style invisibility illusion.

---

## 📷 Invisible Cloak Effect

This tool uses your webcam to detect a colored cloth and replaces that region with a pre-captured background image.

---

## 🚀 Features

✅ Real-time webcam processing
🎯 Detects teal/blue cloak color accurately
🧼 Mask cleaning to remove noise & halos
🪄 Smooth invisibility effect
💻 Beginner-friendly OpenCV project

---

## 🛠 Tech Stack

* Python 3.x
* OpenCV (`cv2`)
* NumPy

---

## 📦 Installation

### 1️⃣ Install dependencies

```bash
pip install opencv-python numpy
```

### 2️⃣ Download the project

Clone your repository:

```bash
https://github.com/codertheashish/Invisible_cloth
```

---

## ▶️ How to Use

### Step 1: Capture Background

* Place camera in a fixed position.
* Capture an empty background image and save it as:

```
image.jpg
```

### Step 2: Run the Script

```bash
python invisible_cloak.py
```

### Step 3: Use the Cloak

* Wear a teal/blue cloth.
* Stand in front of the camera.
* The cloth area becomes invisible 🎩✨

Press **Q** to quit.

---

## 📁 Output

✔ Real-time invisibility effect
✔ Background replaces cloak area

---

## ⚙️ How It Works

1. Captures webcam frames.
2. Converts frame to HSV color space.
3. Detects cloak color using range masking.
4. Cleans mask using morphology & blur.
5. Replaces cloak area with background image.

---

## 📌 Notes

* Camera must remain stable.
* Background image should match camera view.
* Avoid similar colors in surroundings.

---

## 👨‍💻 Author

**Ashish Kumar Prajapati**

---
