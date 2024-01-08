import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

print(sopa.select("title")[0].getText())

columna_lateral = sopa.select(".sidebar-block")
print(columna_lateral)