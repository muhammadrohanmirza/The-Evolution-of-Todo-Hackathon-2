# Todo Application with Time-Aware and Recurring Tasks

This is an in-memory Python console application that allows users to manage their tasks with advanced time-aware and recurring capabilities.

## Features

- **Add Tasks**: Create new tasks with optional descriptions
- **Due Dates**: Assign due dates to tasks to track deadlines
- **Overdue Task Identification**: Automatically identify and display overdue tasks
- **Recurring Tasks**: Create tasks that repeat on a daily, weekly, monthly, or yearly basis
- **Task Management**: Update, delete, and mark tasks as complete/incomplete
- **Filtering**: Filter tasks by due date status (overdue, upcoming, none)
- **Search**: Search tasks by title or description

## Usage

Run the application from the src directory:

```bash
cd src
python main.py
```

The application provides a menu-driven interface:

1. **Add Task**: Create a new task with an optional due date and recurrence pattern
2. **View All Tasks**: Display all tasks with their due dates and recurrence status
3. **Update Task**: Modify an existing task's title, description, or due date
4. **Delete Task**: Remove a task from the list
5. **Mark Task as Complete/Incomplete**: Toggle the completion status of a task
6. **Search Tasks**: Find tasks by keyword in title or description
7. **Filter Tasks by Due Date Status**: Show only overdue, upcoming, or tasks without due dates
8. **Sort Tasks**: Sort tasks by title, due date, or status

### Creating Tasks with Due Dates

When adding a task, you can specify a due date in one of these formats:
- YYYY-MM-DD (e.g., 2023-12-25)
- MM/DD/YYYY (e.g., 12/25/2023)
- DD/MM/YYYY (e.g., 25/12/2023)

### Creating Recurring Tasks

When adding a task, you can make it recurring by selecting the recurrence frequency:
- Daily
- Weekly
- Monthly
- Yearly

You'll also specify the interval (e.g., every 2 weeks, every 3 months).

When a recurring task is marked as complete, the application automatically creates the next occurrence based on the recurrence pattern.

### Filtering Tasks

The application allows filtering tasks by due date status:
- **All**: Show all tasks
- **Overdue**: Show tasks with past due dates that are not completed
- **Upcoming**: Show tasks with future due dates that are not completed
- **None**: Show tasks without due dates

## Architecture

The application follows a modular design:

- `models/task.py`: Contains the Task and RecurrencePattern data models
- `services/task_service.py`: Business logic for task operations
- `services/date_utils.py`: Date and time utility functions
- `lib/validators.py`: Validation functions for dates and recurrence patterns
- `cli/cli.py`: Command-line interface

## Testing

Unit tests are located in the `tests/` directory (in the parent directory):
- `tests/unit/models/`: Tests for data models
- `tests/unit/services/`: Tests for service layer
- `tests/unit/lib/`: Tests for utility functions
- `tests/integration/`: Integration tests

## Data Model

The application uses the following data models:

### Task
- `id`: Unique integer identifier
- `title`: Task title
- `description`: Optional task description
- `complete`: Boolean indicating completion status
- `due_date`: Optional datetime for the task deadline
- `recurrence_pattern`: Optional recurrence pattern
- `created_at`: Datetime when the task was created
- `completed_at`: Optional datetime when the task was completed

### RecurrencePattern
- `frequency`: How often the task repeats ('daily', 'weekly', 'monthly', 'yearly')
- `interval`: How many periods between occurrences
- `end_condition`: Optional condition for when recurrence ends