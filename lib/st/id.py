class ST_ID():
    """
    ID标识
    无符号整数,文档内唯一,0表示无效标识
    """
    def __int__(self,id:int):
        assert isinstance(id,int) and id > 0, "Invalid ID"
        self.id = int(id)
