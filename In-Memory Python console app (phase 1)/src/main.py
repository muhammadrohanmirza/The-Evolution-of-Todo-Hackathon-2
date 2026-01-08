"""
Main entry point for the Todo In-Memory Python Console App.
"""

import sys
import os

# Handle both direct execution and module execution
try:
    from .services.todo_service import TodoService
    from .cli.cli import TodoCLI
except ImportError:
    # If run as a script directly, add the src directory to the path and import without the dot
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from services.todo_service import TodoService
    from cli.cli import TodoCLI


def main():
    """
    Main application entry point.
    Initializes the service and CLI, then starts the application loop.
    """
    print("Welcome to the Todo In-Memory Python Console App!")
    print("Enhanced with priority levels, search, filter, and sort capabilities.")

    # Initialize the service and CLI
    todo_service = TodoService()
    cli = TodoCLI(todo_service)

    # Start the CLI loop
    cli.run()


if __name__ == "__main__":
    main()