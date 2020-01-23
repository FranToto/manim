# source venv/bin/activate --> To be in Python Virtual Env

from manimlib.imports import *
import math

class EqRabbit(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 3,
        "y_min" : 0,
        "y_max" : 10,
        "graph_origin" : DOWN*3 + RIGHT*2,
        "function_color" : WHITE,
        "axes_color" : BLUE,
        "x_axis_label": "$t$",
        "x_labeled_nums" :range(0,3),
        "y_axis_label": "$x$",
        "y_labeled_nums" :range(0,10),
        "exclude_zero_label": False,
        "x_axis_width": 4,
        "y_axis_height":5,
    }

    def construct(self):
        rab1 = ImageMobject("rabbitwhite")
        rab2 = ImageMobject("rabbitwhite")
        text = TextMobject("Imagine 2 cute little rabbits left alone on a new planet ...")
        text2 = TextMobject("As you might expect, they start having fun.")
        text3 = TextMobject("And have offsprings.")
        text4 = TextMobject("Let's count the population every regular period of time.")
        time0 = TextMobject("$t=0$")
        time1 = TextMobject("$t=1$")
        time2 = TextMobject("$t=2$")
        x0 = TextMobject("$x=2$")
        x1 = TextMobject("$x=4$")
        x2 = TextMobject("$x=8$")

        self.play(Write(text))
        self.wait()
        self.play(
                FadeIn(rab1),
                rab1.shift, LEFT*6, UP*1.5,
                FadeIn(rab2),
                rab2.shift, LEFT*6, DOWN*1.5,
                text.scale, 0.5,
                text.to_corner, UP + LEFT,
                run_time=2,
                path_arc=0 #Change 0 by -np.pi
            )
        self.wait()
        self.play(
                rab1.scale, 0.5,
                rab2.scale, 0.5,
            )
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(
            Transform(text2,text3),
            ApplyWave(rab1),
            ApplyWave(rab2),
            run_time=2,
        )
        self.wait()
        self.play(
            Transform(text2,text4),
            ApplyWave(rab1),
            ApplyWave(rab2),
            run_time=2,
        )
        self.wait()
        self.play(
                text2.scale, 0.5,
                text2.shift, UP*3 + LEFT*3.4,
                run_time=2,
                path_arc=0, #Change 0 by -np.pi
            )
        self.wait()

        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x(t)")

        point = Dot(self.coords_to_point(0,2))
        point2 = Dot(self.coords_to_point(1,4))
        point3 = Dot(self.coords_to_point(2,8))

        self.play(
                FadeIn(time0),
                time0.shift, LEFT*6, DOWN*3,
            )
        self.wait()
        self.play(
                FadeIn(x0),
                x0.shift, LEFT*6, DOWN*2.5,
                Write(point),
                point.scale,2,
            )
        self.wait()
        self.play(
                FadeIn(time1),
                time1.shift, LEFT*4, DOWN*3,
                rab1.shift, RIGHT*2,
                rab2.shift, RIGHT*2,
            )
        self.wait()
        self.play(
                FadeIn(x1),
                x1.shift, LEFT*4, DOWN*2.5,
                Write(point2),
                point2.scale,2,
        )
        self.wait()
        self.play(
                FadeIn(time2),
                time2.shift, LEFT*2, DOWN*3,
                rab1.shift, RIGHT*2,
                rab2.shift, RIGHT*2,
            )
        self.wait()
        self.play(
                FadeIn(x2),
                x2.shift, LEFT*2, DOWN*2.5,
                Write(point3),
                point3.scale,2,
        )

 ### FUNCTIONS     
    def func_to_graph(self,t):
        return (2*math.exp(2*t))


class GraphRabbit(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 3,
        "y_min" : 0,
        "y_max" : 10,
        "graph_origin" : DOWN*3 + LEFT*6,
        "function_color" : WHITE,
        "axes_color" : BLUE,
        "x_axis_label": "$t$",
        "x_labeled_nums" :range(0,3),
        "y_axis_label": "$x$",
        "y_labeled_nums" :range(0,10),
        "exclude_zero_label": False,
        "x_axis_width": 5,
        "y_axis_height":5,
    }

    def construct(self):
        
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x(t)")

        vline = self.get_vertical_line_to_graph(2,func_graph)

        t = self.coords_to_point(1,self.func_to_graph(1))
        x = self.coords_to_point(0,self.func_to_graph(1))

        hline = Line(t,x,color=YELLOW)

        point = Dot(self.coords_to_point(0,self.func_to_graph(0)))
        point2 = Dot(self.coords_to_point(1,self.func_to_graph(1)))
        point3 = Dot(self.coords_to_point(2,self.func_to_graph(2)))

        #self.play(ShowCreation(func_graph), Write(graph_lab))
        #self.wait()
        # App points -> Add other points of t=1,2, then link graph scene to Intro scene
        #self.add(point)
        self.play(
                Write(point),
                point.scale,2,
            )
        self.wait()
        self.play(
                Write(point2),
                point2.scale,2,
            )
        self.wait()
        self.play(
                Write(point3),
                point3.scale,2,
            )
        self.wait()
        self.play(
                ShowCreation(vline),
                ShowCreation(hline),
        )
        for i in range(1,5):
            rab1 = ImageMobject("rabbitwhite")
            rab1.shift(i*RIGHT)
            rab1.scale(0.25)
            self.add(rab1) 
            self.wait()
        self.wait()   

    def func_to_graph(self,t):
        return (2*exp(2*t))


class CopyRabbit(Scene):
    def construct(self):
        rab1 = ImageMobject("rabbitwhite")
        time0 = TextMobject("$t=0$")
        time1 = TextMobject("$t=1$")
        time1.to_edge(DOWN + LEFT)
        self.add(rab1)
        self.play(
            ReplacementTransform(rab1,rab1),
            rab1.shift, UP,
        )
        self.play(
                FadeInFrom(time0,DOWN),
                FadeInFrom(time1,DOWN)
        )



