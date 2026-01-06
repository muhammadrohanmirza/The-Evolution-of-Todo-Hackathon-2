"""
Data models for the Todo application.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo task.
    
    Attributes:
        id: Unique integer identifier for the task
        title: String representing the task title (required)
        description: String with detailed task information (optional)
        complete: Boolean indicating completion status (default False)
    """
    id: int
    title: str
    description: Optional[str] = ""
    complete: bool = False