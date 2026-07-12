import cv2
import numpy as np
import math


class Flower:

    def __init__(self):

        self.stem_height = 100
        self.bloom = 40

        self.tulip = cv2.imread(
            "assets/tulip.png",
            cv2.IMREAD_UNCHANGED
        )

        if self.tulip is None:
            raise Exception(
                "Cannot find assets/tulip.png"
            )

    def reset(self):

        self.stem_height = 100
        self.bloom = 40

    def update(self, left_distance, right_distance):

        if left_distance is not None:

            self.stem_height = int(
                np.interp(
                    left_distance,
                    [10, 220],
                    [80, 500]
                )
            )

        if right_distance is not None:

            self.bloom = int(
                np.interp(
                    right_distance,
                    [10, 220],
                    [30, 140]
                )
            )

    def overlay_png(
        self,
        background,
        overlay,
        x,
        y
    ):

        if overlay.shape[2] < 4:
            return

        h, w = overlay.shape[:2]

        if x < 0 or y < 0:
            return

        if x + w > background.shape[1]:
            return

        if y + h > background.shape[0]:
            return

        alpha = overlay[:, :, 3] / 255.0

        for c in range(3):

            background[
                y:y+h,
                x:x+w,
                c
            ] = (
                alpha * overlay[:, :, c]
                +
                (1 - alpha)
                * background[
                    y:y+h,
                    x:x+w,
                    c
                ]
            )

    def draw(self, frame):

        h, w, _ = frame.shape

        center_x = w // 2
        center_y = h - 80

        sway = int(
            15 * math.sin(
                cv2.getTickCount()
                /
                cv2.getTickFrequency()
            )
        )

        flower_x = center_x + sway
        flower_y = center_y - self.stem_height

        # Stem
        cv2.line(
            frame,
            (center_x, center_y),
            (flower_x, flower_y),
            (0, 180, 0),
            10
        )

        # Leaves

        leaf_y = center_y - self.stem_height // 2

        cv2.ellipse(
            frame,
            (center_x - 40, leaf_y),
            (20, 60),
            -45,
            0,
            360,
            (0, 180, 0),
            -1
        )

        cv2.ellipse(
            frame,
            (center_x + 40, leaf_y),
            (20, 60),
            45,
            0,
            360,
            (0, 180, 0),
            -1
        )

        scale = self.bloom / 70

        tulip = cv2.resize(
            self.tulip,
            None,
            fx=scale,
            fy=scale
        )

        fh, fw = tulip.shape[:2]

        # Create bouquet

        offsets = [

            (-120, 20),
            (-80, -20),
            (-40, 10),

            (0, 0),

            (40, 10),
            (80, -20),
            (120, 20),

            (-60, -60),
            (60, -60)

        ]

        for ox, oy in offsets:

            tx = flower_x + ox
            ty = flower_y + oy

            glow = cv2.GaussianBlur(
                tulip,
                (31, 31),
                0
            )

            self.overlay_png(
                frame,
                glow,
                tx - fw // 2,
                ty - fh // 2
            )

            self.overlay_png(
                frame,
                tulip,
                tx - fw // 2,
                ty - fh // 2
            )

        # Sparkles

        for _ in range(15):

            px = np.random.randint(
                flower_x - 180,
                flower_x + 180
            )

            py = np.random.randint(
                flower_y - 180,
                flower_y + 50
            )

            cv2.circle(
                frame,
                (px, py),
                np.random.randint(1, 4),
                (255, 255, 255),
                -1
            )