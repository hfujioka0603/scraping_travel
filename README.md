# scraping_travel

概要：WEBスクレイピングによる、旅行サイト各社のキャンペーン情報の収集
目的：旅行業界におけるトレンドや需要期を定量的に把握することにより、クライアントへの施策提案材料とする。
対象サイト：トラベラーズナビ様
対象ページ：https://travelersnavi.com/coupon/category/waribiki/
対象ページ：最新1〜2ページ
対象箇所：キャンペーン見出しのタイトル・日付部分

補足：
・robot.txtの有無は確認済み。
 その上で対象サイトへのサーバー配慮としてページネーションインターバルは2秒としている。
・selenium、chromedriver、pandasはpipインストールが必要。
　その際、今回はpython3で実行するため、「pip3」にてインストールを行った。
　参考：
　https://www.haya-programming.com/entry/2018/09/09/202711#%E3%81%AA%E3%81%9C%E3%81%93%E3%81%AE%E5%AF%BE%E5%87%A6%E3%81%A7%E8%89%AF%E3%81%84%E3%81%AE
・chromedriverはブラウザのバージョンに合わせてpipする。
　参考：
　https://chromedriver.chromium.org/downloads/version-selection
　https://qiita.com/hanzawak/items/2ab4d2a333d6be6ac760
 
