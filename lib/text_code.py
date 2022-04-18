class TextCode:
    def __init__(self):
        self.__TextValue = ''
        #select ↓
        self.__X = ''
        self.__Y = ''
        self.__DeltaX = []
        self.__DeltaY = []

    def get_TextValue(self):
        return self.__TextValue
    def set_TextValue(self, textvalue):
        self.__TextValue = textvalue

    def get_select_X(self):
        return self.__X
    def set_select_X(self, x):
        self.__X = float(x)

    def get_select_Y(self):
        return self.__Y
    def set_select_Y(self, y):
        self.__Y = float(y)

    def get_select_DeltaX(self):
        return self.__DeltaX
    def set_select_DeltaX(self, deltax):
        self.__DeltaX.append(int(num) for num in deltax.split(' '))

    def get_select_DeltaY(self):
        return self.__DeltaY
    def set_select_DeltaY(self, deltay):
        self.__DeltaY.append(int(num) for num in deltay.split(' '))
