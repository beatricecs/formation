import pathlib
import bs4
import datetime


class Page:
    def __init__(self, soup):
        self.soup = soup

class Field:
    def __init__(self, css_selector):
        self.css_selector = css_selector

class TextInput(Field):
    def __get__(self, instance, owner):
        element = instance.soup.select_one(self.css_selector)
        return element.text.strip()

class DateInput(TextInput):
    def __get__(self, instance, owner):
        value = super().__get__(instance, owner)
        return datetime.datetime.strptime(value, "%d/%m/%Y").date()

class BasolPage(Page):
    region = TextInput("span:nth-of-type(1)")
    departement = TextInput("span:nth-of-type(2)")
    number = TextInput("span:nth-of-type(3)")
    date = DateInput("span:nth-of-type(6)")
    author = TextInput("span:nth-of-type(7)")
    usual_name = TextInput("span:nth-of-type(9)")
    commune = TextInput("span:nth-of-type(10)")


content = pathlib.Path('/tmp/example.html').read_text()
soup = bs4.BeautifulSoup(content, 'html.parser')

page = BasolPage(soup)

print(page.region)
print(page.departement)
print(page.number)
print(page.date)
print(page.author)
print(page.usual_name)
print(page.commune)