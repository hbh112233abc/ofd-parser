from typing import List
from action import CT_Action
from outline_elem import CT_OutlineElem
# 大纲节点
class CT_OutlineElem:
    def __init__(
        self,
        title:str,
        count:int=0,
        expanded:bool=True,
        actions:List[CT_Action]=None,
        children:List[CT_OutlineElem]=None
    ):
        self.Title = title
        self.Count = count
        self.Expanded = expanded
        self.Actions = actions
        self.Children = children
