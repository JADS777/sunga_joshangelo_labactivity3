## Overview
This program is an interactive command-line Task Tracking system developed in Python. It demonstrates foundational Object-Oriented Design (OOD) principles by modeling real-world tasks and managing their states and behaviors.

## Architecture
The system is built using two related classes that separate individual item behavior from list management:

1. **Task Class:** Serves as the blueprint for individual tasks. 
    * It encapsulates the state (title, priority, status.
    * It provides specific methods (`mark_in_progress()`, `mark_completed()`) to safely alter its internal status without direct external modification.
    * It includes a `__str__` dunder method for clean terminal formatting.
2. **TaskManager Class:** Acts as the collection manager.
    * It stores a list of `Task` objects and handles overarching system operations. 
    * It includes functionalities for adding tasks, safely removing tasks via index retrieval, filtering tasks by status using list comprehensions, and displaying the current queue.

```
+---------------------------+          +--------------------------+
|       TaskManager         |          |           Task           |
+---------------------------+          +--------------------------+
| - tasks: List[Task]       | <>------ | - title: String          |
+---------------------------+ (manages)| - priority: String       |
| + add_task(task)          |          | - status: String         |
| + remove_task(index)      |          +--------------------------+
| + get_task(index)         |          | + mark_in_progress()     |
| + get_tasks_by_status()   |          | + mark_completed()       |
| + display_tasks()         |          | + __str__()              |
+---------------------------+          +--------------------------+
```

## How to Run
1. Ensure Python3 is installed.
2. Run: python3 main.py

