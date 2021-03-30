#!/usr/bin/env python

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()  #Give the path of Chrome driver    
driver.maximize_window()                        
driver.get('https://web.whatsapp.com/')

print("Welcome Mr \\xnone")

if __name__ == "__main__":
    while True:
        input('Enter anything after scanning QR code..  Hit ENTER to start')

        names = []  
        na=input("Enter your Target's name: ")
        cap=na.title()                                      
        names.extend(cap.split(","))                         
        msg = str(input("Enter your message: "))
	#msg = str("")
        count = int(input("How many times: "))
        for name in names:
            user = driver.find_element_by_xpath(f'//span[@title = "{name}"]').click()

        sleep(2)
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_xpath('//button[@class="_1U1xa"]').click()
            print("SEND \""+msg+"\" ("+str(i)+ " From "+str(count)+")")

