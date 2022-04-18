from color import CT_Color

# 颜色段
class CT_Segment:
    def __init__(self,color:CT_Color,position:float=None):
        self.Position = position
        self.Color = color
