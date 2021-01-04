from manim import *
import numpy as np


class What(Scene):
    def construct(self):
        config.frame_width = 4
        config.frame_height = 12

        tex = MathTex(
            r"x_1,\cdots,&x_n\\",
            r"x_{i_1}-x_{j_1}&\leq c_1\\" + r"x_{i_2}-x_{j_2}&\leq c_2\\" +
            r"\vdots&\\" + r"x_{i_n}-x_{j_n}&\leq c_m\\",
        )
        self.play(Write(tex))
        self.wait()

        braceUp = Brace(tex[0], UP, buff=SMALL_BUFF)
        braceRight = Brace(tex[1], RIGHT, buff=SMALL_BUFF)
        textUp = braceUp.get_text("$n$ variables")
        textRight = braceRight.get_text("$m$ equations")
        self.play(
            GrowFromCenter(braceUp),
            FadeIn(textUp),
        )
        self.wait()
        self.play(
            GrowFromCenter(braceRight),
            FadeIn(textRight),
        )
        self.wait()


class Graph(Scene):
    def construct(self):
        config.frame_width = 4
        config.frame_height = 12
        A = Circle(radius=0.25,
                   fill_color=WHITE,
                   fill_opacity=1,
                   stroke_color=WHITE)
        B = Circle(radius=0.25,
                   fill_color=WHITE,
                   fill_opacity=1,
                   stroke_color=WHITE)
        C = Circle(radius=0.25,
                   fill_color=WHITE,
                   fill_opacity=1,
                   stroke_color=WHITE)
        pA = np.array([0, 0, 0])
        pB = np.array([2, 0, 0])
        pC = np.array([2, 2, 0])
        A.move_to(pA)
        B.move_to(pB)
        C.move_to(pC)

        # 绘制图的节点结束
        # 开始绘制图的边

        arrowAB = Arrow(pA, pB).set_color(YELLOW)
        arrowAC = Arrow(pA, pC).set_color(YELLOW)
        arrowBC = Arrow(pB, pC).set_color(YELLOW)

        # 绘制完边
        # 开始绘制边权

        textAB = MathTex("w_{AB}").next_to(arrowAB, DOWN)
        textAC = MathTex("w_{AC}").next_to(arrowAC, np.array(
            [-0.5, 0.5, 0])).shift(0.75 * RIGHT).shift(0.75 * DOWN)
        textBC = MathTex("w_{BC}").next_to(arrowBC, RIGHT)

        # 开始绘制节点标号
        markA = Text("A").set_color(BLACK).move_to(pA)
        markB = Text("B").set_color(BLACK).move_to(pB)
        markC = Text("C").set_color(BLACK).move_to(pC)

        self.play(
            GrowFromCenter(A),
            GrowFromCenter(B),
            GrowFromCenter(C),
            Write(markA),
            Write(markB),
            Write(markC),
        )
        self.wait()
        self.play(
            GrowArrow(arrowAB),
            GrowArrow(arrowAC),
            GrowArrow(arrowBC),
            Write(textAB),
            Write(textAC),
            Write(textBC),
        )
        self.wait()

        # 开始绘制公式
        equDis = MathTex(
            r"\text{dis}(B)\leq \text{dis}(C)+&w_{BC}\\",
            r"\Downarrow&\\",
            r"\text{dis}(B)-\text{dis}(C)\leq& w_{BC}\\",
            r"\Downarrow&\\",
            r"x_b-x_c\leq &c_k\\",
        ).next_to(A, LEFT)
        self.play(Write(equDis))
        self.wait()


# examples in Manim Community
class MovingBraces(Scene):
    def construct(self):
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=",  # 0
            "f(x)\\frac{d}{dx}g(x)",  # 1
            "+",  # 2
            "g(x)\\frac{d}{dx}f(x)",  # 3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(ReplacementTransform(brace1, brace2),
                  ReplacementTransform(t1, t2))
        self.wait()


class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX").scale(3)
        self.add(tex)


class HelloTex(Scene):
    def construct(self):
        tex = Tex(r"$\xrightarrow{x^2y^3}$ \LaTeX").scale(3)
        self.add(tex)


class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r"$\mathtt{H} \looparrowright$ \LaTeX").scale(3)
        self.add(tex)


class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r"Hello \LaTeX", color=BLUE).scale(3)
        self.add(tex)


class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(r"$\mathscr{H} \rightarrow \mathbb{H}$}",
                  tex_template=myTemplate).scale(3)
        self.add(tex)


class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex("Hello", r"$\bigstar$", r"\LaTeX").scale(3)
        tex.set_color_by_tex("igsta", RED)
        self.add(tex)


class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(r"$x^2 + y^2 = z^2$",
                  tex_template=TexFontTemplates.french_cursive).scale(3)
        self.add(tex)


class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex("Hello 你好 \\LaTeX",
                  tex_template=TexTemplateLibrary.ctex).scale(3)
        self.add(tex)


class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r"f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6").scale(2)
        self.add(tex)
