import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    print("Truy cập thành công! Đang tiến hành bóc tách dữ liệu...\n")
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_list = []
    blocks = soup.find_all('div', class_='quote')
    
    for block in blocks:
        quote_text = block.find('span', class_='text').text
        author = block.find('small', class_='author').text
        quotes_list.append({
            'Tác giả': author,
            'Câu châm ngôn': quote_text
        })
    df_quotes = pd.DataFrame(quotes_list)
    
    print(df_quotes.head())
else:
    print(f"Lỗi truy cập! Mã lỗi: {response.status_code}")