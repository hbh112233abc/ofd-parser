class CGTransform:
    def __init__(self):
        self.__CodePosition = 0
        #select ↓
        self.__CodeCount = 0
        self.__GlyphCount = 0
        self.__Glyphs = []

    def get_CodePosition(self):
        return self.__CodePosition
    def set_CodePosition(self, pos_string):
        self.__CodePosition = int(pos_string)

    def get_select_CodeCount(self):
        return self.__CodeCount
    def set_select_CodePosition(self, count_string):
        self.__CodeCount = int(count_string)

    def get_select_GlyphCount(self):
        return self.__GlyphCount
    def set_select_GlyphCount(self, count_string):
        self.__GlyphCount = int(count_string)

    def get_select_Glyphs(self):
        return self.__Glyphs
    def set_select_Glyphs(self, glyphs):
        self.__Glyphs = glyphs
