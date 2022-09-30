import abc

from selenium.common.exceptions import NoSuchElementException as exceptElement

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

class CardContainer(PageElement, abc.ABC):

  def todos(self):
    cards = self.find_elements(self.card)
    # return [Card(card) for card in cards] #Pythinic
    po_cards = []
    for card in cards:
      po_cards.append(Card(card))
    return po_cards

class AFazer(CardContainer):

  fieldset = Locator.FIELDSET
  card = Locator.CARD

class Fazendo(CardContainer):

  fieldset = Locator.FIELDSET_B
  card = Locator.CARD

class Pronto(CardContainer):

  fieldset = Locator.FIELDSET_C
  card = Locator.CARD

class Card:

  def __init__(self,selenium_object):
    self.selenium_object = selenium_object
    self.name = Locator.CARD_NAME
    self.description = Locator.CARD_DESCRIPTION
    self.do = Locator.CARD_DO_BUTTON
    self.cancel = Locator.CARD_CANCEL_BUTTON
    self.refazer = Locator.CARD_REFAZER_BUTTON
    self._load()

  def click_do(self):
    self.selenium_object.find_element(*self.do).click()

  def click_cancel(self):
    try:
      self.selenium_object.find_element(*self.cancel).click()
    except exceptElement:
      print('Elemento não tem botão cancelar, click em Refazer')
      self.selenium_object.find_element(*self.refazer).click()

  
  def _load(self):
    self.name = self.selenium_object.find_element(*self.name).text
    self.description = self.selenium_object.find_element(*self.description).text

  def __repr__(self):
    return f'Card(name ="{self.name}", description = "{self.description}")'

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
todos = a_fazer.todos()
# print(a_fazer.todos())

# pega o primeiro card da lista e clica em Fazer ou cancel. 
todos[0].click_do()

fazendo = Fazendo(driver)
todos[0].click_do() # move P/ Pronto

pronto = Pronto(driver)
# print(pronto.todos())
todos[0].click_cancel() # click em refazer 







