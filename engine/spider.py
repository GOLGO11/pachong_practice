import logging
import time

from selenium import webdriver

# 封面定位
xpath1 = [
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[1]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[2]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[3]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[4]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[5]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[6]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[7]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[8]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[9]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[10]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[11]/div[1]/a/img',
    '//*[@id="bodywrap"]/div[2]/div[1]/ul/li[12]/div[1]/a/img',

]

# 下一页
xpath2 = [
    '//*[@id="bodywrap"]/div[2]/div[2]/div/span[2]/a',
    '//*[@id="bodywrap"]/div[2]/div[2]/div/span[3]/a',
    '//*[@id="bodywrap"]/div[2]/div[2]/div/span[3]/a',
    '//*[@id="bodywrap"]/div[2]/div[2]/div/span[3]/a',
    '//*[@id="bodywrap"]/div[2]/div[2]/div/span[3]/a',
    '//*[@id="bodywrap"]/div[2]/div[2]/div/span[3]/a',

]

url = [
    'https://wnacg.org/albums-index-page-1-sname-%E8%84%9A.html',
    'https://wnacg.org/albums-index-page-2-sname-%E8%84%9A.html',
    'https://wnacg.org/albums-index-page-3-sname-%E8%84%9A.html',
    'https://wnacg.org/albums-index-page-4-sname-%E8%84%9A.html',
    'https://wnacg.org/albums-index-page-5-sname-%E8%84%9A.html',
    'https://wnacg.org/albums-index-page-6-sname-%E8%84%9A.html',
    'https://wnacg.org/albums-index-page-7-sname-%E8%84%9A.html',
]
driver = webdriver.Chrome()


def switch_handle():
    window = driver.current_window_handle
    all_window = driver.window_handles
    for i in all_window:
        if i != window:
            driver.switch_to.window(all_window[i])


def spider():
    # 爬取关键字查询之后的所有结果
    driver.get(url[0])
    # 爬取策略为：1.点击图片进入详情页，在详情页点下载进入下载页，在下载页点击下载按钮。
    for n in range(0, 6, 1):
        for number in range(0, 12, 1):
            driver.find_element('xpath', xpath1[number]).click()
            # 切换句柄, 获取当前句柄，如果不是最新句柄则切换到最新句柄
            switch_handle()
            driver.find_element('xpath', '//*[@id="bodywrap"]/div/div[1]/a[2]').click()
            time.sleep(3)
            switch_handle()
            driver.find_element('xpath', '/html/body/div[2]/div[2]/div/a[1]/span').click()
            time.sleep(3)
            driver.get(url[n])
            switch_handle()
            time.sleep(2)
        driver.find_element('xpath', xpath2[n]).click()
    time.sleep(10000)
    logging.info('爬取成功')


foot()
