from modules import functions
import time

# this is a multi line text
text = """
Principles of productivity:
Managing your inflow.
Systemizing everything that repeat
"""

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", current_time)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # The with context manager makes it, so you don't have to manual close the file
        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = []
        # for item in todos:
        #    new_item = item.strip('\n')
        #    new_todos.append(new_item)

        # list comprehension for modifying items of a list:
        #  new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            todos = functions.get_todos()

            newTodo = input("What do you want it to be: ")
            todos[number] = newTodo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            # the continue statement runs another iteration of the while loop
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action[0:5].startswith('exit'):
        print("Bye!")
        break
    else:
        print("Command is not valid.")
