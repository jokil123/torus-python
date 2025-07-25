from __future__ import annotations
from abc import ABC, abstractmethod
import os
import sys
import time

from torus_lib.vector import Vector3

import sys
import time


def clear_last_lines(n, m):
    """
    Clears the last n to m lines of the terminal.

    Args:
      n: The starting line number from the bottom (1 is the last line).
      m: The ending line number from the bottom.
    """
    if n <= 0 or m < n:
        return

    # Move the cursor up to the starting line
    sys.stdout.write(f"\033[{m}A")

    # Clear from cursor to the end of the screen
    sys.stdout.write("\033[J")

    sys.stdout.flush()


class Color(Vector3):
    def luminance(self) -> float:
        return self.dot(Color.WHITE / 3)

    BLACK: Color
    WHITE: Color
    GRAY: Color

    RED: Color
    GREEN: Color
    BLUE: Color


Color.BLACK = Color(0, 0, 0)
Color.WHITE = Color(1, 1, 1)
Color.GRAY = Color(0.5, 0.5, 0.5)
Color.RED = Color(1, 0, 0)
Color.GREEN = Color(0, 1, 0)
Color.BLUE = Color(0, 0, 1)


class Display(ABC):
    @abstractmethod
    def draw(self, data: list[list[Color]]):
        pass

    @abstractmethod
    def get_resolution(self) -> tuple[int, int]:
        """gets the resolution (height (V), width(H))"""
        pass

    @abstractmethod
    def get_pixel_ratio(self) -> float:
        pass


class ConsoleDisplay(Display):
    def get_resolution(self) -> tuple[int, int]:
        s = os.get_terminal_size()
        return (s.lines, s.columns)

    def get_pixel_ratio(self) -> float:
        return 0.5

    def draw(self, data: list[list[Color]]):
        content = "\n"

        for h in range(0, len(data)):
            row = data[h]
            for w in range(0, len(row)):
                col = data[h][w]

                char = self.__color_to_character(col)
                content += char
            if h != len(data) - 1:
                content += "\n"

        print(content, end="")

    @staticmethod
    def __color_to_character(col: Color) -> str:
        CHARS = (
            """ .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""
        )

        lum = max(0, min(1, col.luminance()))

        charIndex = int(lum * (len(CHARS) - 1))

        return CHARS[charIndex]

    @staticmethod
    def __clear_console():
        os.system("cls" if os.name == "nt" else "clear")
        # time.sleep(1)
        # sys.stdout.write("\033[2J\033[H")
        # sys.stdout.flush()
