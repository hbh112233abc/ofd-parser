# 打印权限
class CT_Print:
    def __init__(self,printable:bool=True,copies:int=-1):
        """打印权限

        Args:
            printable (bool, optional): 是否允许被打印. Defaults to True.
            copies (int, optional): 打印份数,在Printable为true时有效,若Printable 为true并且不设置Copics则打印份数不受限,若Copics的值为负值时,打印份数不受限,当Copics的值为0时,不允许打印,当Copics的值大于0时，则代表实际可打印的份数值. Defaults to -1.
        """
        self.Printable = printable
        self.Copies = copies
