from abc import ABC


class PageElement(ABC):

  def __init__(self, webdriver, url=''):
    self.webdriver = webdriver
    self.url = url

  def find_element(self, locator):
    return self.webdriver.find_element(*locator)

  def find_elements(self, locator):
    return self.webdriver.find_elements(*locator)

  def open(self):
    self.webdriver.get(self.url)
