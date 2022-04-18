from text import CT_Text
from path import CT_Path
from image import CT_Image
from composite import CT_Composite

# 页面块
class CT_PageBlock:
    def __init__(self,page_block,text_object:CT_Text,path_object:CT_Path,image_object:CT_Image,composite_object:CT_Composite):
        """页面块

        Args:
            page_block (CT_PageBlock): 页面块,可以嵌套
            text_object (CT_Text): 文字对象
            path_object (CT_Path): 图形对象
            image_object (CT_Image): 图像对象
            composite_object (CT_Composite): 复合对象
        """
        self.PageBlock = page_block
        self.TextObject = text_object
        self.ImageObject = image_object
        self.PathObject = path_object
        self.CompositeObject = composite_object
