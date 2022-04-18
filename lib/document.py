from typing import List,Union
from st import ST_Loc
from ct import CT_Action,CT_Bookmark,CT_Permission,CT_VPreferences,CT_CommonData
from page import PageNode
from outline import Outline

class Document:
    def __init__(
        self,
        common_data:CT_CommonData,
        pages:List[PageNode],
        actions:List[CT_Action],
        bookmarks:List[CT_Bookmark],
        outlines:List[Outline] = [],
        permissions:List[CT_Permission]=[],
        v_preferences:CT_VPreferences=None,
        attachments:Union[ST_Loc,List[ST_Loc]] = None,
        annotations:Union[ST_Loc,List[ST_Loc]] = None,
        custom_tags:Union[ST_Loc,List[ST_Loc]] = None,
        extensions:Union[ST_Loc,List[ST_Loc]] = None
    ):
        """文档根节点

        Args:
            common_data (CommonData): 文档公共数据,定义了页面区域,公共资源等数据
            pages (List[Page]): 页树
            actions (List[CT_Action]): 动作序列,存在多个Action对象时,依次执行
            bookmarks (List[CT_Bookmark]): 书签集
            outlines (List[Outline], optional): 大纲. Defaults to [].
            permissions (List[CT_Permission], optional): 权限声明. Defaults to [].
            v_preferences (CT_VPreferences, optional): 视图首选项. Defaults to None.
            attachments (Union[ST_Loc | List[ST_Loc]], optional): 附件文件列表. Defaults to None.
            annotations (Union[ST_Loc | List[ST_Loc]], optional): 注释文件列表. Defaults to None.
            custom_tags (Union[ST_Loc | List[ST_Loc]], optional): 自定义标签文件列表. Defaults to None.
            extensions (Union[ST_Loc | List[ST_Loc]], optional): 扩展文件列表. Defaults to None.
        """
        self.CommonData = common_data
        self.Pages = pages
        self.Actions = actions
        self.Bookmarks = bookmarks
        self.Outlines = outlines
        self.Permissions = permissions
        self.VPreferences = v_preferences
        self.Attachments = attachments
        self.Annotations = annotations
        self.CustomTags = custom_tags
        self.Extensions = extensions
