#!/usr/bin/env python
# source venv/bin/activate --> To be in Python Virtual Env

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

class FirstScene(Scene):
    def construct(self):
        text=TextMobject("text")
        #self.add(text) #Not animated
        self.play(FadeIn(text),run_time=2)
# Different animation to Play : Write, GrowFromCenter, FadeIn -> In the /manimlib/animation/creation.py folder
        self.wait(1)
# n seconds wait
        self.remove(text)
        self.wait(1)


# See old_projects folder for many, many more

class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("finger")
        self.play(DrawBorderThenFill(svg,rate_func=linear))
        self.wait()

class ImageTest(Scene):
    def construct(self):
        image = ImageMobject("rabbitwhite")
        self.play(FadeIn(image))
        self.wait()

class EqRabbit(Scene):
    def construct(self):
        rab1 = ImageMobject("rabbitwhite")
        rab2 = ImageMobject("rabbitwhite")
        text = TextMobject("Imagine 2 cut little rabbits left alone on a new planet ...")
        text2 = TextMobject("As you might expect, they start having fun.")
        text3 = TextMobject("And after a time t, we observe 4 more rabbits on the planet.")
		#text.shift(LEFT*2)
        self.play(Write(text))
        self.wait()
        self.play(
                text.scale, 0.5,
                text.to_corner, UP + LEFT,
                run_time=2,
                path_arc=0 #Change 0 by -np.pi
            )
        self.wait()
        self.play(
                FadeIn(rab1),
                rab1.shift, LEFT*6, UP*1.5,
                FadeIn(rab2),
                rab2.shift, LEFT*6, DOWN*1.5,
            )
        self.play(
                rab1.scale, 0.5,
                rab2.scale, 0.5
            )
        self.wait()
        self.play(
                Write(text2),
                rab1.shift, DOWN*1,
                rab2.shift, UP*1,
            )
        self.play(
                rab1.shift, UP*1,
                rab2.shift, DOWN*1,
            )
        self.wait()
		#self.play(ReplacementTransform(text2,text3))
        #self.wait()
