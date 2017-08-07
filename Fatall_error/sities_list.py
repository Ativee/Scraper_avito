import Fatall_error
from bs4 import BeautifulSoup

Fatall_error.point()

html = Fatall_error.point()
bsObj = BeautifulSoup(html, "html.parser")

h3 = bsObj.find_all('ul')
for i in h3:
    f = i.find_all('ul')

    print(len(f))


