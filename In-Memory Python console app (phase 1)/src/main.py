"""
Main entry point for the Todo In-Memory Python Console App.
"""

import sys
import os

# Handle both direct execution and module execution
try:
    from .todo_manager import TodoManager
    from .models import Task
except ImportError:
    # If run as a script directly, add the src directory to the path and import without the dot
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from todo_manager import TodoManager
    from models import Task


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "="*40)
    print("TODO APPLICATION")
    print("="*40)
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("0. Exit")
    print("-"*40)


def display_task(task: Task):
    """
    Display a single task with proper formatting.

    Args:
        task: The Task object to display
    """
    status = "✔️" if task.complete else "❌"
    print(f"[{status}] ID: {task.id} | Title: {task.title}")
    if task.description:
        print(f"      Description: {task.description}")


def display_tasks(tasks: list):
    """
    Display all tasks in a formatted way.

    Args:
        tasks: List of Task objects to display
    """
    if not tasks:
        print("\nNo tasks found.")
        return

    print(f"\nTotal tasks: {len(tasks)}")
    for task in tasks:
        display_task(task)
        print()


def get_user_input(prompt: str) -> str:
    """
    Get input from the user with proper error handling.

    Args:
        prompt: The prompt to display to the user

    Returns:
        The user's input as a string
    """
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nOperation cancelled by user.")
        return ""


def get_task_id_input(prompt: str = "Enter task ID: ") -> int:
    """
    Get a task ID from user input with validation.

    Args:
        prompt: The prompt to display to the user

    Returns:
        The task ID as an integer, or -1 if invalid
    """
    user_input = get_user_input(prompt)
    if not user_input:
        return -1

    try:
        task_id = int(user_input)
        return task_id
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return -1


def main():
    """
    Main application loop.
    """
    print("Welcome to the Todo In-Memory Python Console App!")

    todo_manager = TodoManager()

    while True:
        display_menu()

        choice = get_user_input("Select an option (0-5): ")

        if choice == "0":
            print("Thank you for using the Todo App. Goodbye!")
            break

        elif choice == "1":
            # Add Task
            title = get_user_input("Enter task title: ")
            if not title:
                print("Task title cannot be empty.")
                continue

            description = get_user_input("Enter task description (optional): ")

            task = todo_manager.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")

        elif choice == "2":
            # View Task List
            tasks = todo_manager.get_all_tasks()
            display_tasks(tasks)

        elif choice == "3":
            # Update Task
            task_id = get_task_id_input("Enter task ID to update: ")
            if task_id == -1:
                continue

            task = todo_manager.get_task_by_id(task_id)
            if not task:
                print(f"Task with ID {task_id} not found.")
                continue

            print(f"Current task: {task.title}")
            if task.description:
                print(f"Current description: {task.description}")

            new_title = get_user_input(f"Enter new title (current: '{task.title}'): ")
            if not new_title:
                new_title = None  # Keep existing title

            new_description = get_user_input(f"Enter new description (current: '{task.description}'): ")
            if new_description == task.description:
                new_description = None  # Keep existing description

            if todo_manager.update_task(task_id, new_title, new_description):
                print("Task updated successfully.")
            else:
                print("Failed to update task.")

        elif choice == "4":
            # Delete Task
            task_id = get_task_id_input("Enter task ID to delete: ")
            if task_id == -1:
                continue

            if todo_manager.delete_task(task_id):
                print(f"Task with ID {task_id} deleted successfully.")
            else:
                print(f"Task with ID {task_id} not found.")

        elif choice == "5":
            # Mark Task as Complete
            task_id = get_task_id_input("Enter task ID to mark as complete/incomplete: ")
            if task_id == -1:
                continue

            task = todo_manager.get_task_by_id(task_id)
            if not task:
                print(f"Task with ID {task_id} not found.")
                continue

            # Toggle the completion status
            new_status = not task.complete
            if todo_manager.mark_task_complete(task_id, new_status):
                status_str = "complete" if new_status else "incomplete"
                print(f"Task marked as {status_str}.")
            else:
                print("Failed to update task status.")

        else:
            print("Invalid option. Please select a number between 0 and 5.")


if __name__ == "__main__":
    main()