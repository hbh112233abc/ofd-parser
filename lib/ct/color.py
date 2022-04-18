from st.array import ST_Array
from st.ref_id import ST_RefID
from pattern import CT_Pattern
from axial_shd import CT_AxialShd
from radial_shd import CT_RadialShd
from gouraud_shd import CT_GouraudShd
from la_gouraud_shd import CT_LaGouraudShd
# 颜色
class CT_Color:
    def __init__(
        self,
        value:ST_Array=None,
        index:int=None,
        color_space:ST_RefID=None,
        alpha:int=255,
        pattern:CT_Pattern=None,
        axial_shd:CT_AxialShd=None,
        radial_shd:CT_RadialShd=None,
        gouraud_shd:CT_GouraudShd=None,
        la_gouraud_shd:CT_LaGouraudShd=None
    ):
        """颜色属性

        Args:
            value (ST_Array, optional): 颜色值,指定了当前颜色空间下各通道的取值。Value 的取值应符合"通道1通道2通道3.."格式。此属性不出现时，应采用Index属性从颜色空间的调色板中的取值。当二者都不出现时,该颜色各通道的值全部为0. Defaults to None.
            index (int, optional): 调色板中颜色的编号,非负整数,将从当前颜色空间的调色板中取出相应索引的预定义颜色用来绘制。索引从0开始. Defaults to None.
            color_space (ST_RefID, optional): 引用资源文件中颜色空间的标识默认值为文档设定的颜色空间. Defaults to None.
            alpha (int, optional): 颜色透明度,在0~255之间取值。默认为255,表示完全不透明. Defaults to 255.
            pattern (CT_Pattern, optional): 底纹填充,复杂颜色的一种。描述见8.3.3. Defaults to None.
            axial_shd (CT_AxialShd, optional): 轴向渐变,复杂颜色的一种。描述见8.3.1.2. Defaults to None.
            radial_shd (CT_RadialShd, optional): 径向渐变,复杂颜色的一种。描述见8.3.4.3. Defaults to None.
            gouraud_shd (CT_GouraudShd, optional): 高洛德渐变,复杂颜色的一种。描述见8.3.1.4. Defaults to None.
            la_gouraud_shd (CT_LaGouraudShd, optional): 格构高洛德渐变,复杂颜色的一种。描述见8.3.1.5. Defaults to None.
        """
        self.Value = value
        self.Index = index
        self.ColorSpace = color_space
        self.Alpha = alpha
        self.Pattern = pattern
        self.AxialShd = axial_shd
        self.RadialShd = radial_shd
        self.GouraudShd = gouraud_shd
        self.LaGouraudShd = la_gouraud_shd
