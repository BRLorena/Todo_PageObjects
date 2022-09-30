from page_objects import Page

from .elements import Afazer, Fazendo, Pronto, Todo


class PageTodo(Page): # encapsular as paginas
  a_fazer = Afazer()
  fazendo = Fazendo()
  pronto = Pronto()
  todo = Todo()
