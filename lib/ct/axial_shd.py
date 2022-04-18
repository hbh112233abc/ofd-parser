from typing import List

from st.pos import ST_Pos
from segment import CT_Segment
# 轴向渐变
class CT_AxialShd:
    def __init__(self,start_point:ST_Pos,end_point:ST_Pos,segments:List[CT_Segment],map_type:str='Direct',map_unit:float=None,extend:int=0):
        """轴向渐变

        Args:
            start_point (ST_Pos): 轴线的起始点
            end_point (ST_Pos): 轴线的结束点
            segments (List[CT_Segment]): 颜色段，至少出现两个
            map_type (str, optional): 渐变绘制的方式,可选值为Direct、Repeat、Reflect. Defaults to 'Direct'.
            map_unit (float, optional): 轴线一个渐变区间的长度,当MapType的值不等于Direct时出现 默认值为轴线长度. Defaults to None.
            extend (int, optional): 轴线延长线方向是否继续绘制渐变。可选值为0、1、2、3
                0:不向两侧继续绘制渐变
                1:在结束点至起始点延长线方向绘制渐变
                2:在起始点至结束点延长线方向绘制渐变
                3:向两侧延长线方向绘制渐变
                Defaults to 0.
        """
        assert len(segments) >= 2,'Segments length must >= 2'
        self.Segments = []
        if segments[0].Position is None:
            segments[0].Position = 0
        if segments[-1].Position is None:
            segments[-1].Position = 1.0
        for i, segment in enumerate(segments):
            if segment.Position is None:
                if segments[i+1].Position is None:
                    segment.Position = 1*i/len(segments)
                else:
                    segment.Position = segments[i-1].Position + (segments[i+1].Position-segments[i-1].Position)/2
            self.Segments.append(segment)
        self.StartPoint = start_point
        self.EndPoint = end_point
        assert map_type in ('Direct','Repeat','Reflect'),"MapType must be one of ['Direct','Repeat','Reflect']"
        self.MapType = map_type
        self.MapUnit = map_unit
        assert isinstance(extend,int) and 0<=extend<=3,'Extend must be between 0 and 3'
        self.Extend = extend
