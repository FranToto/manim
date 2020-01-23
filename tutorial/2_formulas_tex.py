from manimlib.imports import *

class Formula(Scene):
    def construct(self):
        formula_tex=TexMobject(r"\frac{d}{dx}f(x)=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}")
        formula_tex.scale(0.5)
        self.add(formula_tex)



