"""
Data models for the Todo application with time-aware and recurring task capabilities.
"""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any


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
class RecurrencePattern:
    """
    Defines how a task repeats.

    Attributes:
        frequency: How often the task repeats ('daily', 'weekly', 'monthly', 'yearly')
        interval: How many periods between occurrences (e.g., every 2 weeks)
        end_condition: Optional condition for when recurrence ends
    """
    frequency: str  # 'daily', 'weekly', 'monthly', 'yearly'
    interval: int = 1
    end_condition: Optional[Dict[str, Any]] = None  # e.g., {'type': 'after_occurrences', 'value': 5}


@dataclass
class Task:
    """
    Represents a single todo task with time-aware and recurring capabilities.

    Attributes:
        id: Unique integer identifier for the task
        title: String representing the task title (required)
        description: String with detailed task information (optional)
        complete: Boolean indicating completion status (default False)
        priority: Priority level of the task (default MEDIUM)
        due_date: Optional datetime object representing the task deadline
        recurrence_pattern: Optional RecurrencePattern object defining repetition rules
        created_at: Datetime object representing when the task was created
        completed_at: Optional datetime object representing when the task was completed
    """
    id: int
    title: str
    description: Optional[str] = ""
    complete: bool = False
    priority: Priority = Priority.MEDIUM
    due_date: Optional[datetime] = None
    recurrence_pattern: Optional[RecurrencePattern] = None
    created_at: datetime = None
    completed_at: Optional[datetime] = None

    def __post_init__(self):
        """
        Initialize default values after object creation.
        """
        if self.created_at is None:
            self.created_at = datetime.now()
        
        if self.completed_at is None and self.complete:
            self.completed_at = datetime.now()