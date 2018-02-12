from selenium import webdriver

driver = webdriver.Chrome('/home/whikwon/Documents/chromedriver')

driver.implicitly_wait(2)

# login
driver.get('https://www.quantopian.com/signin')
driver.find_element_by_xpath('//*[@id="user_email"]').send_keys('whikwon@gmail.com')
driver.find_element_by_xpath('//*[@id="user_password"]').send_keys('rnjsgnl1!')
driver.find_element_by_xpath('//*[@id="login-button"]').click()

# move to lectures page 
driver.get('https://www.quantopian.com/lectures')
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/a[10]/div/span[1]').click()
driver.find_element_by_xpath('//*[@id="clone-notebook-button"]').click()
driver.find_element_by_xpath('//*[@id="download_ipynb"]').click()


