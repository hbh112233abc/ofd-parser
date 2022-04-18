from ct import CT_DocInfo
from st import ST_Loc
class DocBody:
    def __init__(self,doc_info:CT_DocInfo,doc_root:ST_Loc,versions=None,signatures:ST_Loc=None):
        self.DocInfo = doc_info
        self.DocRoot = doc_root
        self.Versions = versions
        self.Signatures = signatures
