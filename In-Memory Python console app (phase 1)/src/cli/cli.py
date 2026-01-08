"""
Command-line interface for the Todo application.

This module provides the user interface for interacting with the todo list,
including menu options and input handling.
"""

from typing import Optional
from models import Task, Priority
from services.todo_service import TodoService


class TodoCLI:
    """
    Command-line interface for the Todo application.

    This class handles all user interactions through the command line,
    including displaying menus, getting user input, and showing results.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the CLI with a TodoService instance.

        Args:
            todo_service: The service to handle task operations
        """
        self.todo_service = todo_service

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("TODO APPLICATION - MAIN MENU")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete/Incomplete")
        print("6. Assign Task Priority")
        print("7. Search Tasks")
        print("8. Filter Tasks")
        print("9. Sort Tasks")
        print("0. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            The user's choice as a string
        """
        choice = input("Enter your choice (0-9): ").strip()
        return choice

    def add_task(self):
        """Handle adding a new task."""
        print("\n--- ADD TASK ---")
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return

        description = input("Enter task description (optional): ").strip()

        task = self.todo_service.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")

    def view_all_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- ALL TASKS ---")
        tasks = self.todo_service.display_task_list()

        if not tasks:
            print("No tasks found.")
            return

        # Print header
        print(f"{'ID':<3} {'Title':<20} {'Description':<25} {'Status':<10} {'Priority':<10}")
        print("-" * 75)

        # Print each task
        for task in tasks:
            status = "✓ Complete" if task.complete else "○ Incomplete"
            print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:24]:<25} {status:<10} {task.priority.value:<10}")

    def update_task(self):
        """Handle updating an existing task."""
        print("\n--- UPDATE TASK ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.todo_service.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        print(f"Current task: {task.title}")
        new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep): ").strip()
        new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep): ").strip()

        # Prepare update parameters
        update_params = {}
        if new_title:
            update_params['title'] = new_title
        if new_description:
            update_params['description'] = new_description

        if update_params:
            updated_task = self.todo_service.update_task(task_id, **update_params)
            print(f"Task {task_id} updated successfully.")
        else:
            print("No changes made to the task.")

    def delete_task(self):
        """Handle deleting a task."""
        print("\n--- DELETE TASK ---")
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        if self.todo_service.delete_task(task_id):
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_task_status(self):
        """Handle marking a task as complete/incomplete."""
        print("\n--- MARK TASK STATUS ---")
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.todo_service.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_status = "Complete" if task.complete else "Incomplete"
        new_status = input(f"Task is currently {current_status}. Mark as (c)omplete or (i)ncomplete? ").strip().lower()

        if new_status in ['c', 'complete']:
            self.todo_service.update_task(task_id, complete=True)
            print(f"Task {task_id} marked as Complete.")
        elif new_status in ['i', 'incomplete']:
            self.todo_service.update_task(task_id, complete=False)
            print(f"Task {task_id} marked as Incomplete.")
        else:
            print("Invalid input. Please enter 'c' for complete or 'i' for incomplete.")

    def assign_priority(self):
        """Handle assigning priority to a task."""
        print("\n--- ASSIGN TASK PRIORITY ---")
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.todo_service.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        print("Select priority level:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        choice = input("Enter choice (1-3): ").strip()

        priority_map = {
            '1': Priority.HIGH,
            '2': Priority.MEDIUM,
            '3': Priority.LOW
        }

        if choice in priority_map:
            priority = priority_map[choice]
            updated_task = self.todo_service.assign_priority(task_id, priority)
            if updated_task:
                print(f"Priority {priority.value} assigned to task {task_id}.")
            else:
                print(f"Failed to assign priority to task {task_id}.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    def search_tasks(self):
        """Handle searching for tasks."""
        print("\n--- SEARCH TASKS ---")
        keyword = input("Enter keyword to search: ").strip()

        if not keyword:
            print("Search keyword cannot be empty!")
            return

        tasks = self.todo_service.search_tasks(keyword)

        if not tasks:
            print("No tasks found matching the keyword.")
            return

        print(f"\n--- SEARCH RESULTS FOR '{keyword}' ---")
        print(f"{'ID':<3} {'Title':<20} {'Description':<25} {'Status':<10} {'Priority':<10}")
        print("-" * 75)

        for task in tasks:
            status = "✓ Complete" if task.complete else "○ Incomplete"
            print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:24]:<25} {status:<10} {task.priority.value:<10}")

    def filter_tasks(self):
        """Handle filtering tasks."""
        print("\n--- FILTER TASKS ---")

        # Filter by status
        print("Filter by status:")
        print("1. All")
        print("2. Complete only")
        print("3. Incomplete only")
        status_choice = input("Enter choice (1-3): ").strip()

        status_map = {
            '1': 'all',
            '2': 'complete',
            '3': 'incomplete'
        }
        status_filter = status_map.get(status_choice)

        if not status_filter:
            print("Invalid status choice.")
            return

        # Filter by priority
        print("\nFilter by priority:")
        print("1. All")
        print("2. High only")
        print("3. Medium only")
        print("4. Low only")
        priority_choice = input("Enter choice (1-4): ").strip()

        priority_map = {
            '1': None,
            '2': Priority.HIGH,
            '3': Priority.MEDIUM,
            '4': Priority.LOW
        }
        priority_filter = priority_map.get(priority_choice)

        if priority_choice not in priority_map:
            print("Invalid priority choice.")
            return

        tasks = self.todo_service.filter_tasks(
            status_filter=status_filter,
            priority_filter=priority_filter
        )

        print(f"\n--- FILTERED TASKS ---")
        print(f"{'ID':<3} {'Title':<20} {'Description':<25} {'Status':<10} {'Priority':<10}")
        print("-" * 75)

        for task in tasks:
            status = "✓ Complete" if task.complete else "○ Incomplete"
            print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:24]:<25} {status:<10} {task.priority.value:<10}")

    def sort_tasks(self):
        """Handle sorting tasks."""
        print("\n--- SORT TASKS ---")

        print("Sort by:")
        print("1. Title")
        print("2. Priority")
        print("3. Status")
        field_choice = input("Enter choice (1-3): ").strip()

        field_map = {
            '1': 'title',
            '2': 'priority',
            '3': 'complete'
        }
        sort_field = field_map.get(field_choice, 'title')

        print("\nSort order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = input("Enter choice (1-2): ").strip()

        order_map = {
            '1': 'asc',
            '2': 'desc'
        }
        sort_order = order_map.get(order_choice, 'asc')

        tasks = self.todo_service.sort_tasks(sort_field=sort_field, sort_order=sort_order)

        print(f"\n--- SORTED TASKS ({sort_field.upper()}, {sort_order.upper()}) ---")
        print(f"{'ID':<3} {'Title':<20} {'Description':<25} {'Status':<10} {'Priority':<10}")
        print("-" * 75)

        for task in tasks:
            status = "✓ Complete" if task.complete else "○ Incomplete"
            print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:24]:<25} {status:<10} {task.priority.value:<10}")

    def run(self):
        """Run the main CLI loop."""
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_all_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_task_status()
            elif choice == '6':
                self.assign_priority()
            elif choice == '7':
                self.search_tasks()
            elif choice == '8':
                self.filter_tasks()
            elif choice == '9':
                self.sort_tasks()
            elif choice == '0':
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")

            # Pause to let user see the result
            input("\nPress Enter to continue...")