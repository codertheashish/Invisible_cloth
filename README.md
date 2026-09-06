# 🧥 Invisible Cloth

A real-time **Invisible Cloak effect** built using Python and OpenCV.
This project detects a specific cloth color (teal/blue) and replaces it with the background, creating a Harry Potter-style invisibility illusion.

---

## 🚀 Features

✅ Real-time webcam processing<br>
🎯 Detects teal/blue cloak color accurately<br>
🧼 Mask cleaning to remove noise & halos<br>
🪄 Smooth invisibility effect<br>
💻 Beginner-friendly OpenCV project<br>

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
https://github.com/codertheashish/Invisible_cloth.git
```

---

## ▶️ How to Use

### Step 1: Capture Background

* Place camera in a fixed position.
* Capture an empty background image and save it as:

```
image.jpeg
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

✔ Real-time invisibility effect<br>
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

- GitHub:
[codertheashish](https://github.com/codertheashish)
- Linkedin :
[codertheashish](https://www.linkedin.com/in/codertheashish/)
- Instagram :
[codertheashish](https://www.instagram.com/codertheashish/)

---
<img width="601" height="350" alt="Invisible_cloak" src="https://github.com/user-attachments/assets/6414a138-8f32-4ef6-85d8-4113e925042c" />
