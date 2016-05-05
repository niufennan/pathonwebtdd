# -*-coding:utf8-*-

import sys
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(StaticLiveServerTestCase):
	
	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if "liveserver" in arg:
				cls.server_url="http://"+arg.split("=")[1]
				return
		super().setUpClass()
		cls.server_url=cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url==cls.live_server_url:
			super().tearDownClass()



	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(13)
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self,row_text):
		table=self.browser.find_element_by_id("id_list_table")
		rows=table.find_elements_by_tag_name("tr")
		self.assertIn(row_text,[row.text for row in rows])

	def test_layout_and_styling(self):
		#伊迪斯访问首页
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024,786)
		#他看到输入框完美的剧中显示
		inputbox=self.browser.find_element_by_id("id_new_item")

		self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta=5)



	def test_can_start_a_list_and_retrivev_it_later(self):
		#伊利斯听说有一个很酷的在线代办事项应用
		#她去看了看这个应用的首页
		self.browser.get(self.server_url)

		#她注意到网页的标题和头部都包含”To-Do“这个词
		self.assertIn( "To-Do", self.browser.title)# , "Browser title was" +browser.title
		header_text=self.browser.find_element_by_tag_name("h1").text
		self.assertIn("To-Do",header_text)

		#应用邀请她输入一个待办事项
		inputbox=self.browser.find_element_by_id("id_new_item")
		self.assertEqual(inputbox.get_attribute("placeholder"),"Enter a to-do item")


		#她在一个文本框中输入了 “Buy peacock feathers”
		#伊利斯的爱好是使用假蝇做鱼饵钓鱼
		inputbox.send_keys("Buy peacock feathers")

		#她按回车后，页面更新了
		#待办事项表格中显示了 “1 Buy peacock feathers”
		inputbox.send_keys(Keys.ENTER)
		
		edith_list_url=self.browser.current_url


		self.assertRegex(edith_list_url,"/lists/.+")

		self.check_for_row_in_list_table("1: Buy peacock feathers")


		#页面中有显示了一个文本框 可以输入其他的待办事项
		#她输入了“Use peacock feathers to make a fly”
		#伊迪斯做事很有条例
		inputbox=self.browser.find_element_by_id("id_new_item")
		#伊利斯的爱好是使用假蝇做鱼饵钓鱼
		inputbox.send_keys("Use peacock feathers to make a fly")

		#她按回车后，页面更新了
		#待办事项表格中显示了 “1 Buy peacock feathers”
		inputbox.send_keys(Keys.ENTER)
		#页面再次更新，他的清单中显示了两个待办事项
		self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
		self.check_for_row_in_list_table("1: Buy peacock feathers")
		


		#现在一个叫弗朗西斯的访问首页
		##我们使用一个新浏览器会话
		##确保伊迪斯的信息不回从cookie中泄露出来
		self.browser.quit()
		self.browser=webdriver.Firefox()

		#弗朗西斯访问首页
		#页面中看不到伊迪斯的清单
		self.browser.get(self.server_url)
		page_text=self.browser.find_element_by_tag_name("body").text
		self.assertNotIn("Buy peacock feathers", page_text)
		self.assertNotIn("make a fly",page_text)

		#弗朗西斯输入了一个新待办事项 新建一个清单
		#他不像伊迪斯那样兴趣盎然
		inputbox=self.browser.find_element_by_id("id_new_item")
		inputbox.send_keys("Buy milk")
		inputbox.send_keys(Keys.ENTER)

		#弗朗西斯获得了唯一的URL
		francis_list_url=self.browser.current_url
		self.assertRegex(francis_list_url,"/lists/.+")
		self.assertNotEqual(francis_list_url,edith_list_url)

		#这个页面还是没有伊迪斯的清单
		page_text=self.browser.find_element_by_tag_name("body").text
		self.assertNotIn("Buy peacock feathers",page_text)

		self.assertIn("Buy milk",page_text)

		#两个人都很满意 睡觉去啦 
		#end
	

		


		#伊迪斯想知道这个网站是否会记住他的清单

		#他看到网站为他生成了一个唯一的url

		#self.fail("Finish the test!")
		#并且页面中有一些文字解说这个功能

		#她房屋这个url 发现他的待办事项列表还在

		#她很满意 去睡觉了

		#browser.quit()

