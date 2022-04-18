from st.box import ST_Box

# 页面区域
class CT_PageArea:
    def __init__(self,physical_box:ST_Box,application_box:ST_Box=None,content_box:ST_Box=None,bleed_box:ST_Box=None):
        """页面区域

        Args:
            physical_box (ST_Box): 物理区域,左上角为原点
            application_box (ST_Box, optional): 显示区域,页面内容实际显示或打印的区域,位于物理区域内,包含页眉,页脚,版心等内容. Defaults to None.
            content_box (ST_Box, optional): 版心区域,正文区域,左上角坐标决定了其在显示区域的位置; [例外处理] 如果版心区域不完全位于显示区域内,显示区域外的部分则被忽略;如果版心区域完全位于显示区域外,则版心区域不被绘制. Defaults to None.
            bleed_box (ST_Box, optional): 出血区域,即超出设备性能限制的额外出血区域,物理区域之外;不出现时,默认值位物流区域;[例外处理]如果出血区域不完全位于页面物理区域外,页面物理区域内的部分则被忽略。如果出血区域完全位于页面物理区域内，出血区域无效. Defaults to None.
        """
        self.PhysicalBox = physical_box
        self.ApplicationBox = application_box
        self.ContentBox = content_box
        self.BleedBox = bleed_box
