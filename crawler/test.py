from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.naver.com')

driver.find_element_by_name("query").send_keys('위메프 굽네치킨')
driver.find_element_by_id("search_btn").click()
driver.find_element_by_xpath("//div[@class='detail']//div[@class='tit']//a[@href]").click()

sleep(20)

driver.get('http://search.wemakeprice.com/search?search_cate=top&search_keyword=%ED%98%84%EB%8C%80%EB%B0%B1%ED%99%94%EC%A0%90+%EC%83%81%ED%92%88%EA%B6%8C&_service=5&_type=3')
descs = driver.find_elements_by_xpath("//span[@class='link type03']//*//*//strong[@class='tit_desc']")


for desc in descs:
    try:
        if "교환권" in desc.text and "상품권" in desc.text:
            desc.click()
            driver.switch_to_window(driver.window_handles[2])
            print(driver.page_source.encode('utf-8'))
            conditions = driver.find_elements_by_xpath("//tbody//tr//td[@*]")
            print(conditions)
            for condition in conditions:
                print(condition.text)
    except:
        print("ERROR!, but pass!")
