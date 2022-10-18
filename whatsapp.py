from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv

message_text="<3" # message you want to send 
# y = "😔".encode('utf-8')

# z = y.decode('utf-8')
# print(z)

# message_text = y

no_of_message=10 # no. of time you want the message to be send

# with open('nums.csv', newline='') as csvfile:
#     data = list(csv.reader(csvfile))
    # reader = csv.reader(csvfile)
    # data = [tuple(row) for row in reader]

mobile_no_list = [919839153053]

# for item in data[0][74:]:
#     item='91'+item
#     mobile_no_list.append(item)
# print(data[0])


# mobile_no_list=[919412028979, 919412972376] # list of phone number can be of any length

print(mobile_no_list)

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Chrome('./chromedriver')
driver.get("http://web.whatsapp.com")
sleep(10) #wait time to scan the code in second

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("Invailid Phone Number:"+str(phone_no))
for mobile_no in mobile_no_list:
    try:
        send_whatsapp_msg(mobile_no,message_text)

    except Exception as e:
        sleep(10)
        is_connected()
