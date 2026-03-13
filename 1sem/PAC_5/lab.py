import time
import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

detect_motion = True
last_switch_time = time.time()
switch_interval = 0

_, prev = cap.read()

prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if time.time() - last_switch_time > switch_interval:
        detect_motion = not detect_motion
        last_switch_time = time.time()

    result = np.zeros_like(frame)

    if detect_motion:
        flow = cv2.calcOpticalFlowFarneback(
            prev_gray, gray, None,
            0.5, 3, 15, 3, 5, 1.2, 0
        )
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        motion_mask = mag > 1

        result[motion_mask] = [0, 0, 255]
        result[~motion_mask] = [0, 255, 0]

        text = "Red" if np.any(motion_mask) else "Green"

    else:
        result[:, :] = [0, 255, 0]
        text = "Green"

    cv2.putText(result, text, (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    combined = np.hstack((
        cv2.resize(frame, None, fx=0.6, fy=0.6),
        cv2.resize(result, None, fx=0.6, fy=0.6)
    ))

    cv2.imshow("result", combined)

    prev_gray = gray.copy()

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
