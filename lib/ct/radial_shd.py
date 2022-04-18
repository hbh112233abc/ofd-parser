from typing import List
from st.pos import ST_Pos
from segment import CT_Segment
# 径向渐变
class CT_RadialShd:
    def __init__(
        self,
        segments: List[CT_Segment],
        start_point:ST_Pos,
        end_point:ST_Pos,
        end_radius:float,
        start_radius:float=0,
        map_type:str='Direct',
        map_unit:float=None,
        eccentricity:float=0,
        angle:float=0,
        extend:int=0,
    ):
        """径向渐变

        Args:
            segments (List[CT_Segment]): 颜色段，至少出现两个
            start_point (ST_Pos): _description_
            end_point (ST_Pos): _description_
            end_radius (float): _description_
            start_radius (float, optional): _description_. Defaults to 0.
            map_type (str, optional): _description_. Defaults to 'Direct'.
            map_unit (float, optional): _description_. Defaults to None.
            eccentricity (float, optional): _description_. Defaults to 0.
            angle (float, optional): _description_. Defaults to 0.
            extend (int, optional): _description_. Defaults to 0.
        """
        self.MapType = map_type
        self.MapUnit = map_unit
        self.Eccentricity = eccentricity
        self.Angle = angle
        self.StartPoint = start_point
        self.EndPoint = end_point
        self.StartRadius = start_radius
        self.EndRadius = end_radius
        self.Extend = extend
        self.Segments = segments
