import requests
from bs4 import BeautifulSoup


def get_dollar_course():
    """
    Get today's dollar course in rubles.

    According to National Central Bank of Russia.
    """
    url = 'https://www.cbr.ru/scripts/XML_daily.asp/'
    page = requests.get(url)

    # Use BeautifulSoup4 to parse
    soup = BeautifulSoup(page.text, 'xml')

    valutes = soup.find_all('Valute')

    for valute in valutes:
        if valute['ID'] == 'R01235':
            course = float(valute.find('Value').text.replace(',', '.'))
            return course