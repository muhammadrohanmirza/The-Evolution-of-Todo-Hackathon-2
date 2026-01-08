"""
Service layer for todo operations.

This module contains the business logic for managing tasks,
including adding, updating, deleting, and querying tasks.
"""

from typing import List, Optional
from enum import Enum
import logging
from models import Task, Priority


# Configure logging for the service
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TodoService:
    """
    Service class for managing todo tasks.

    This class handles all business logic related to task management,
    including creating, retrieving, updating, and deleting tasks.
    """

    def __init__(self):
        """Initialize the TodoService with an empty task list."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the list.

        Args:
            title: The title of the task
            description: Optional description of the task

        Returns:
            The newly created Task object
        """
        task = Task(id=self._next_id, title=title, description=description)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.

        Returns:
            A list of all Task objects
        """
        return self.tasks.copy()

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None,
                   complete: Optional[bool] = None) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            complete: New completion status (optional)

        Returns:
            The updated Task object if found, None otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if complete is not None:
                task.complete = complete
            return task
        return None

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

    def assign_priority(self, task_id: int, priority: Priority) -> Optional[Task]:
        """
        Assign a priority level to a task.

        Args:
            task_id: The ID of the task to update
            priority: The priority level to assign

        Returns:
            The updated Task object if found, None otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            old_priority = task.priority
            task.priority = priority
            logger.info(f"Priority updated for task {task_id}: {old_priority.value} -> {priority.value}")
            return task
        logger.warning(f"Failed to assign priority: task {task_id} not found")
        return None

    def display_task_list(self) -> List[Task]:
        """
        Get all tasks with their priority information.

        Returns:
            A list of all Task objects
        """
        return self.get_all_tasks()

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Find tasks containing a keyword in title or description.

        Args:
            keyword: The keyword to search for

        Returns:
            A list of Task objects that match the keyword
        """
        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.tasks:
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        logger.info(f"Search for '{keyword}' returned {len(matching_tasks)} task(s)")
        return matching_tasks

    def filter_tasks(self, status_filter: Optional[str] = None,
                     priority_filter: Optional[Priority] = None) -> List[Task]:
        """
        Filter tasks by completion status or priority.

        Args:
            status_filter: Filter by status ('all', 'complete', 'incomplete')
            priority_filter: Filter by priority level

        Returns:
            A list of Task objects that match the filter criteria
        """
        filtered_tasks = self.tasks.copy()

        # Apply status filter if specified
        if status_filter and status_filter != 'all':
            if status_filter == 'complete':
                filtered_tasks = [task for task in filtered_tasks if task.complete]
            elif status_filter == 'incomplete':
                filtered_tasks = [task for task in filtered_tasks if not task.complete]

        # Apply priority filter if specified
        if priority_filter:
            filtered_tasks = [task for task in filtered_tasks if task.priority == priority_filter]

        # Log filter operation
        status_desc = f"status={status_filter}" if status_filter else "no status filter"
        priority_desc = f"priority={priority_filter.value if priority_filter else None}" if priority_filter is not None else "no priority filter"
        logger.info(f"Applied filters: {status_desc}, {priority_desc}. Result: {len(filtered_tasks)} task(s)")

        return filtered_tasks

    def sort_tasks(self, sort_field: str = 'title', sort_order: str = 'asc') -> List[Task]:
        """
        Sort tasks by specified field and order.

        Args:
            sort_field: Field to sort by ('title', 'priority', 'complete')
            sort_order: Sort order ('asc' for ascending, 'desc' for descending)

        Returns:
            A sorted list of Task objects
        """
        reverse = sort_order == 'desc'

        if sort_field == 'title':
            sorted_tasks = sorted(self.tasks, key=lambda t: t.title.lower(), reverse=reverse)
        elif sort_field == 'priority':
            # Sort by priority with HIGH > MEDIUM > LOW
            priority_order = {Priority.HIGH: 3, Priority.MEDIUM: 2, Priority.LOW: 1}
            sorted_tasks = sorted(self.tasks,
                                 key=lambda t: priority_order[t.priority],
                                 reverse=reverse)
        elif sort_field == 'complete':
            sorted_tasks = sorted(self.tasks, key=lambda t: t.complete, reverse=reverse)
        else:
            # Default to sorting by title
            sorted_tasks = sorted(self.tasks, key=lambda t: t.title.lower(), reverse=reverse)

        logger.info(f"Sorted {len(sorted_tasks)} task(s) by {sort_field} in {'ascending' if not reverse else 'descending'} order")
        return sorted_tasks