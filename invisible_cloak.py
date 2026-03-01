import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread("image.jpg")

if background is None:
    print("Background not found!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ✅ tuned teal range (white ignore)
    lower_teal = np.array([75, 80, 60])
    upper_teal = np.array([110, 255, 255])

    mask = cv2.inRange(hsv, lower_teal, upper_teal)

    # mask cleaning
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.medianBlur(mask, 5)

    mask_inv = cv2.bitwise_not(mask)

    cloak = cv2.bitwise_and(background, background, mask=mask)
    normal = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # ✅ no halo edges
    final = cloak + normal

    cv2.imshow("Invisible Cloak FINAL", final)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()