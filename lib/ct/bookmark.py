from .dest import CT_Dest
# 书签
class CT_Bookmark:
    def __init__(self,name:str,dest:CT_Dest):
        """书签

        Args:
            name (str): 书签名称
            dest (CT_Dest): 书签对应文档位置
        """
        self.Name = name
        self.Dest = dest
