from selenium import webdriver
from re import findall
from time import sleep

class Ep_info(object):

    def __init__(self,html):
        self.html = html

    def bilibili_Ep_info(self):
        print('正在打开浏览器，请稍等...')
        driver = webdriver.Firefox()
        try:
            driver.get(self.html)
        except:
            print("打开浏览器这里出了问题")
            exit()
        sleep(5)
        Ep_info_rep = findall(r"bangumi.bilibili.com/anime/\d{2,}/play#\d{2,}",driver.page_source)
        Ep_info_list = []
        driver.close()
        print("浏览器正常关闭...")
        for i in Ep_info_rep:
            if i not in Ep_info_list:
                Ep_info_list.append(i)
        print("目前一共有"+str(len(Ep_info_list))+"集")
        return Ep_info_list
