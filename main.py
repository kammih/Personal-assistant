class PersonalAssistant:

  def __init__(self):
    self.contacts = {
      'Rubi': 'Marketing Coordinator', 'Tyler':
      'Software Developer', 'Truitt': 'Sales Representative'
    }
    self.todos = []
 
  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

    
  def get_todos(self):
    return self.todos
  

  def get_birthday(self, name):
    if name == "Rubi":
      return "Birthday is 03/13/23!"
    elif name == "Tyler":
      return "Birthday is 01/03/95!"
    elif name == "Truitt":
      return "Birthday is 01/06/25!"
    else:
      return "Can't find birthday for this person..."
  
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name!"



assistant = PersonalAssistant()
assistant.add_todo("Pick up groceries")
assistant.add_todo("Schedule meeting for next week")
print(assistant.get_todos())
assistant.remove_todo("Pick up groceries")
print(assistant.get_todos())
print(assistant.get_contact("Rubi"))
print(assistant.get_birthday("Truitt"))