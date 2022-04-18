class ST_Box():
    """
    矩形区域
    以空格分割
    前两个值表示左上角坐标
    后两个值表示宽,高
    数值可以是整数或浮点数
    宽高须>0
    """
    def __init__(self,box:str):
        box_split = box.split(' ')
        assert len(box_split) == 4, "Invalid box string"
        self.x = float(box_split[0])
        self.y = float(box_split[1])
        self.width = float(box_split[2])
        self.height = float(box_split[3])
        assert self.width > 0 and self.height > 0, "width and height must > 0"

    def __str__(self):
        return f'<ST_Box x={self.x},y={self.y},width={self.width},height={self.height}>'
