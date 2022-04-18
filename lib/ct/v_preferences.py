# 视图首选项
class CTVPreferences:
    def __init__(self,page_mode:str='None',page_layout:str='OneColumn',tab_display:str='FileName',hide_toolbar:bool=False,hide_menubar:bool=False,hide_window_ui:bool=False,zoom_mode:str='Default',zoom:float=1.0):
        """视图首选项

        Args:
            page_mode (str, optional): 窗口模式.
                None-常规模式
                FullScreen-打开后全文显示
                UseOutlines-同时呈现文档大纲
                UseThumbs-同时呈现缩略图
                UseCustomTags-同时呈现语义结构
                UseLayers-同时呈现图层
                UseAttatchs-同时呈现附件
                UseBookmarks-同时呈现书签
             Defaults to 'None'.
            page_layout (str, optional): 页面布局模式,可取值如下:
                OnePage-单页模式
                OneColumn-单列模式
                TwoPageL-对开模式
                TwoColumnL-对 开连续模式
                TwoPageR-对开靠右模式
                TwoColumnR-对开连续靠右模式. Defaults to 'OneColumn'.
            tab_display (str, optional): 标题栏显示模式.
                FileName-文件名称
                DocTitle-元数据中的Title
             Defaults to 'FileName'.
            hide_toolbar (bool, optional): 隐藏工具栏. Defaults to False.
            hide_menubar (bool, optional): 隐藏菜单栏. Defaults to False.
            hide_window_ui (bool, optional): 隐藏主窗口之外其他窗口组件. Defaults to False.
            zoom_mode (str, optional): 自动缩放模式.
                Delault-默认縮放
                FitHeight-适合高度
                FitWidth-适合宽度
                FitRect-适合区域
             Defaults to 'Default'.
            zoom (float, optional): 文档缩放率. Defaults to 1.0.
        """
        assert page_mode in ("None","FullScreen","UseOutlines","UseThumbs","UseCustomTags","UseLayers","UseAttatchs","UseBookmarks"),"PageMode must be one of:None,FullScreen,UseOutlines,UseThumbs,UseCustomTags,UseLayers"
        self.PageMode = page_mode
        assert page_layout in ("OnePage","OneColumn","TwoPageL","TwoColumnL","TwoPageR","TwoColumnR"),"PageLayout must be one of: OnePage, OneColumn, TwoPageL, TwoColumnL,TwoPageR,TwoColumnR"
        self.PageLayout = page_layout
        assert tab_display in ("FileName","Title"),"TabDisplay must be one of: FileName,Title"
        self.TabDisplay = tab_display
        self.HideToolbar = hide_toolbar
        self.HideMenubar = hide_menubar
        self.HideWindowUI = hide_window_ui
        assert zoom_mode in ("Delault","FitHeight","FitWidth","FitRect",),"ZoomMode must be one of:Default,FitHeitht,FitWidth,FitRect"
        self.ZoomMode = zoom_mode
        self.Zoom = zoom
