import abc

from page_objects import PageElement
from selenium.common.exceptions import NoSuchElementException as exceptElement

from .locator import Locator


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

  @property
  def todos(self):
    cards = self.find_elements(self.card)
    # return [Card(card) for card in cards] #Pythinic
    po_cards = []
    for card in cards:
      po_cards.append(Card(card))
    return po_cards

class Afazer(CardContainer):

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
