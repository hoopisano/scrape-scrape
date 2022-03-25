import bs4, requests

# Download a webpage's HTML
res = requests.get('https://weather.com/weather/today/l/40.63,-74.02?par=google')
status = res.status_code    # Make sure it worked
print(status)

# Parse the HTML doc that was downloaded.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.select('.CurrentConditions--tempValue--3a50n') # Copy CSS Selector for the element you want
print(elems)                                                # Pass it into the .select() method.

elemsStripped = elems[0].text.strip()       # Access the inner HTML, which is
print(elemsStripped)                        # the text that appears on the webpage.
