from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = "https://qa-test.avenuecode.com/users/sign_in"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        #driver.find_element(By.XPATH,"//a[@href='/users/sign_in]").click()
        driver.find_element_by_id("user_email").send_keys("marcocelone16@gmail.com")
        driver.find_element_by_id("user_password").send_keys("avenuecode001")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_xpath("//a[@href='/tasks']").click()
        driver.implicitly_wait(3)


        #elementList = driver.find_elements(
       #     By.XPATH, "//table[@class='table']/tbody/tr")
       # size = len(elementList)
       # print("Size of the list: " + str(size))

        #driver.find_element_by_id("new_task").send_keys("test")
        #driver.find_element_by_xpath("//div[@class='input-group']//span[@class='input-group-addon glyphicon glyphicon-plus']").click()
        #time.sleep(2)

        elementList1 = driver.find_element(
            By.XPATH, "//button[@class='btn btn-xs btn-primary ng-binding']")
        size1 = elementList1.text
        print(size1)
        size2 = int("".join(filter(str.isdigit,size1)))
        print(size2)

        print("Size1 of the list: " +str(size1) )

        #assert size1 != size +1

        """
        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)
                """

ff = WorkingWithElementsList()
ff.testListOfElements()