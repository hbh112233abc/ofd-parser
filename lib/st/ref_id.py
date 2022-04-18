from .id import ST_ID
class ST_RefID(ST_ID):
    """
    ID标识引用
    此标识应该是文档内已定义的ID标识
    """
    def __init__(self,id):
        super(ST_RefID, self).__init__(id)
