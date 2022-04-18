from datetime import datetime
# 日期类型
class DateTime:
    def __init__(self,date:str):
        self.datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
