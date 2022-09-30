from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.pages import PageTodo

browser = webdriver.Chrome(ChromeDriverManager().install())

# Arrange ---------------------------------------------------------
todo_page = PageTodo(browser, 'https://selenium.dunossauro.live/todo_list.html')
todo_page.open()


# Act --------------------------------------------------------------
todo_page.todo.create_todo(
  'Fazer a aula', 
  'Selenium aula PO'
  )

todo_page.todo.create_todo(
  'Criado pelo PageElement',
  'UHULLL'
)

# Assert -----------------------------------------------------------
first_todo = todo_page.a_fazer.todos()[0]
second_todo = todo_page.a_fazer.todos()[1]
assert first_todo.name == 'Fazer a aula'
assert second_todo.description == 'UHULLL'

browser.quit()
