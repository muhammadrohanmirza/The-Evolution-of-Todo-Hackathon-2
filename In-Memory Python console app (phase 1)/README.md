# Todo In-Memory Python Console App

A simple command-line todo application that stores tasks in memory. This application allows users to add, view, update, delete, and mark tasks as complete.

## Features

- Add new tasks with title and optional description
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete

## Setup

1. Make sure you have Python 3.13+ installed
2. Install UV package manager: `pip install uv`
3. Clone this repository
4. Navigate to the project directory
5. Run the application: `python src/main.py`

## Usage

The application provides a menu-driven interface. Simply follow the prompts to interact with your todo list.

## Architecture

- `src/main.py` - Entry point with CLI menu loop
- `src/todo_manager.py` - Core class handling task storage and all operations
- `src/models.py` - Task dataclass definition