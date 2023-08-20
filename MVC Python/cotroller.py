from model import TaskModel
from view import TaskView

class TaskController:
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

    def add_task(self, task):
        self.model.add_task(task)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)
