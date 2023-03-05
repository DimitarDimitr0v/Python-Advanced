from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        for curr_task in self.tasks:
            if curr_task.name == task_name:
                curr_task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed = [t for t in self.tasks if t.completed == True]
        return f"Cleared {len(completed)} tasks."

    def view_section(self):
        tasks_details = "\n".join([tsk.details() for tsk in self.tasks])
        return f"Section {self.name}:\n{tasks_details}"

