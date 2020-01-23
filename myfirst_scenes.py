#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim myfirst_scenes.py Example1 -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class Example1(Scene):
    def construct(self):
        title2 = TextMobject("Hellaaa")
        basel2 = TexMobject(
            "f"
        )
        VGroup(title2,basel2).arrange(DOWN)
        self.play(
            Write(title2),
            FadeInFrom(basel2, UP),
        )
        self.wait()

        title = TextMobject("Exponential Growth")
        basel = TexMobject(
            "\\frac{df}{dt} = rt"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            FadeOut(title2),
            FadeOut(basel2),
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
