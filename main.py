import cv2
import mediapipe as mp
import math

from flower import Flower

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

flower = Flower()

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        left_distance = None
        right_distance = None

        if results.multi_hand_landmarks and results.multi_handedness:

            for hand_landmarks, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness
            ):

                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                label = handedness.classification[0].label

                thumb = hand_landmarks.landmark[4]
                index = hand_landmarks.landmark[8]

                h, w, _ = frame.shape

                tx = int(thumb.x * w)
                ty = int(thumb.y * h)

                ix = int(index.x * w)
                iy = int(index.y * h)

                distance = math.hypot(tx - ix, ty - iy)

                # Draw pinch points
                cv2.circle(frame, (tx, ty), 8, (0, 255, 255), -1)
                cv2.circle(frame, (ix, iy), 8, (0, 255, 255), -1)
                cv2.line(frame, (tx, ty), (ix, iy), (255, 255, 255), 2)

                # Left hand controls stem growth
                if label == "Left":
                    left_distance = distance

                # Right hand controls bloom
                elif label == "Right":
                    right_distance = distance

        flower.update(left_distance, right_distance)

        flower.draw(frame)

        cv2.putText(
            frame,
            "GestureBloom",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Left Hand = Grow Stem",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Right Hand = Bloom Flower",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "S = Save | R = Reset | ESC = Exit",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.imshow("GestureBloom", frame)

        key = cv2.waitKey(1)

        if key == ord("s"):
            cv2.imwrite("my_tulip.png", frame)
            print("Artwork Saved as my_tulip.png")

        elif key == ord("r"):
            flower.reset()
            print("Flower Reset")

        elif key == 27:  # ESC
            break

cap.release()
cv2.destroyAllWindows()