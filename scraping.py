from selenium import webdriver
import chromedriver_binary
import time
import pandas as pd
import re

TITLE_LIST = []
DAY_LIST = []

browser = webdriver.Chrome()
for num in range(1,3):
    browser.get('https://travelersnavi.com/coupon/category/waribiki/page/{}'.format(num))
    
    main_articles = browser.find_element_by_tag_name('main')
    campaign_title = main_articles.find_elements_by_tag_name('h3')
    campaign_day = main_articles.find_elements_by_css_selector('.blog_info > p')
 
    for title in campaign_title:
        TITLE_LIST.append(title.text)
    for day in campaign_day:

        """cssセレクターによるpタグについての補足
        pタグのみで指定した場合、日付部分の後ろについているハッシュタグ情報まで抜きとってしまう。
        この部分は今回の収集では必要ないため、splitメソッドと正規表現を用いて日付情報のみを正しく取得。
        """
        nen = day.text.split('/')[0]
        tsuki = day.text.split('/')[1]
        hi = re.sub('\\D', '', day.text.split('/')[2])
        DAY_LIST.append(nen + '/' + tsuki + '/' +hi)
    time.sleep(2)

browser.close()

df = pd.DataFrame()

df['TITLE'] = TITLE_LIST
df['DAY'] = DAY_LIST

print(df)
df.to_csv('scraping_travel.csv',index=False)
