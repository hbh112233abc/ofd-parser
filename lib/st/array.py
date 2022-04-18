class ST_Array():
    """
    以空格分割的数组
    元素可以是除ST_Loc,ST_Array外的数据类型,不可嵌套
    """
    def __init__(self,array_str:str):
        self.array_str = array_str

    def __str__(self):
        return f"<ST_Array `{self.array_str}`>"

    def array(self)->list:
        return self.array_str.split(' ')
