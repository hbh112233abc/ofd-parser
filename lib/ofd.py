from typing import Union,List
from doc_body import DocBody
class OFD:
    def __init__(self,doc_body:Union[DocBody,List[DocBody]],version:str='1.0',doc_type='OFD'):
        self.Version = version
        assert doc_type in ('OFD', 'OFD-A'), "DocType must be OFD or OFD-A"
        self.DocType = doc_type
        if isinstance(doc_body,DocBody):
            doc_body = [doc_body]
        self.DocBodyList = doc_body

    def is_archive(self):
        return self.DocType == 'OFD-A'

    def set_archive(self):
        self.DocType = 'OFD-A'
