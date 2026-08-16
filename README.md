# Task Manager System

## Overview
This program is a command-line Task Tracking system developed in Python. It demonstrates foundational Object-Oriented Design (OOD) principles by modeling real-world tasks and managing their states and 
behaviors within a structured environment.

## Architecture
The system is built using two related classes that separate individual item behavior from list management:
1. Task Class: Serves as the blueprint for individual tasks. It encapsulates the state (title, priority, status) and provides specific methods
 (`mark_in_progress()`, `mark_completed()`) to safely alter its internal status without direct external modification. It also includes a `__str__` dunder method for clean terminal formatting.
2. TaskManager Class: Acts as the collection manager. It stores a list of `Task` objects and handles overarching system operations. This includes adding tasks, removing tasks (with built-in error checking if
 a task is missing), filtering tasks by status using list comprehensions, and displaying the current queue.

```
+---------------------------+          +--------------------------+
|       TaskManager         |          |           Task           |
+---------------------------+          +--------------------------+
| - tasks: List[Task]       | <>------ | - title: String          |
+---------------------------+ (manages)| - priority: String       |
| + add_task(task)          |          | - status: String         |
| + remove_task(task)       |          +--------------------------+
| + get_tasks_by_status()   |          | + mark_in_progress()     |
| + display_tasks()         |          | + mark_completed()       |
+---------------------------+          +--------------------------+
```
