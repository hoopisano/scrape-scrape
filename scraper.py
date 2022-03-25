import bs4, requests

def getPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.abaproduct-price')
    return elems[0].text.strip()


price = getPrice('https://herringbonebooks.indielite.org/book/9781945051791')
print(f"The price of the Book is: {price}")
