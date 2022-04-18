from st.ref_id import ST_RefID
# 图层
class CT_Layer:
    def __init__(self,type:str='Body',draw_param:ST_RefID=None):
        assert type in ('Body','Foreground','Background'),"Layer type must be one of ['Body','Foreground','Background']"
        self.Type = type
        self.DrawParam = draw_param
