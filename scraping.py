"""目録
概要：WEBスクレイピングによる、旅行サイト各社のキャンペーン情報の収集
目的：旅行業界におけるトレンドや需要期を定量的に把握することにより、クライアントへの施策提案材料とする。
対象サイト：トラベラーズナビ様
対象ページ：https://travelersnavi.com/coupon/category/waribiki/
対象ページ：最新1〜2ページ
対象箇所：キャンペーン見出しのタイトル・日付部分

補足：
robot.txtの有無は確認済み。
その上で対象サイトへのサーバー配慮としてページネーションインターバルは2秒としている。
"""

from selenium import webdriver
import chromedriver_binary
import time
import pandas as pd
import re

"""importについての補足/注意点
・selenium、chromedriver、pandasはpipインストールが必要。
　その際、今回はpython3で実行するため、「pip3」にてインストールを行った。
　参考：
　https://www.haya-programming.com/entry/2018/09/09/202711#%E3%81%AA%E3%81%9C%E3%81%93%E3%81%AE%E5%AF%BE%E5%87%A6%E3%81%A7%E8%89%AF%E3%81%84%E3%81%AE
・chromedriverはブラウザのバージョンに合わせてpipする。
　参考：
　https://chromedriver.chromium.org/downloads/version-selection
　https://qiita.com/hanzawak/items/2ab4d2a333d6be6ac760
"""

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