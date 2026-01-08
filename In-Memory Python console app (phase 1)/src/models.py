"""
Data models for the Todo application.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Priority(Enum):
    """
    Represents the priority level of a task.

    Attributes:
        HIGH: For urgent or important tasks
        MEDIUM: For standard priority tasks
        LOW: For tasks that can be deferred
    """
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id: Unique integer identifier for the task
        title: String representing the task title (required)
        description: String with detailed task information (optional)
        complete: Boolean indicating completion status (default False)
        priority: Priority level of the task (default MEDIUM)
    """
    id: int
    title: str
    description: Optional[str] = ""
    complete: bool = False
    priority: Priority = Priority.MEDIUM