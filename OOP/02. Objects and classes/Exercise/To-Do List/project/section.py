from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: str):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        else:
            task_name.completed = True
            return f"Completed task {task_name}"

    def clean_section(self):
        completed = len([x for x in self.tasks if x.completed])
        return f"Cleared {completed} tasks."

    def view_section(self):
        tasks_details = "\n".join([tsk.details() for tsk in self.tasks])
        return f"Section {self.name}:\n{tasks_details}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
