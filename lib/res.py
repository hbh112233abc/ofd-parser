from typing import List
from st import *
from ct import CT_ColorSpace, CT_DrawParam,CT_Font,CT_MultiMedia,CT_VectorG
class Res:
    def __init__(self,base_loc:ST_Loc,color_spaces:List[CT_ColorSpace]=None,draw_params:List[CT_DrawParam]=None,fonts:List[CT_Font]=None,multi_medias:List[CT_MultiMedia]=None,composite_graphic_units:List[CT_VectorG]=None):
        self.BaseLoc = base_loc
        self.ColorSpaces = color_spaces
        self.DrawParams = draw_params
        self.Fonts = fonts
        self.MultiMedias = multi_medias
        self.CompositeGraphicUnits = composite_graphic_units
