from ct import CT_Action,CT_OutlineElem
# 大纲
class OutlineElem():
    def __init__(self,title:str,count:int=0,expanded:bool=True,actions:List[CT_Action]=None,outline_elem:CT_OutlineElem=None):
        self.Title = title
        self.Count = count
        self.Expanded = expanded
        self.Actions = actions
        self.OutlineElem = outline_elem
