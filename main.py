class Task:
    def __init__(self, title, priority="Normal", status="To-Do"):
        self.title = title
        self.priority = priority
        self.status = status

    def mark_in_progress(self):
        self.status = "In Progress"

    def mark_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"Task: {self.title}, Priority: {self.priority}, Status: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            print(f"{task.title} has been removed.")
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def display_tasks(self):
        print("Current Tasks:")
        if not self.tasks:
            print("List empty. Sit back and relax.")
        for i in range(len(self.tasks)):
            print(f"{i + 1}. {self.tasks[i]}")

if __name__ == "__main__":
    task_manager = TaskManager()

    t1=Task("CPE106L LabActivity4", priority="High")
    t2=Task("Buy groceries")
    t3=Task("Look for internship", priority="High")
    t4=Task("Group laboratory report", status="In Progress")
    t5=Task("Touch grass", priority="Low")

    task_manager.add_task(t1)
    task_manager.add_task(t2)
    task_manager.add_task(t3)
    task_manager.add_task(t4)
    task_manager.add_task(t5)
    task_manager.display_tasks()

    t1.mark_in_progress()
    task_manager.remove_task(t2)
    t3.mark_completed()
    t4.mark_completed()
    t5.mark_completed()
    task_manager.display_tasks()


    completed_tasks = task_manager.get_tasks_by_status("Completed")
    for task in completed_tasks:
        print(f"Completed Task: {task}")

