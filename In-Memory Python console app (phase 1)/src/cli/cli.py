"""
Command-line interface for the Todo application with time-aware and recurring task capabilities.

This module provides the user interface for interacting with the todo list,
including menu options and input handling.
"""
from datetime import datetime
from typing import Optional
import sys
import os

# Add the parent directory to the path so imports work correctly
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from models.task import Task, RecurrencePattern
from services.task_service import TaskService
from services.date_utils import parse_date


class TodoCLI:
    """
    Command-line interface for the Todo application with time-aware and recurring capabilities.

    This class handles all user interactions through the command line,
    including displaying menus, getting user input, and showing results.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the CLI with a TaskService instance.

        Args:
            task_service: The service to handle task operations
        """
        self.task_service = task_service

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*60)
        print("TODO APPLICATION - MAIN MENU")
        print("="*60)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete/Incomplete")
        print("6. Search Tasks")
        print("7. Filter Tasks by Due Date Status")
        print("8. Sort Tasks")
        print("0. Exit")
        print("-"*60)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            The user's choice as a string
        """
        choice = input("Enter your choice (0-8): ").strip()
        return choice

    def add_task(self):
        """Handle adding a new task with optional due date and recurrence pattern."""
        print("\n--- ADD TASK ---")
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return

        description = input("Enter task description (optional): ").strip()

        # Ask for due date
        due_date_str = input("Enter due date (optional, format: YYYY-MM-DD or MM/DD/YYYY): ").strip()
        due_date = None
        if due_date_str:
            try:
                due_date = parse_date(due_date_str)
            except ValueError as e:
                print(f"Invalid date format: {e}")
                return

        # Ask for recurrence pattern
        recurrence_choice = input("Make this task recurring? (y/n): ").strip().lower()
        recurrence_pattern = None
        if recurrence_choice == 'y':
            print("Select recurrence frequency:")
            print("1. Daily")
            print("2. Weekly")
            print("3. Monthly")
            print("4. Yearly")

            freq_choice = input("Enter choice (1-4): ").strip()
            freq_map = {
                '1': 'daily',
                '2': 'weekly',
                '3': 'monthly',
                '4': 'yearly'
            }

            if freq_choice in freq_map:
                frequency = freq_map[freq_choice]
                try:
                    interval = int(input(f"Enter interval (every N {frequency}): ").strip())
                    if interval <= 0:
                        print("Interval must be a positive number.")
                        return
                except ValueError:
                    print("Invalid interval. Must be a number.")
                    return

                recurrence_pattern = RecurrencePattern(frequency=frequency, interval=interval)
            else:
                print("Invalid frequency choice. Task will not be recurring.")
                recurrence_pattern = None

        try:
            task = self.task_service.create_task(title, description, due_date, recurrence_pattern)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error creating task: {e}")

    def view_all_tasks(self):
        """Handle viewing all tasks with due dates."""
        print("\n--- ALL TASKS ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        # Print header
        print(f"{'ID':<3} {'Title':<20} {'Description':<20} {'Status':<12} {'Due Date':<16} {'Recurrence':<12}")
        print("-" * 90)

        # Print each task
        for task in tasks:
            status = "✓ Complete" if task.complete else "○ Incomplete"
            due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else "None"
            recurrence_str = f"{task.recurrence_pattern.frequency}" if task.recurrence_pattern else "None"
            print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:19]:<20} {status:<12} {due_date_str:<16} {recurrence_str:<12}")

    def update_task(self):
        """Handle updating an existing task."""
        print("\n--- UPDATE TASK ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        print(f"Current task: {task.title}")
        new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep): ").strip()
        new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep): ").strip()

        # Ask for new due date
        due_date_str = input(f"Enter new due date (current: '{task.due_date}', format: YYYY-MM-DD or MM/DD/YYYY, press Enter to keep): ").strip()
        new_due_date = None
        if due_date_str:
            try:
                new_due_date = parse_date(due_date_str)
            except ValueError as e:
                print(f"Invalid date format: {e}")
                return
        elif due_date_str == "":
            # Empty string means keep current due date
            new_due_date = task.due_date

        # Prepare update parameters
        update_params = {}
        if new_title:
            update_params['title'] = new_title
        if new_description:
            update_params['description'] = new_description
        if 'new_due_date' in locals() and new_due_date != task.due_date:
            update_params['due_date'] = new_due_date

        if update_params:
            updated_task = self.task_service.update_task(task_id, **update_params)
            if updated_task:
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Failed to update task {task_id}.")
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

        if self.task_service.delete_task(task_id):
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

        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        current_status = "Complete" if task.complete else "Incomplete"
        new_status = input(f"Task is currently {current_status}. Mark as (c)omplete or (i)ncomplete? ").strip().lower()

        if new_status in ['c', 'complete']:
            completed_task = self.task_service.complete_task(task_id)
            if completed_task:
                print(f"Task {task_id} marked as Complete.")
                # If the task was recurring, inform the user about the new occurrence
                if task.recurrence_pattern:
                    print("A new occurrence of this recurring task has been created.")
            else:
                print(f"Failed to mark task {task_id} as complete.")
        elif new_status in ['i', 'incomplete']:
            self.task_service.update_task(task_id, complete=False)
            print(f"Task {task_id} marked as Incomplete.")
        else:
            print("Invalid input. Please enter 'c' for complete or 'i' for incomplete.")

    def search_tasks(self):
        """Handle searching for tasks."""
        print("\n--- SEARCH TASKS ---")
        keyword = input("Enter keyword to search: ").strip()

        if not keyword:
            print("Search keyword cannot be empty!")
            return

        # For now, we'll use a simple approach to search in the task list
        all_tasks = self.task_service.get_all_tasks()
        matching_tasks = []
        keyword_lower = keyword.lower()

        for task in all_tasks:
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        if not matching_tasks:
            print("No tasks found matching the keyword.")
            return

        print(f"\n--- SEARCH RESULTS FOR '{keyword}' ---")
        print(f"{'ID':<3} {'Title':<20} {'Description':<20} {'Status':<12} {'Due Date':<16} {'Recurrence':<12}")
        print("-" * 90)

        for task in matching_tasks:
            status = "✓ Complete" if task.complete else "○ Incomplete"
            due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else "None"
            recurrence_str = f"{task.recurrence_pattern.frequency}" if task.recurrence_pattern else "None"
            print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:19]:<20} {status:<12} {due_date_str:<16} {recurrence_str:<12}")

    def filter_tasks_by_due_date_status(self):
        """Handle filtering tasks by due date status."""
        print("\n--- FILTER TASKS BY DUE DATE STATUS ---")
        print("Filter options:")
        print("1. All tasks")
        print("2. Overdue tasks")
        print("3. Upcoming tasks")
        print("4. Tasks with no due date")

        choice = input("Enter choice (1-4): ").strip()
        status_map = {
            '1': 'all',
            '2': 'overdue',
            '3': 'upcoming',
            '4': 'none'
        }

        if choice in status_map:
            status = status_map[choice]
            try:
                tasks = self.task_service.filter_tasks_by_due_date_status(status)
            except ValueError as e:
                print(f"Error filtering tasks: {e}")
                return

            print(f"\n--- {status.upper()} TASKS ---")
            print(f"{'ID':<3} {'Title':<20} {'Description':<20} {'Status':<12} {'Due Date':<16} {'Recurrence':<12}")
            print("-" * 90)

            for task in tasks:
                status_str = "✓ Complete" if task.complete else "○ Incomplete"
                due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else "None"
                recurrence_str = f"{task.recurrence_pattern.frequency}" if task.recurrence_pattern else "None"
                print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:19]:<20} {status_str:<12} {due_date_str:<16} {recurrence_str:<12}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    def sort_tasks(self):
        """Handle sorting tasks."""
        print("\n--- SORT TASKS ---")

        print("Sort by:")
        print("1. Title")
        print("2. Due date")
        print("3. Status")
        field_choice = input("Enter choice (1-3): ").strip()

        field_map = {
            '1': 'title',
            '2': 'due_date',
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

        # For this implementation, we'll just sort by the selected field in memory
        # A full implementation would require a sort_tasks method in TaskService
        tasks = self.task_service.get_all_tasks()

        if sort_field == 'title':
            tasks = sorted(tasks, key=lambda t: t.title.lower(), reverse=(sort_order == 'desc'))
        elif sort_field == 'due_date':
            # Sort by due date, with None dates at the end
            tasks = sorted(tasks,
                          key=lambda t: (t.due_date is None, t.due_date),
                          reverse=(sort_order == 'desc'))
        elif sort_field == 'complete':
            tasks = sorted(tasks, key=lambda t: t.complete, reverse=(sort_order == 'desc'))

        print(f"\n--- SORTED TASKS ({sort_field.upper()}, {sort_order.upper()}) ---")
        print(f"{'ID':<3} {'Title':<20} {'Description':<20} {'Status':<12} {'Due Date':<16} {'Recurrence':<12}")
        print("-" * 90)

        for task in tasks:
            status = "✓ Complete" if task.complete else "○ Incomplete"
            due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else "None"
            recurrence_str = f"{task.recurrence_pattern.frequency}" if task.recurrence_pattern else "None"
            print(f"{task.id:<3} {task.title[:19]:<20} {task.description[:19]:<20} {status:<12} {due_date_str:<16} {recurrence_str:<12}")

    def run(self):
        """Run the main CLI loop."""
        print("Welcome to the Todo Application with Time-Aware and Recurring Tasks!")

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
                self.search_tasks()
            elif choice == '7':
                self.filter_tasks_by_due_date_status()
            elif choice == '8':
                self.sort_tasks()
            elif choice == '0':
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 8.")

            # Pause to let user see the result
            input("\nPress Enter to continue...")