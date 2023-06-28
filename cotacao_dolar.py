
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

page = requests.get("https://www.google.com/search?q=cotacao+dolar&oq=cotacao&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDsyBggCEEUYOzIGCAMQRRg5MgkIBBAAGEMYigUyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyDQgIEAAYgwEYsQMYgAQyBwgJEAAYgATSAQc5MzVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8",headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

valor_dolar = soup.find_all("span",class_="DFlfde SwHCTb")[0]


df = pd.DataFrame(valor_dolar)

print(df)
