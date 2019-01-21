# coding: utf-8
import datetime,unittest
import sys
sys.getdefaultencoding()
print(sys.path)
import os
os.chdir('/Users/lipengjie/eclipse-workspace/TestPython1')
for file in os.listdir(os.getcwd()):
    print(file)
sys.path.append('/Users/lipengjie/eclipse-workspace/TestPython1')
sys.path.append('/Users/lipengjie/eclipse-workspace/TestPython1/src')
sys.path.append('/Users/lipengjie/eclipse-workspace/TestPython1/src/com/caibo/case')
sys.path.append('/Users/lipengjie/eclipse-workspace/TestPython1/src/com/caibo/api')
from com.caibo.api.Utils import Utils
from com.caibo.api.HTMLTestRunner import HTMLTestRunner





case_path=os.getcwd();
now_time = datetime.datetime.now().strftime('%Y_%m_%d')  #当前日期,每天的报告放在每天的文件夹下
a = 'hello word'
b = a.replace('word','python')
temp_report_path=os.getcwd()
temp2_report_path=temp_report_path.replace('case','')
report_path = temp2_report_path+"report"+"/"+now_time # 存放报告路径
utils = Utils()
utils.mkdir(report_path)  #创建测试报告目录
utils.mkdir(temp2_report_path+"screenShots"+"/"+now_time)  #创建截图目录


def creat_suite():
    uit = unittest.TestSuite()

    # 获取所有以test开头.py结尾的测试用例文件
    #discover = unittest.defaultTestLoader.discover(case_path, pattern="Test_*.py", top_level_dir=None)
    discover = unittest.defaultTestLoader.discover('/Users/lipengjie/eclipse-workspace/TestPython1/src/com/caibo/case', pattern="Test_*.py", top_level_dir=None)
    print(discover)
    # print (discover)
    # 遍历并执行每一个测试用例
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
            #print(test_case)
    return uit


# 执行测试
if __name__ == "__main__":
    suite = creat_suite()
    fb = open(r'/Users/lipengjie/eclipse-workspace/TestPython1/src/com/caibo/report/'+now_time+'/result.html', 'wb')
    runner = HTMLTestRunner(stream=fb, title=u'彩播app自动化测试报告', description=u'项目描述：Android环境')
    runner.run(suite)
    fb.close()
    
    
    