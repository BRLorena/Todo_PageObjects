from element import PageElement
from locator import Locator


class Todo(PageElement):

  name = Locator.NAME
  description = Locator.DESCRIPTION
  urgent = Locator.URGENT
  submit = Locator.SUBMIT

  def create_todo(self, name, description, urgent=False):
    self.webdriver.find_element(*self.name).send_keys(name)
    self.webdriver.find_element(*self.description).send_keys(description)
    if urgent:
      self.webdriver.find_element(*self.urgent).click()
    self.webdriver.find_element(*self.submit).click()

class AFazer(PageElement):

  fieldset = Locator.FIELDSET
  card = Locator.CARD

  def get_todos(self):
    cards = self.find_elements(self.card)
    return [Card(card) for card in cards] #Pythinic
    # po_cards = []
    # for card in cards:
    #   po_cards.append(Card(card))
    # print(po_cards)
    # return po_cards

class Card:

  def __init__(self,selenium_object):
    self.selenium_object = selenium_object
    self.name = Locator.CARD_NAME
    self.description = Locator.CARD_DESCRIPTION
    self.do = Locator.CARD_DO_BUTTON
    self.cancel = Locator.CARD_CANCEL_BUTTON
    self._load()

  def do(self):
    self.selenium_object.find_element(*self._do).click()

  def cancel(self):
    self.selenium_object.find_element(*self._cancel).click()

  def _load(self):
    self.name = self.selenium_object.find_element(*self.name).text
    self.description = self.selenium_object.find_element(*self.description).text

  def __repr__(self):
    return f'Card(name = "{self.name}", description = "{self.description}")'

# -----------------------------------------------------------------

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://selenium.dunossauro.live/todo_list.html'

todo_element = Todo(driver,url)
todo_element.open()

todo_element.create_todo(
  'Dormir',
  'Dormir é muito bom'
)

a_fazer = AFazer(driver,url)
todos = a_fazer.get_todos()
print(a_fazer.get_todos())
# pega o primeiro card da lista e executa a func. do()
todos[0].do()

