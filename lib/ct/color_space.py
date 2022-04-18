from st.array import ST_Array
from st.loc import ST_Loc
# 颜色空间
class CT_ColorSpace:
    def __init__(self,type:str='RGB',bits_per_component:int=8,profile:ST_Loc=None,palette:ST_Array=None):
        """颜色空间

        Args:
            type (str, optional): 类型."RGB","GRAY","CMYK" Defaults to 'RGB'.
            bits_per_component (int, optional): 每个颜色通道所使用的位数,有效取值为:1,2,4,8,16. Defaults to 8.
            profile (ST_Loc): 颜色配置文件
            palette (ST_Array): 调色板
        """
        assert type in ("RGB","GRAY","CMYK"),"ColorSpace type must be one of ['RGB','GRAY','CMYK']"
        self.Type = type
        assert bits_per_component in (1,2,4,8,16),"ColorSpace BitsPerComponent must be one of (1,2,4,8,16)"
        self.BitsPerComponent = bits_per_component
        self.Profile = profile
        self.Palette = palette
