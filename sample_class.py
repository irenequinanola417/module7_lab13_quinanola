class TaskManager:
    def __init__(self, title, owner, completed=False):
        self.title = title
        self.owner = owner
        self.completed = completed

    def mark_complete(self):
        self.completed = True
        return "Task marked as complete."

    def display(self):
        return f"Task: {self.title}, Owner: {self.owner}, Completed: {self.completed}"

    def set_priority(self, level):
        return f"Priority set to {level}"