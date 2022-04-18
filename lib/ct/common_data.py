from st.id import ST_ID
from st.ref_id import ST_RefID
from st.loc import ST_Loc
from page_area import CT_PageArea
from template_page import CT_TemplatePage


# 文档公共数据
class CT_CommonData:
    def __init__(self,max_unit_id:ST_ID,page_area:CT_PageArea,public_res:ST_Loc=None,document_res:ST_Loc=None,template_page:CT_TemplatePage=None,default_cs:ST_RefID=None):
        """文档公共数据

        Args:
            max_unit_id (ST_ID): 当前文档所有对象使用标识的最大值,初始值0;
            page_area (PageArea): 指定页面区域的默认大小和位置
            public_res (ST_Loc, optional): 公共资源序列. Defaults to None.
            document_res (ST_Loc, optional): 文档资源序列. Defaults to None.
            template_page (CT_TemplatePage, optional): 模板页序列. Defaults to None.
            default_cs (ST_RefID, optional): 引用在资源文件中定义的颜色空间标识,如果此项不存在,采用RGB位默认颜色空间. Defaults to ''.
        """
        self.MaxUnitID = max_unit_id
        self.PageArea = page_area
        self.PublicRes = public_res
        self.DocumentRes = document_res
        self.Template = template_page
        self.DefaultCS = default_cs
