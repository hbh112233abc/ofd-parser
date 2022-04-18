class ST_Pos():
    """
    点坐标
    空格分割,前为x,后为y
    整数或浮点数
    """
    def __init__(self,position:str):
        pos = position.split(' ')
        assert len(pos) == 2, "Invalid position string"
        self.x = float(pos[0])
        self.y = float(pos[1])

    def __str__(self):
        return f'<ST_Pos x={self.x},y={self.y}>'
