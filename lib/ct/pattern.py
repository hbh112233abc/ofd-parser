from st.array import ST_Array
from st.ref_id import ST_RefID
from page_block import CT_PageBlock

# 底纹结构
class CT_Pattern:
    def __init__(
        self,
        width:float,
        height:float,
        x_step:float=0,
        y_step:float=0,
        reflect_method:str='Normal',
        relative_to:str='Object',
        ctm:ST_Array=None,
        cell_content:CT_PageBlock=None,
        thumbnail:ST_RefID=None
    ):
        """底纹属性

        Args:
            width (float): 底纹单元的宽度
            height (float): 底纹单元的高度
            x_step (float, optional): X方向底纹单元的间距,默认为底纹单元的宽度,若设定值小于底纹单元宽度时,应按默认值处理. Defaults to 0.
            y_step (float, optional): Y方向底纹单元的间距,默认为底纹单元的高度,若设定值小于底纹单元高度时,应按默认值处理. Defaults to 0.
            reflect_method (str, optional): 描述底纹单元的印象翻转方式,枚举值(Normal,Column,Row,RowAndColumn). Defaults to 'Normal'.
            relative_to (str, optional): 底纹单元起始绘制位置 Page:相对于页面坐标系的原点;Object:相对于对象坐标系的原点. Defaults to 'Object'.
            ctm (ST_Array, optional): 底纹单元的变换矩阵,用于某些需要对底纹单元进行平移旋转变换的场合,默认为单位矩阵;底纹呈现时先做XStcp、YStcp排列,然后起做CTM处理. Defaults to None.
            cell_content (CT_PageBlock, optional): 底纹单元,用底纹填充目标区域时,所使用的单元对象CellContent作为底纹对象的绘制单元,使用一-种和外界没有任何关联的独立的坐标空间:坐标以左上角(0,0)为原点,X轴向右增长,Y轴向下增长，单位为毫米。. Defaults to None.
            thumbnail (ST_RefID, optional): 引用资源文件中缩略图图像的标识. Defaults to None.
        """
        self.Width = width
        self.Height = height
        self.XStep = max(x_step,self.Width)
        self.YStep = max(y_step,self.Height)
        assert reflect_method in ("Normal","Column","Row","RowAndColumn"),'ReflectMethod must be one of ["Normal","Column","Row","RowAndColumn"]'
        self.ReflectMethod = reflect_method
        self.RelativeTo = relative_to
        self.CTM = ctm
        self.CellContent = cell_content
        self.Thumbnail = thumbnail
