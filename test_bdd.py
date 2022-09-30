from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.pages import PageTodo

browser = webdriver.Chrome(ChromeDriverManager().install())

"""
Scenario: Criar Cartão

  Dado que esteja na pagina Todo
  Quando criar um todo
  Então o cartão deve estar na pilha "A fazer"
"""


todo_page = PageTodo(browser, 'https://selenium.dunossauro.live/todo_list.html')
todo_page.open()
print('Dado que esteja na pagina Todo')

print('Quando criar um todo')
todo_page.todo.create_todo(
  'Fazer a aula', 
  'Selenium aula PO'
  )

todo_page.todo.create_todo(
  'Criado pelo PageElement',
  'UHULLL'
)

print('Então o cartão deve estar na pilha A fazer')
first_todo = todo_page.a_fazer.todos[0]
second_todo = todo_page.a_fazer.todos[1]
assert first_todo.name == 'Fazer a aula'
assert second_todo.description == 'UHULLL'

print("----"*20)

"""
Scenario: Mover Cartões para Fazendo

  Dado que esteja na pagina Todo
  Quando tiver um todo criado
  e clicar Fazer
  Então o cartão deve estar na pilha "Fazendo"
"""
print('Dado que esteja na pagina Todo')

print('Quando tiver um todo Criado e clicar Fazer')
first_fazendo = todo_page.a_fazer.todos[0]
first_fazendo.click_do()
sec_fazendo = todo_page.a_fazer.todos[0]
sec_fazendo.click_do()

print('Então o cartão deve estar na pilha Fazendo')
assert first_fazendo.name == 'Fazer a aula'
assert sec_fazendo.description == 'UHULLL'

browser.quit()
