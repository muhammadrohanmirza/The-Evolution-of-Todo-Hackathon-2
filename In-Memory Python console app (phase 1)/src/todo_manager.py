"""
TodoManager class to handle all task operations.
"""

from typing import List, Optional

# Handle both direct execution and module execution
try:
    from .models import Task
except ImportError:
    from models import Task


class TodoManager:
    """
    Manages the in-memory storage of tasks and provides methods for all CRUD operations.
    """

    def __init__(self):
        """
        Initialize the TodoManager with an empty task list and ID counter.
        """
        self.tasks: List[Task] = []
        self._next_id = 1

    def get_next_id(self) -> int:
        """
        Get the next available ID and increment the counter.

        Returns:
            The next available unique ID
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and optional description.

        Args:
            title: The task title (required)
            description: The task description (optional)

        Returns:
            The newly created Task object
        """
        task_id = self.get_next_id()
        task = Task(id=task_id, title=title, description=description, complete=False)
        self.tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the task list.

        Returns:
            A list of all Task objects
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a task's title or description by its ID.

        Args:
            task_id: The ID of the task to update
            title: The new title (optional)
            description: The new description (optional)

        Returns:
            True if the task was updated, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int, complete: bool = True) -> bool:
        """
        Mark a task as complete or incomplete by its ID.

        Args:
            task_id: The ID of the task to update
            complete: Whether the task should be marked as complete (default True)

        Returns:
            True if the task was updated, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.complete = complete
            return True
        return False