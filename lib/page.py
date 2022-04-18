from st import *
from ct import *

# 页面节点
class PageNode():
    def __init__(self,id:ST_ID,base_loc:ST_Loc):
        """页面节点

        Args:
            id (ST_ID): _description_
            base_loc (ST_Loc): _description_
        """
        self.ID = id
        self.BaseLoc = base_loc

# 模板页
class Template:
    """
    该页所使用的模板页。
    模板页的内容结构和普通页相同,定义在CommonData指定的XMI.文件中。-一个页可以使用多个模板页。该节点使用时通过TemplatclID来引用具体的模板,并通过ZOrder属性来控制模板在页面中的呈现顺序
    注:在模板页的内容描述中该属性无效
    """
    def __init__(self,id:ST_RefID,z_order:str="Background"):
        self.TemplateId = id

class Page:
    def __init__(self,area:CT_PageArea,template:Template,page_res:ST_Loc,content:List[CT_Layer]=None,actions:List[CT_Action]=None)
