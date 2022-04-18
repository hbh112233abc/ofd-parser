import os

class ST_Loc():
    """
    包结构内的文件路径
        "." 表示当前路径
        ".." 表示父级路径
        "/" 表示根路径
        未显示指定表示当前路径
        路径区分大小写
    """
    def __init__(self,path:str,parent:str):
        self.path = path
        self.parent = parent

    def __str__(self):
        return f'<ST_Loc `{self.path}`>'

    def realpath(self):
        return os.path.join(self.parent,self.path)
