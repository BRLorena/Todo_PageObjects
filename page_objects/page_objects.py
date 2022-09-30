import abc


class SeleniumObject:
  def find_element(self, locator):
    return self.webdriver.find_element(*locator)

  def find_elements(self, locator):
    return self.webdriver.find_elements(*locator)

class Page(abc.ABC, SeleniumObject): #Abstrata, deve saber coisas de selenium
  
  def __init__(self, webdriver, url=''):
    self.webdriver = webdriver
    self.url = url
    self._reflection()

  def open(self):
    self.webdriver.get(self.url)

  #buscar todos os PageElements
  def _reflection(self): 
    for atributo in dir(self): 
      attr_real = getattr(self, atributo)#pega o valor do atributo
      # verifica dentro da class qual atr. é PageElement
      if isinstance(attr_real,PageElement):
        attr_real.webdriver = self.webdriver

class PageElement(abc.ABC,SeleniumObject):
  def __init__(self, webdriver=None):
    self.webdriver = webdriver
