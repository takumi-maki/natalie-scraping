import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_today_info():
    url = "https://natalie.mu/owarai/news"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    list_df = pd.DataFrame(columns=['タイトル', '概要', 'スコア', '投稿時間'])
    
    
    for i in range(30):
        time = soup.select('.NA_card_date')[i].string
        #今日だけの情報を取得
        if ":" in time:
            title = soup.select('.NA_card_title')[i].string
            summary = soup.select('.NA_card_summary')[i].string
            score = int(soup.select('.NA_card_score')[i].string)
            
            tmp_se = pd.Series([title, summary, score, time], index=list_df.columns, name=i)
            list_df = list_df.append(tmp_se)


    list_df.to_csv('data.csv', index=True)            


if __name__ == '__main__':
    get_today_info()

