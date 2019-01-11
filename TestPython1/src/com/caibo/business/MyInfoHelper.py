# -*- coding: utf-8 -*-
from com.caibo.api.Utils import Utils
from com.caibo.ui.MyInfoPage import MyInfoPage
from com.caibo.business.BaseHelper import BaseHelper
import time

class MyInfoHelper(BaseHelper):
    global driver

    def __init__(self):   
        pass
    
    def to_my_info(self,case_name,second):   #去我的个人信息页面   param:case_name-用例名称,second-截图等待秒数
        my_info_page = MyInfoPage()
        util=Utils()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_my_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_button).click()
        if(second>1):
            util.getImage(MyInfoHelper.driver, case_name, second)
        else :
            util.getImage(MyInfoHelper.driver, case_name, 1)
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_back_button).click()
        print("本次测试完成") 
        
    
    def edit_nickname_error(self,nick_name="",case_name="",second=0):   #修改昵称   param:case_name-用例名称,second-截图等待秒数
        my_info_page = MyInfoPage()
        util=Utils()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_my_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_nickname).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_nickname_input).click()
        if(nick_name==""):
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_savename_button).click()     
        else:
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_nickname_input).clear()
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_nickname_input).send_keys(nick_name)
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_savename_button).click()
            time.sleep(1)
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_mes_button).click()
            time.sleep(1)
        if(second>1):
            util.getImage(MyInfoHelper.driver, case_name, second)
        else :
            util.getImage(MyInfoHelper.driver, case_name, 0)
            
        util.tap(MyInfoHelper.driver, 28, 72, 56, 110)    #此处返回使用绝对坐标来点击,使用id会有获取不到元素异常
        time.sleep(1)
        util.tap(MyInfoHelper.driver, 28, 72, 56, 110) 
        #util.getElementById(MyInfoHelper.driver,my_info_page.resid_back_button).click()
        #MyInfoHelper.driver.find_element_by_xpath("//*[@resource-id='com.dbljoy.lottery:id/img_goback']").click()
        time.sleep(1)
        #util.getElementById(MyInfoHelper.driver,my_info_page.resid_back_button).click()
        #MyInfoHelper.driver.find_element_by_xpath("//*[@resource-id='com.dbljoy.lottery:id/img_goback']").click()
        print("本次测试完成") 
    def edit_nickname_right(self,nick_name="",case_name="",second=0):   #修改昵称   param:case_name-用例名称,second-截图等待秒数
        my_info_page = MyInfoPage()
        util=Utils()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_my_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_nickname).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_nickname_input).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_nickname_input).clear()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_nickname_input).send_keys(nick_name)
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_savename_button).click()
        if(second>1):
            util.getImage(MyInfoHelper.driver, case_name, second)
        else :
            util.getImage(MyInfoHelper.driver, case_name, 1)
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_back_button).click()
        time.sleep(1)
        print("本次测试完成") 
    def identity_relname(self,relname="",relcard="",case_name="",second=0):   #实名认证   param:relname-真实姓名,relcard-身份证号,case_name-用例名称,second-截图等待秒数
        my_info_page = MyInfoPage()
        util=Utils()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_my_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_identity).click()
        if(relname=="" and relcard==""):
            pass
        else :
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_identity_relname).click()
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_identity_relname).clear()
            util.getElementById(MyInfoHelper.driver,my_info_page.resid_identity_relname).send_keys(relname)
            if(relcard==""):
                pass
            else :
                util.getElementById(MyInfoHelper.driver,my_info_page.resid_identity_relcard).click()
                util.getElementById(MyInfoHelper.driver,my_info_page.resid_identity_relcard).clear()
                util.getElementById(MyInfoHelper.driver,my_info_page.resid_identity_relcard).send_keys(relcard)
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_identity_commit_button).click()
        if(second>1):
            util.getImage(MyInfoHelper.driver, case_name, second)
        else :
            util.getImage(MyInfoHelper.driver, case_name, 0)
        util.tap(MyInfoHelper.driver, 28, 72, 56, 110)    #此处返回使用绝对坐标来点击,使用id会有获取不到元素异常
        time.sleep(1)
        util.tap(MyInfoHelper.driver, 28, 72, 56, 110) 
        print("本次测试完成") 
        
    def get_code_by_mobile(self,mobile="",case_name,second=0):   #实名认证   param:mobile-手机号,case_name-用例名称,second-截图等待秒数
        my_info_page = MyInfoPage()
        util=Utils()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_my_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_button).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_myinfo_updatepwd).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_updatepwd_mobile).click()
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_updatepwd_mobile).send_keys(mobile)
        util.getElementById(MyInfoHelper.driver,my_info_page.resid_updatepwd_get_code_button).click()
        if(second>1):
            util.getImage(MyInfoHelper.driver, case_name, second)
        else :
            util.getImage(MyInfoHelper.driver, case_name, 1)
        util.tap(MyInfoHelper.driver, 28, 72, 56, 110)    #此处返回使用绝对坐标来点击,使用id会有获取不到元素异常
        time.sleep(1)
        util.tap(MyInfoHelper.driver, 28, 72, 56, 110) 
        print("本次测试完成") 





