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
        print(f"\nSuccess: '{task.title}' has been added.")

    def remove_task(self, index):
        try:
            task = self.tasks.pop(index)
            print(f"\nSuccess: '{task.title}' has been removed.")
        except IndexError:
            print("\nError: Task not found at the given index.")

    def get_task(self, index):
        try:
            return self.tasks[index]
        except IndexError:
            return None

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status.lower() == status.lower()]

    def display_tasks(self):
        print("\n--- Current Tasks ---")
        if not self.tasks:
            print("List empty. No tasks to display.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

def main():
    task_manager = TaskManager()

    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Update Task Status")
        print("4. Remove a Task")
        print("5. Filter Tasks by Status")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("\nInvalid input. Please enter a numeric value between 1 and 6.")
            continue

        if choice == 1:
            title = input("Enter task title: ").strip()
            if not title:
                print("\nError: Task title cannot be empty.")
                continue
            print("\nSelect Priority:")
            print("1. Low")
            print("2. Normal")
            print("3. High")
            try:
                prio_choice = input("Enter priority (1-3) [Default: Normal]: ")
                if not prio_choice:
                    priority = "Normal"
                else:
                    prio_choice = int(prio_choice)
                    if prio_choice == 1:
                        priority = "Low"
                    elif prio_choice == 2:
                        priority = "Normal"
                    elif prio_choice == 3:
                        priority = "High"
                    else:
                        print("\nInvalid choice. Defaulting to Normal priority.")
                        priority = "Normal"
            except ValueError:
                print("\nInvalid input. Defaulting to Normal priority.")
                priority = "Normal"
            task_manager.add_task(Task(title, priority))

        elif choice == 2:
            task_manager.display_tasks()
        
        elif choice == 3:
            task_manager.display_tasks()
            if not task_manager.tasks:
                continue
            try:
                task_num = int(input("Enter the task number to update: ")) - 1
                if task_num < 0:
                    print("\nError: Invalid task number.")
                    continue
                task = task_manager.get_task(task_num)
                if task:
                    print("\n1. Mark In Progress")
                    print("2. Mark Completed")
                    status_choice = input("Choose new status (1 or 2): ")
                    if status_choice == '1':
                        task.mark_in_progress()
                        print("\nSuccess: Task marked as In Progress.")
                    elif status_choice == '2':
                        task.mark_completed()
                        print("\nSuccess: Task marked as Completed.")
                    else:
                        print("\nError: Invalid choice. Status not updated.")
                else:
                    print("\nError: Invalid task number.")
            except ValueError:
                print("\nError: Please enter a valid numerical index.")

        elif choice == 4:
            task_manager.display_tasks()
            if not task_manager.tasks:
                continue
            try:
                task_num = int(input("Enter the task number to remove: ")) - 1
                if task_num < 0:
                    print("\nError: Invalid task number.")
                else:
                    task_manager.remove_task(task_num)
            except ValueError:
                print("\nError: Please enter a valid numerical index.")

        elif choice == 5:
            print("\nSelect Status to Filter:")
            print("1. To-Do")
            print("2. In Progress")
            print("3. Completed")
            try:
                stat_choice = int(input("Enter choice (1-3): "))
                if stat_choice == 1:
                    status = "To-Do"
                elif stat_choice == 2:
                    status = "In Progress"
                elif stat_choice == 3:
                    status = "Completed"
                else:
                    print("\nError: Invalid choice. Please select 1, 2, or 3.")
                    continue
                filtered = task_manager.get_tasks_by_status(status)
                print(f"\n--- Tasks with status '{status}' ---")
                if not filtered:
                    print("No tasks found matching that status.")
                else:
                    for i, task in enumerate(filtered):
                        print(f"- {task}")
            except ValueError:
                print("\nError: Please enter a valid numerical choice.")

        elif choice == 6:
            print("\nExiting Task Manager. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()
