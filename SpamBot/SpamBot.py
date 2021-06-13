from threading import Thread

from selenium import webdriver
from time import sleep
from random import randint
import multiprocessing
import random

class Bot():

    def __init__(self):
        self.spam('Текст')

    def spam(self, spam1):
        self.driver = webdriver.Chrome()
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc3Uq5ts0ywKhZDRMNCrxV5LGfY8pHV6b0timV5Uu3QRODpQA/viewform')
       #Нулевой вопрос
        chois = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label',
                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label',
                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[3]/label']
        self.driver.find_element_by_xpath(random.choice(chois)).click()
        sleep(2)
       #Первый вопрос
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label').click()
        # Второй вопрос
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]').click()
        # Третий вопрос
        self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]').click()
        # Третий вопрос
        username_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        username_input.send_keys(spam1)
        self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label').click()
        self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()


def main():
        Bot()

processss = []
for x in range(2):
    proccess = multiprocessing.Process(target=main())
    if __name__ == '__main__':
        processss.append(proccess)
        proccess.start()
        for proccess in processss:
            proccess.join()



