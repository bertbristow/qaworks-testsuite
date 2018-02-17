from selenium import webdriver


def test_contact_us():
	driver = webdriver.Firefox()
	driver.get('http://www.qaworks.com/contact-us/')

	driver.find_element_by_xpath('//input[@name="your-name"]').send_keys('j.Bloggs')
	driver.find_element_by_xpath('//input[@name="your-email"]').send_keys('j.Bloggs@qaworks.com')
	driver.find_element_by_xpath('//input[@name="your-company"]').send_keys('test automation')
	driver.find_element_by_xpath('//textarea[@name="your-message"]').send_keys('please contact me I want to find out more')
	driver.find_element_by_xpath('//input[@id="contact-us-send"]').click()


if __name__=='__main__':
	test_contact_us()
