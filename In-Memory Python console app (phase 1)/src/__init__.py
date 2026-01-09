"""
Todo Application Package

This package contains a simple command-line todo application that stores tasks in memory.
"""

__version__ = "1.0.0"
__author__ = "Todo App Developer"

# Import main classes to make them available at package level
from .models.task import Task, RecurrencePattern, Priority

__all__ = ["Task", "RecurrencePattern", "Priority"]