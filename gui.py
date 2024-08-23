from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("todos.txt"),
                      key='todosListItem',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))
# this .read() will actually display it in the command line
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todosListItem'])
    match event:
        case 'Add':
            todos = functions.get_todos("todos.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos, "todos.txt")
            window['todosListItem'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todosListItem'][0]
            new_todo = values['todo']

            todos = functions.get_todos("todos.txt")
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos, "todos.txt")
            window['todosListItem'].update(values=todos)
        case 'todosListItem':
            window['todo'].update(value=values['todosListItem'][0])
        case sg.WIN_CLOSED:
            break

window.close()
