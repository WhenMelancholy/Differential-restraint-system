from manim import *


class HappyTest(Scene):
    def construct(self):
        happy = SVGMobject(r"E:\github\Differential-restraint-system\video\asset\happy.svg")
        self.play(ShowCreation(happy))
