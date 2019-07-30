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