from st.ref_id import ST_RefID
from st.array import ST_Array
from color import CT_Color

# 绘制参数
class CT_DrawParam:
    def __init__(self,relative:ST_RefID=None,join:str="Miter",line_width:float=0.353,dash_offset:float=0,dash_pattern:ST_Array=None,cap:str="Butt",miter_limit:float=3.528,fill_color:CT_Color=None,stroke_color:CT_Color=None):
        """绘制参数

        Args:
            relative (ST_RefID, optional): 基础绘制参数,引用资源文件中的绘制参数标识. Defaults to None.
            join (str, optional): 线条连接样式.
                Miter-直角
                Round-圆角
                Bevel-斜角
             Defaults to "Miter".
            line_width (float, optional): 线宽. Defaults to 0.353.
            dash_offset (float, optional): 虚线样式,DashPattern存在时才生效. Defaults to 0.
            dash_pattern (ST_Array, optional): 虚线重复样式. Defaults to None.
            cap (str, optional): 线端点样式.
                Butt-无封边
                Round-圆角
                Square-直角
             Defaults to "Butt".
            miter_limit (float, optional): Join为Miter时小角度结合点的截断值. Defaults to 3.528.
            fill_color (CT_Color, optional): 填充颜色,默认透明色. Defaults to None.
            stroke_color (CT_Color, optional): 勾边颜色,默认黑色. Defaults to None.
        """
        self.Relative = relative
        assert join in ("Miter","Round","Bevel"), "join should be one of Miter,Round,Bevel"
        self.Join = join
        self.LineWidth = line_width
        self.DashOffset = dash_offset
        self.DashPattern = dash_pattern
        self.Cap = cap
        self.MiterLimit = miter_limit
        self.FillColor = fill_color
        self.StrokeColor = stroke_color
