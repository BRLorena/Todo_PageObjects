from selenium.webdriver.common.by import By


class Locator():

  NAME = (By.ID, "todo-name")
  DESCRIPTION = (By.ID, "todo-desc")
  URGENT = (By.ID, "todo-next")
  SUBMIT = (By.ID, "todo-submit")

  #AFazer 
  FIELDSET = (By.CSS_SELECTOR, "div.body_a fieldset")
  CARD = (By.CLASS_NAME, "terminal-card")

  #Card
  CARD_NAME = (By.CSS_SELECTOR, "header.name")
  CARD_DESCRIPTION = (By.CSS_SELECTOR, "div.description")
  CARD_DO_BUTTON = (By.CSS_SELECTOR, "button.do")
  CARD_CANCEL_BUTTON = (By.CSS_SELECTOR, "button.cancel")