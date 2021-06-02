from manim import *
from pathlib import Path
import os

RESOLUTION = ""
FLAGS = f"ps {RESOLUTION}"
SCENE = "FourierSeries"


class FourierSeries(Scene):
    def construct(self):
        fourier_transform = MathTex("f(t)=",
                                    "\\frac{a_0}{2}",
                                    "+"
                                    "\sum_{n=1}^{\infty}a_ncosnt",
                                    "+",
                                    "\sum_{n=1}^{\infty}b_nsinnt")
        copyright = MathTex("\\copyright cognitojayant").shift(3 * DOWN + 6 * RIGHT).scale(0.5)
        self.add(fourier_transform, copyright)
        self.play(Write(fourier_transform))
        self.wait()
        self.play(fourier_transform.animate.move_to(3 * UP))
        self.wait()
        brace1 = Brace(fourier_transform[1], DOWN, buff=SMALL_BUFF)
        brace1.set_color(GREEN)
        brace2 = Brace(fourier_transform[2], DOWN, buff=SMALL_BUFF)
        brace2.set_color(YELLOW)
        brace3 = Brace(fourier_transform[4], DOWN, buff=SMALL_BUFF)
        brace3.set_color(RED)
        a_0 = MathTex("a_0", "=", "\\frac{1}{\\pi}\\, \\int_{\\alpha}^{\\alpha + 2\\pi}\\,f(t)\\,dt", color=GREEN)
        self.play(
            FadeIn(brace1),
            Write(a_0),
        )
        self.wait()
        self.play(
            FadeIn(brace1),
            a_0.animate.move_to(1.3 * UP + 4 * LEFT)
        )
        a_n = MathTex("a_n", "=", "\\frac{1}{\\pi}\\, \\int_{\\alpha}^{\\alpha + 2\\pi}\\,f(t)\\,cosnt \\,dt",
                      color=YELLOW)
        self.play(
            FadeIn(brace2),
            Write(a_n),
        )
        self.wait()
        self.play(
            FadeIn(brace2),
            a_n.animate.move_to(0.5 * DOWN + 4 * LEFT)
        )

        b_n = MathTex("b_n", "=", "\\frac{1}{\\pi}\\, \\int_{\\alpha}^{\\alpha + 2\\pi}\\,f(t)\\,sinnt \\,dt",
                      color=RED).move_to(2 * DOWN)
        self.play(
            FadeIn(brace3),
            Write(b_n),
        )
        self.wait()
        self.play(
            FadeIn(brace3),
            b_n.animate.move_to(2.5 * DOWN + 4 * LEFT)
        )
        self.wait()


if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
