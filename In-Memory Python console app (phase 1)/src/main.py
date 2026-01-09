"""
Main entry point for the Todo application with time-aware and recurring task capabilities.
"""
from services.task_service import TaskService
from cli.cli import TodoCLI


def main():
    """Main function to run the Todo application."""
    # Create the task service
    task_service = TaskService()

    # Create the CLI interface
    cli = TodoCLI(task_service)

    # Run the CLI
    cli.run()


if __name__ == "__main__":
    main()