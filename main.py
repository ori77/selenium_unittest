import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		print("setup")  
		self.driver = webdriver.Chrome('C:\\webdrivers\\chromedriver\\chromedriver.exe')
		self.driver.get('http://www.python.org')
		self.driver.maximize_window() 
	
	##def test_example(self):
	##	print("Test")
	##	assert True
 
	##def test_title(self):
	##	mainPage = page.MainPage()
	##	assert mainPage.does_title_match()

	def test_search_python(self):
		mainPage = page.MainPage(self.driver)
		assert mainPage.does_title_match()
		mainPage.search_text_element = "pycon"
		mainPage.click_go_button()
		search_result_page = page.SearchResultPage(self.driver)
		assert search_result_page.are_results_found()

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()