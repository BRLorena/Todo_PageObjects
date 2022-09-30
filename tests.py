from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.elements import Todo
from pages.pages import PageTodo

browser = webdriver.Chrome(ChromeDriverManager().install())

page = PageTodo(browser, 'https://selenium.dunossauro.live/todo_list.html')

page.open()

page.todo.create_todo(
  'Fazer a aula', 
  'Selenium aula PO'
  )

todo = Todo(browser)
todo.create_todo(
  'Criado pelo PageElement',
  'UHULLL'
)

print(page.a_fazer.todos())
