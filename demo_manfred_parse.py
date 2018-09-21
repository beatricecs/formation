import pathlib
import bs4

content = pathlib.Path('/tmp/example.html').read_text()

soup = bs4.BeautifulSoup(content, 'html.parser')
result = soup.select_one("span:nth-of-type(1)")
print ('_____________________')
print(result.text)
result = soup.select_one("span:nth-of-type(2)")
print(result.text)
result = soup.select_one("span:nth-of-type(3)")
print(result.text.strip())
result = soup.select_one("span:nth-of-type(6)")
print(result.text.strip())
result = soup.select_one("span:nth-of-type(7)")
print(result.text.strip())
result = soup.select_one("span:nth-of-type(9)")
print(result.text.strip())

print ('_____________________')
