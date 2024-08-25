from modules import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkTeal12")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("todos.txt"),
                      key='todosListItem',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   font=('Helvetica', 20))
# this .read() will actually display it in the command line
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos("todos.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos, "todos.txt")
            window['todosListItem'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todosListItem'][0]
                new_todo = values['todo']

                todos = functions.get_todos("todos.txt")
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos, "todos.txt")
                window['todosListItem'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case 'Complete':
            try:
                todo_to_complete = values['todosListItem'][0]
                todos = functions.get_todos("todos.txt")
                todos.remove(todo_to_complete)
                functions.write_todos(todos, "todos.txt")
                window['todosListItem'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todosListItem':
            window['todo'].update(value=values['todosListItem'][0])
        case sg.WIN_CLOSED:
            break

window.close()
