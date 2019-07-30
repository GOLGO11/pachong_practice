import logging
import time

from common.utils import url, driver, switch_handle, xpath2, xpath1


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
    # 文件下载路径为chrome浏览器指定路径
    time.sleep(10000)
    logging.info('爬取成功')


spider()
