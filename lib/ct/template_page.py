from st.id import ST_ID
from st.loc import ST_Loc
# 页面模板
class CT_TemplatePage:
    def __init__(self,id:ST_ID,base_loc:ST_Loc,name:str='',z_order:str='Background'):
        self.ID = id
        self.BaseLoc = base_loc
        self.Name = name
        self.ZOrder = z_order
