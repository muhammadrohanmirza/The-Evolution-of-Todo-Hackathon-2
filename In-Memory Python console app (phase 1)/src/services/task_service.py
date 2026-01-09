"""
Service layer for todo operations with time-aware and recurring task capabilities.

This module contains the business logic for managing tasks,
including adding, updating, deleting, and querying tasks with due dates and recurrence.
"""
from datetime import datetime
from typing import List, Optional, Dict, Any
import logging
import sys
import os

# Add the parent directory to the path so imports work correctly
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from models.task import Task, RecurrencePattern
from services.date_utils import is_overdue, add_interval_to_date
from lib.validators import validate_task_with_recurrence


# Configure logging for the service
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TaskService:
    """
    Service class for managing todo tasks with time-aware and recurring capabilities.

    This class handles all business logic related to task management,
    including creating, retrieving, updating, and deleting tasks with due dates and recurrence.
    """

    def __init__(self):
        """Initialize the TaskService with an empty task list."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def create_task(self, title: str, description: str = "", due_date: Optional[datetime] = None,
                   recurrence_pattern: Optional[RecurrencePattern] = None) -> Task:
        """
        Add a new task to the list with optional due date and recurrence pattern.

        Args:
            title: The title of the task
            description: Optional description of the task
            due_date: Optional due date for the task
            recurrence_pattern: Optional recurrence pattern for the task

        Returns:
            The newly created Task object
        """
        # When there's a recurrence pattern, there must be a due date
        if recurrence_pattern is not None and due_date is None:
            raise ValueError("A due date is required for recurring tasks")

        # For validation, convert the RecurrencePattern object to a dictionary format
        # that the validation function expects
        recurrence_dict = None
        if recurrence_pattern is not None:
            recurrence_dict = {
                "frequency": recurrence_pattern.frequency,
                "interval": recurrence_pattern.interval,
                "end_condition": recurrence_pattern.end_condition
            }

        # Validate task if it has recurrence pattern
        task_data = {
            "title": title,
            "description": description,
            "due_date": due_date.strftime("%Y-%m-%d %H:%M") if due_date else None,  # Convert datetime to string for validation
            "recurrence_pattern": recurrence_dict
        }

        # Only validate if there's a recurrence pattern
        if recurrence_pattern is not None:
            # Validate the recurrence pattern components individually
            if recurrence_dict["frequency"] not in ["daily", "weekly", "monthly", "yearly"]:
                raise ValueError(f"Invalid frequency: {recurrence_dict['frequency']}")

            if not isinstance(recurrence_dict["interval"], int) or recurrence_dict["interval"] <= 0:
                raise ValueError(f"Invalid interval: {recurrence_dict['interval']}")

            # Validate the due date format
            if due_date and not self._validate_date_format_for_task(task_data["due_date"]):
                raise ValueError(f"Invalid date format: {task_data['due_date']}")

        task_id = self._next_id
        task = Task(
            id=task_id,
            title=title,
            description=description,
            due_date=due_date,
            recurrence_pattern=recurrence_pattern
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def _validate_date_format_for_task(self, date_str: str) -> bool:
        """
        Internal method to validate date format.
        """
        if not date_str or not isinstance(date_str, str):
            return False

        # Remove extra whitespace
        date_str = date_str.strip()

        # Define supported formats
        formats = [
            "%Y-%m-%d %H:%M",
            "%m/%d/%Y %H:%M",
            "%d/%m/%Y %H:%M",
            "%Y-%m-%d",
            "%m/%d/%Y",
            "%d/%m/%Y"
        ]

        for fmt in formats:
            try:
                datetime.strptime(date_str, fmt)
                return True
            except ValueError:
                continue

        return False

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
                   complete: Optional[bool] = None,
                   due_date: Optional[datetime] = None) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            complete: New completion status (optional)
            due_date: New due date (optional)

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
                if complete and task.completed_at is None:
                    task.completed_at = datetime.now()
            if due_date is not None:
                task.due_date = due_date
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

    def complete_task(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete. If the task has a recurrence pattern,
        creates the next occurrence.

        Args:
            task_id: The ID of the task to complete

        Returns:
            The completed Task object, and optionally the newly created recurring Task object if applicable
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        # Mark the current task as complete
        task.complete = True
        task.completed_at = datetime.now()

        # If the task has a recurrence pattern, create the next occurrence
        if task.recurrence_pattern:
            next_task = self._create_next_occurrence(task)
            if next_task:
                self.tasks.append(next_task)
                logger.info(f"Created next occurrence of recurring task {task.title}")

        return task

    def _create_next_occurrence(self, task: Task) -> Optional[Task]:
        """
        Create the next occurrence of a recurring task.

        Args:
            task: The completed recurring task

        Returns:
            The new Task object for the next occurrence, or None if recurrence should end
        """
        if not task.recurrence_pattern:
            return None

        pattern = task.recurrence_pattern

        # Check if recurrence should end based on end_condition
        if pattern.end_condition:
            end_type = pattern.end_condition.get('type')
            end_value = pattern.end_condition.get('value')

            if end_type == 'after_occurrences':
                # Count how many occurrences of this task exist in the system
                # This is a simplified approach - in a real system you might track this differently
                pass  # For now, we'll continue creating occurrences
            elif end_type == 'on_date':
                # Check if the next occurrence date would exceed the end date
                next_date = add_interval_to_date(task.due_date or task.created_at,
                                                pattern.frequency, pattern.interval)
                end_date = datetime.fromisoformat(end_value) if isinstance(end_value, str) else end_value
                if next_date > end_date:
                    return None

        # Calculate the next due date based on the recurrence pattern
        next_due_date = add_interval_to_date(
            task.due_date or task.created_at,
            pattern.frequency,
            pattern.interval
        )

        # Adjust the next due date if it falls in the past
        if next_due_date < datetime.now():
            # Keep adding intervals until we get a future date
            while next_due_date < datetime.now():
                next_due_date = add_interval_to_date(
                    next_due_date,
                    pattern.frequency,
                    pattern.interval
                )

        # Create a new task with the same properties as the original
        new_task = Task(
            id=self._next_id,
            title=task.title,
            description=task.description,
            complete=False,  # New occurrence starts as incomplete
            due_date=next_due_date,
            recurrence_pattern=pattern,
            created_at=datetime.now()
        )
        self._next_id += 1

        return new_task

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all tasks that are overdue (past due date and not completed).

        Returns:
            A list of overdue Task objects
        """
        overdue_tasks = []
        for task in self.tasks:
            if task.due_date and is_overdue(task.due_date, task.complete):
                overdue_tasks.append(task)
        return overdue_tasks

    def assign_priority(self, task_id: int, priority) -> Optional[Task]:
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

    def filter_tasks_by_due_date_status(self, status: str) -> List[Task]:
        """
        Filter tasks by due date status.

        Args:
            status: One of 'overdue', 'upcoming', 'none', 'all'

        Returns:
            A list of Task objects matching the status
        """
        if status == 'overdue':
            return self.get_overdue_tasks()
        elif status == 'upcoming':
            upcoming_tasks = []
            for task in self.tasks:
                if (task.due_date and
                    not is_overdue(task.due_date, task.complete) and
                    not task.complete):
                    upcoming_tasks.append(task)
            return upcoming_tasks
        elif status == 'none':
            no_due_date_tasks = []
            for task in self.tasks:
                if task.due_date is None:
                    no_due_date_tasks.append(task)
            return no_due_date_tasks
        elif status == 'all':
            return self.get_all_tasks()
        else:
            raise ValueError(f"Invalid status: {status}. Must be one of 'overdue', 'upcoming', 'none', 'all'")