# 文档元数据
class CT_DocInfo:
    """
    文档元数据
    """
    def __init__(self):
        # 文档ID,采用uuid生成的32位标识
        self.DocID = ''
        # 文档标题
        self.Title = ''
        # 文档作者
        self.Author = ''
        # 文档主题
        self.Subject = ''
        # 摘要与注释
        self.Abstract = ''
        # 创建日期
        self.CreationDate = ''
        # 最新修改日期
        self.ModDate = ''
        # 分类
        #   Normal:普通文档(默认)
        #   EBook:电子书
        #   ENewPaper:电子报纸
        #   EMagzine:电子期刊杂志

        self.DocUsage = 'Normal'
        # 文档封面 图片路径
        self.Cover = ''
        # 关键词集合 每个关键词用一个Keyword子节点表达
        self.Keywords = []
        # 创建文档的应用程序
        self.Creator = ''
        # 创建文档的应用程序版本
        self.CreatorVersion = ''
        # 用户自定义元数据集合 子节点位CustomData
        self.CustomDatas = []
