# -*- coding: utf-8 -*-
from com.caibo.api.Utils import Utils
from com.caibo.ui.MyInfoPage import MyInfoPage
from com.caibo.business.BaseHelper import BaseHelper
from com.caibo.ui.CashWithdrawalPage import CashWithdrawalPage

class CashWithDrawalHelper(BaseHelper):
    global driver

    def __init__(self):   
        pass
   
    # 手机号，密码，用例标题，秒数，driver的状态（1就进行第一次初始化，0就代表已初始化）
    # 手机号密码为空则不输入

    def to_cash_with_drawl(self,case_name):
        try:
            cash_with_drawl_page = CashWithdrawalPage()
            util=Utils()
            util.getElementById(CashWithDrawalHelper.driver,cash_with_drawl_page.resid_my_record).click()
            util.take_screenShot(CashWithDrawalHelper.driver, case_name, 2)
            util.getElementById(CashWithDrawalHelper.driver,cash_with_drawl_page.resid_back_button).click()
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError