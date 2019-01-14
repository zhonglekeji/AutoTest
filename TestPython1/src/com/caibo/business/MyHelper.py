# -*- coding: utf-8 -*-
from com.caibo.api.Utils import Utils
from com.caibo.ui.MyPage import MyPage
from com.caibo.business.BaseHelper import BaseHelper
import time

class MyHelper(BaseHelper):
    global driver
    def __init__(self):
        pass
   
    # 手机号，密码，用例标题，秒数，driver的状态（1就进行第一次初始化，0就代表已初始化）
    # 手机号密码为空则不输入
    def to_my_page(self,case_name,second):
        try:
            time.sleep(second)
            my_page = MyPage()
            util=Utils()
            util.getElementById(MyHelper.driver,my_page.resid_my_button).click()
            if second>0 :
                util.getImage(MyHelper.driver, case_name, second)
            else:
                util.getImage(MyHelper.driver, case_name, second)
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError

    def to_exhibition_room(self,case_name,second):
        try:
            time.sleep(second)
            my_page = MyPage()
            util=Utils()
            util.getElementById(MyHelper.driver,my_page.resid_exhibitionRoom_button).click();
            print("点击大奖展厅完成")
            if second>0 :
                util.take_screenShot(MyHelper.driver,case_name,second)
            else:
                util.take_screenShot(MyHelper.driver,case_name,0)
        
            pass
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
    
    def clear_cache(self,case_name,second):
        try:
            time.sleep(second)
            my_page = MyPage()
            util=Utils()
            #点击清理缓存,会弹出确认框
            util.getElementById(MyHelper.driver,my_page.resid_clear_cache).click()
            if second>0 :
                util.take_screenShot(MyHelper.driver,case_name,second)
            else:
                util.take_screenShot(MyHelper.driver,case_name,0)
            #由于uiauto定位不到确认框元素,此处采用绝对定位
            #取消  128  680,245-744
            #确定  449  695,600 746
            #点击取消
            util.tap(MyHelper.driver, 128, 680, 245, 744)
            if second>0 :
                util.take_screenShot(MyHelper.driver,case_name,second)
            else:
                util.take_screenShot(MyHelper.driver,case_name,0)
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
        
        
