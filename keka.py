'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Remote(
  desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)

browser.get("https://app.keka.com/Account/login")
time.sleep(10)
driver.save_screenshot('screen.png')
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("password")
username.send_keys("rishi.ambwani@myoperator.co")
password.send_keys("rishi@1234")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
driver.save_screenshot('screen.png')

'''
import calendar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from BeautifulSoup import BeautifulSoup
import requests
import json
import re
import datetime
def main():
    browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    #os.environ["webdriver.chrome.driver"] = chromedriver
    #browser = webdriver.Chrome(chromedriver)
    browser.get('https://app.keka.com/Account/login')

    username= browser.find_element_by_id("email")
    #password = selenium.find_element_by_id("password")

    username.send_keys("rishi.ambwani@myoperator.co")
    #password.send_keys("Pa55worD")
    login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    login_attempt.submit()

    browser.get('https://app.keka.com/Account/login')

    username= browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")

    username.send_keys("username")
    password.send_keys("pass")
    login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    login_attempt.submit()
    time.sleep(1)
    #r=requests.6et('https://myoperator.keka.com/api/mytime/attendance/summary')
    #print(json.dumps(r.text,indent=4))
    browser.get('https://myoperator.keka.com/#/me/attendance')
    #soup_level1=BeautifulSoup(browser.page_source)
    time.sleep(4)
    #print(soup_level1)
    #print(json.loads(soup_level1))
    l=[]
    t=[]
    #>>> k=re.findall(r'((\d|\d\d):\d\d) hrs$','9:38 hrs\n9:38 hrs\n0:11:53 late')
    #>>> k=re.findall(r'((\d|\d\d):\d\d) hrs$','9:40 hrs\n9:40 hrs')
    j=datetime.datetime.strftime(datetime.date.today(),'%d')
    j=int(j)
    count=1
    for td in browser.find_elements_by_xpath("//*[@class='attendance-view attendance-summary ng-scope']"):
        #print(td.text)
        if(count<=j):
            l.append(td.text.encode())
        count+=1
    def parse_time(s):
        hour, min = s.split(':')
        try:
            hour = int(hour)
            min = int(min)
        except ValueError:
            # handle errors here, but this isn't a bad default to ignore errors
            return 0
        return hour * 60 * 60 + min * 60



    #print(len(l))
    #print(l)
    c=0
    for i in l:
        print(i)
        k=re.findall(r'((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?)',i)
        #print(k,i)
        if(k!=[]):
            if(k[0]!='0:00'):
                t.append(k[0])
        else:
            c+=1

    #t=t[1:]
    print(c)
    print(t)
    s=0
    for j in t:
        s+=parse_time(j)

    print(s)
    s=s/float(3600)
    print(s)
    current_hrs=s
    s=s/float(len(t))
    avg_hrs=s
    print(s)
    now = datetime.datetime.now()
    d=calendar.monthrange(now.year, now.month)[1]

    year = int(datetime.datetime.strftime(datetime.date.today(),'%y'))
    month = int(datetime.datetime.strftime(datetime.date.today(),'%m'))
    day_to_count = calendar.SUNDAY

    matrix = calendar.monthcalendar(year,month)

    num_sun = sum(1 for x in matrix if x[day_to_count] != 0)
    '''year = int(datetime.datetime.strftime(datetime.date.today(),'%y'))
    month = int(datetime.datetime.strftime(datetime.date.today(),'%m'))
    day_to_count = calendar.SUNDAY

    matrix = calendar.monthcalendar(year,month)

    num_sat = sum(1 for x in matrix if x[day_to_count] != 0)'''

    total_holidays=2+num_sun
    total_workdays=d-total_holidays
    total_hrs=total_workdays*float(9)
    gross_hrsleft=(total_hrs-current_hrs)/float(total_workdays-len(t))
    hrs_left=total_hrs-current_hrs
    print("gross_hrsleft {}".format(gross_hrsleft))
    print(total_hrs)
    print(total_workdays)
    print(total_holidays)
    round(avg_hrs,2)
    gross_hrsleft=round(gross_hrsleft,2)
    browser.close()
    gross_hrsleft=str(gross_hrsleft)
    arr1=gross_hrsleft.split('.')
    return current_hrs,hrs_left,avg_hrs,gross_hrsleft,arr1

if __name__ == "__main__":
    print("in")
