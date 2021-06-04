from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from getpass import getpass
import time
import sys

print("Are you ready to fill out your timesheet?")

username = input("Username: ")
pwd = getpass()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://myte.accenture.com/OGTE/dashboard/DashboardPage.aspx")

try:
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
    login.send_keys(str(username))
    # login.send_keys('YOUR USERNAME')
    login.send_keys(Keys.RETURN)

    pw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwordInput"))
    )
    pw.send_keys(str(pwd))
    # pw.send_keys('YOUR PASSWORD')
    pw.send_keys(Keys.RETURN)

    skip = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "vipSkipBtn"))
    )
    skip.click()

    sign = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    sign.click()

    timesheet = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "TimeButton_HyperLink"))
    )
    timesheet.click()

    workinghours = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "WorkingHoursMenuLink"))
    )
    workinghours.click()

    #Switch to iframe of Working Hours table
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("DynamicPopupIframe"))

    mytable = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry"))
    )

    rowcount = 0
    rowarray = []
    for row in mytable.find_elements_by_css_selector("tr"):
        rowcount = int(rowcount) + 1
        if rowcount < 10:
            rowcount = "0" + str(rowcount)
        else:
            rowcount = str(rowcount)

        tds = row.find_elements_by_css_selector("td")

        if tds:
            if "Mon" in tds[0].text:
                for td in tds:
                    if td.get_attribute("headers") == "workingHourGridThId_1":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_StartWorkTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_StartWorkTimeMinuteDropDown"))
                        hours.select_by_value('12 PM')
                        minutes.select_by_value('00')
                    elif td.get_attribute("headers") == "workingHourGridThId_2":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_EndWorkTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_EndWorkTimeMinuteDropDown"))
                        hours.select_by_value('06 PM')
                        minutes.select_by_value('00')
                    elif td.get_attribute("headers") == "workingHourGridThId_5":
                        mealbreak = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_MealBreakReasonDropDown"))
                        mealbreak.select_by_value("I took my meal break or a meal break is not required.")
            elif 'Tue' in tds[0].text or 'Wed' in tds[0].text or 'Thu' in tds[0].text:
                for td in tds:
                    if td.get_attribute("headers") == "workingHourGridThId_1":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_StartWorkTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_StartWorkTimeMinuteDropDown"))
                        hours.select_by_value('08 AM')
                        minutes.select_by_value('00')
                    elif td.get_attribute("headers") == "workingHourGridThId_2":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_EndWorkTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_EndWorkTimeMinuteDropDown"))
                        hours.select_by_value('12 PM')
                        minutes.select_by_value('00')
                    elif td.get_attribute("headers") == "workingHourGridThId_3":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_MealStartTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_MealStartTimeMinuteDropDown"))
                        hours.select_by_value('12 PM')
                        minutes.select_by_value('00')
                    elif td.get_attribute("headers") == "workingHourGridThId_4":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_MealEndTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_MealEndTimeMinuteDropDown"))
                        hours.select_by_value('12 PM')
                        minutes.select_by_value('30')
                    elif td.get_attribute("headers") == "workingHourGridThId_5":
                        mealbreak = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_MealBreakReasonDropDown"))
                        mealbreak.select_by_value("I took my meal break or a meal break is not required.")
                    elif td.get_attribute("headers") == "workingHourGridThId_6":
                        rowarray.append(rowcount)
            elif "Fri" in tds[0].text:
                for td in tds:
                    if td.get_attribute("headers") == "workingHourGridThId_1":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_StartWorkTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_StartWorkTimeMinuteDropDown"))
                        hours.select_by_value('08 AM')
                        minutes.select_by_value('00')
                    elif td.get_attribute("headers") == "workingHourGridThId_2":
                        hours = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_EndWorkTimeDropDown"))
                        minutes = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_EndWorkTimeMinuteDropDown"))
                        hours.select_by_value('12 PM')
                        minutes.select_by_value('00')
                    elif td.get_attribute("headers") == "workingHourGridThId_5":
                        mealbreak = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + rowcount + "_MealBreakReasonDropDown"))
                        mealbreak.select_by_value("I took my meal break or a meal break is not required.")

    #Add and fill in rows for Tue, Wed, Thur
    count = 0
    for click in rowarray:
        click = int(click) + count
        count = count + 1
        time.sleep(1)
        try:
            clickme = driver.find_element_by_xpath('//*[@id="ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry"]/tbody/tr[' + str(click) + ']/td[7]/input')
            clickme.click()
            time.sleep(1)

            nextrow = click + 1
            if nextrow < 10:
                nextrow = "0" + str(nextrow)
            else:
                nextrow = str(nextrow)

            starthours = Select(driver.find_element_by_xpath('//*[@id="ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl' + str(nextrow) + '_StartWorkTimeDropDown"]'))
            startminutes = Select(driver.find_element_by_xpath('//*[@id="ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl' + str(nextrow) + '_StartWorkTimeMinuteDropDown"]'))
            starthours.select_by_value('12 PM')
            startminutes.select_by_value('30')

            endhours = Select(driver.find_element_by_xpath('//*[@id="ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl' + str(nextrow) + '_EndWorkTimeDropDown"]'))
            endminutes = Select(driver.find_element_by_xpath('//*[@id="ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl' + str(nextrow) + '_EndWorkTimeMinuteDropDown"]'))
            endhours.select_by_value('06 PM')
            endminutes.select_by_value('30')

            mealbreak = Select(driver.find_element_by_id("ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl" + str(nextrow) + "_MealBreakReasonDropDown"))
            mealbreak.select_by_value("I took my meal break or a meal break is not required.")
        except StaleElementReferenceException:
            break

    # Once all your stuff is done with this frame need to switch back to default
    driver.switch_to.default_content()

except:
    print("Unexpected error: ", sys.exc_info())
    # driver.quit()