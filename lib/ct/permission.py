from .print import CT_Print
from valid_period import CT_ValidPeriod
# 权限声明
class CT_Permission:
    def __init__(self):
        # 编辑
        self.Edit = True
        # 标注
        self.Anot = True
        # 导出
        self.Export = True
        # 数字签名
        self.Signature = True
        # 添加水印
        self.Watermark = True
        # 截屏
        self.PrintScreen = True
        # 打印
        self.Print = CT_Print()
        # 有效期
        self.ValidPeriod = CT_ValidPeriod()
