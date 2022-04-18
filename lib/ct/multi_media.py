from st.loc import ST_Loc
# 多媒体
class CT_MultiMedia:
    def __init__(self,type:str,media_file:ST_Loc,format:str=''):
        """多媒体

        Args:
            type (str): 多媒体类型。支持位图图像、视频、音频三种多媒体类型
            media_file (ST_Loc): 指向OFD包内的多媒体文件的位置
            format (str, optional): 资源的格式。支持BMP、JPEG. PNG.TIFF及AVS等格式,其中TIFF格式不支持多页. Defaults to ''.
        """
        self.Type = type
        self.MediaFile = media_file
        self.Format = format
