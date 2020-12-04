import gspread
from oauth2client.service_account import ServiceAccountCredentials
from csv import writer
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import random
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction

with open('gmailNames.txt') as file:
    names=file.read().split('\n')

def get_a_name():
    return random.choice(names),random.choice(names)

def writeCred(filename,data):
    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(data)

#Google Sheets
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name("cred.json",scope)
client = gspread.authorize(creds)
_filename="GmailCredentials"
client.open(_filename)
spreadsheet=client.open(_filename)
worksheet=spreadsheet.sheet1

#Browserstack
userName = "userName"
accessKey = "accessKey"
desired_cap = {
  'device': 'Google Pixel 3',
  'os_version': '9.0'
}
desired_cap['project'] = 'My First Project'
desired_cap['build'] = 'My First Build'
desired_cap['name'] = 'Bstack-[Python] Sample Test'
desired_cap['app'] = "bs://ddd88ab12e93d652e5aefdbc62896e2798a23763"

try:
    fName,lName = get_a_name()
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    Byear,Bday,Bmonth=str(random.randint(1970,2001)),str(random.randint(0,29)),random.choice(months)

    DOB=f"{Bday}/{Bmonth}/{Byear}"

    driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_cap)
    driver.find_element_by_xpath("//*[@text='SIGN IN']").click()


    driver.implicitly_wait(60)
    driver.find_element_by_xpath("//*[@resource-id='view_container']//android.widget.Spinner").click()

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//android.view.View//android.view.MenuItem[1]").click()

    driver.implicitly_wait(20)
    el=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View")

    el.click()
    sleep(2)

    actions = ActionChains(driver)
    actions.send_keys(fName)
    actions.perform()
    sleep(2)
    el=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View")
    el.click()
    sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(lName)
    actions.perform()


    driver.find_element_by_xpath("//*[@resource-id='collectNameNext']").click()

    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//*[@resource-id="month"]').click()


    driver.implicitly_wait(10)
    driver.find_element_by_xpath(f'//*[@text="{Bmonth}"]').click()

    driver.find_element_by_xpath('//*[@resource-id="day"]').click()


    actions = ActionChains(driver)
    actions.send_keys(Bday)
    actions.perform()
    driver.find_element_by_xpath('//*[@resource-id="year"]').click()

    actions = ActionChains(driver)
    actions.send_keys(Byear)
    actions.perform()

    driver.find_element_by_xpath('//*[@resource-id="gender"]').click()

    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@text="Male"]').click()

    driver.find_element_by_xpath("//*[@resource-id='birthdaygenderNext']").click()

    driver.implicitly_wait(30)
    rnd_email=driver.find_element_by_xpath("//*[@resource-id='selectionc0']")



    email_address=rnd_email.text

    rnd_email.click()

    driver.find_element_by_xpath("//*[@resource-id='next']").click()

    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@resource-id='passwd']").click()

    sleep(2)
    actions = ActionChains(driver)
    actions.send_keys('pa$$word')
    actions.perform()

    driver.find_element_by_xpath("//*[@resource-id='confirm-passwd']").click()
    sleep(2)
    actions = ActionChains(driver)
    actions.send_keys('pa$$word')
    actions.perform()

    driver.find_element_by_xpath("//*[@resource-id='createpasswordNext']").click()
    driver.implicitly_wait(30)

    driver.swipe(364,1843,434,460)



    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@text='Skip']").click()
    driver.implicitly_wait(30)


    # el=driver.find_element_by_xpath("//*[@resource-id='optIn']//parent::android.view.View//following-sibling::android.view.View")
    #
    # el.click()
    #
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@resource-id='next']").click()

    driver.implicitly_wait(30)
    driver.swipe(364,1843,434,460)
    driver.implicitly_wait(30)
    el=driver.find_element_by_xpath("//*[@resource-id='termsofserviceNext']")
    driver.scroll(el,driver.find_element_by_xpath('//*'))
    sleep(2)
    el.click()

    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@text="More"]').click()

    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@text="Accept"]').click()
    sleep(5)
    worksheet.append_row([email_address,'shoaib123@#',DOB])
    writeCred('gmailCreds.csv',[email_address,'shoaib123@#',DOB])


except Exception as e:
    print("Got Error:",e)
    pass #continue
finally:
    driver.quit()
