# -*-coding:utf8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	"""docstring for NewVisitorTest"""
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(13)
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrivev_it_later(self):
		#伊利斯听说有一个很酷的在线代办事项应用
		#她去看了看这个应用的首页
		self.browser.get("http://localhost:8000")

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

		table=self.browser.find_element_by_id("id_list_table")
		rows=table.find_elements_by_tag_name("tr")
		self.assertTrue(any(row.text=="1:Buy peacock feathers" for row in rows),"New to-do item did not appear in table")

		#页面中有显示了一个文本框 可以输入其他的待办事项
		#她输入了“Use peacock feathers to make a fly”
		#伊迪斯做事很有条例
		self.fail("FInish the test!")

		#页面再次更新，他的清单中显示了两个待办事项

		#伊迪斯想知道这个网站是否会记住他的清单

		#他看到网站为他生成了一个唯一的url
		#并且页面中有一些文字解说这个功能

		#她房屋这个url 发现他的待办事项列表还在

		#她很满意 去睡觉了

		#browser.quit()

if __name__ =="__main__":
	unittest.main(warnings="ignore")

