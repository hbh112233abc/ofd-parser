from st.datetime import DateTime
# 有效期
class ValidPeriod:
    def __init__(self,start_date:DateTime=None,end_date:DateTime=None):
        """有效期
        即此文档允许访问的期限,其具体期限取决于开始日期和结束日期,其中开始日期不能晚于结束日期,并且开始日期和结束日期至少出现一个。当不设置开始日期时,代表不限定开始日期，当不设置结束日期时代表不限定结束日期;当此不设置此节点时，表示开始日期和结束日期均不受限

        Args:
            start_date (DateTime, optional): 开始日期. Defaults to None.
            end_date (DateTime, optional): 结束日期. Defaults to None.
        """
        self.StartDate = start_date
        self.EndDate = end_date
