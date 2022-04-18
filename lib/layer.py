class Layer:
    def __init__(self):
        self.__LayerId = ''
        self.__PageBlock = CT_PageBlock()

    def get_LayerId(self):
        return self.__LayerId
    def set_LayerId(self, layerid):
        self.__LayerId = layerid

    def get_PageBlock(self):
        return self.__PageBlock
    def set_PageBlock(self, pageblock):
        self.__PageBlock = pageblock
