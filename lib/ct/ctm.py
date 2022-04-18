import numpy as np
# 变换矩阵
class CT_CTM:
    def __init__(self, Ctm_String:str):
        Ctm_String = Ctm_String.split(' ')
        self.__CTM = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]], dtype = float)
        self.__CTM[0][0] = float(Ctm_String[0])
        self.__CTM[0][1] = float(Ctm_String[1])
        self.__CTM[1][0] = float(Ctm_String[2])
        self.__CTM[1][1] = float(Ctm_String[3])
        self.__CTM[2][0] = float(Ctm_String[4])
        self.__CTM[2][1] = float(Ctm_String[5])
