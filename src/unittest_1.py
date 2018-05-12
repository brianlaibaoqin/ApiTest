#! /usr/bin/env python
#coding=utf-8

import unittest 

from post_get_class_new import HttpRequestResponse



class TestAdd(unittest.TestCase):
    def setUp(self):
        print("我是setUp")
    
    def tearDown(self):
        print("我是teardown")


    def test_lhl(self):
        url = 'http://v.juhe.cn/laohuangli/d'
        params = {"key":"e711bc6362b3179f5a28de7fd3ee4ace","date":"2016-5-14"}
        http = HttpRequestResponse()
        response = http.get(url, params=params)
        #提取响应中的error_code字段进行对比
        self.assertEqual(response['error_code'], 0, msg="fail")
  
  
  
#TestSuite测试套件：就是组合测试case的，常用的方法是addTest
suite = unittest.TestSuite()
suite.addTest(TestAdd("test_lhl"))


#TextTestRunner测试执行，就是来执行我们的脚本，常用方法是run
#自动找test开头的进行运行 
runner = unittest.TextTestRunner()
runner.run(suite)

'''
每个Excel的执行定义一个函数并加入套件中
执行套件
'''
