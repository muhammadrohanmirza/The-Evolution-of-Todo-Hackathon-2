# API Contract: Time-Aware and Recurring Tasks

## Overview
This document defines the API contract for the time-aware and recurring tasks functionality in the todo console application.

## Task Model Extensions

### Task Object
Extended properties:
- `due_date` (string, optional): ISO 8601 formatted date-time string representing the task deadline
- `recurrence_pattern` (object, optional): Defines how the task repeats
  - `frequency` (string): One of "daily", "weekly", "monthly", "yearly"
  - `interval` (integer): How often the pattern repeats (e.g., every 2 weeks)
  - `end_condition` (object, optional): Defines when recurrence ends
    - `type` (string): One of "after_occurrences", "on_date", "never"
    - `value` (integer or string): Count or date depending on type

## Service Methods

### TaskService.create_task(title, description=None, due_date=None, recurrence_pattern=None)
Creates a new task with optional due date and recurrence pattern.

**Parameters:**
- `title` (string): Task title
- `description` (string, optional): Task description
- `due_date` (string, optional): ISO 8601 formatted date-time string
- `recurrence_pattern` (object, optional): Recurrence pattern definition

**Returns:**
- Task object with assigned ID

**Validation:**
- Title is required
- If recurrence_pattern is provided, due_date must also be provided
- recurrence_pattern must have valid frequency and interval values

### TaskService.get_tasks(filter_by_due_date=None)
Retrieves tasks with optional filtering by due date status.

**Parameters:**
- `filter_by_due_date` (string, optional): One of "overdue", "upcoming", "none", "all"

**Returns:**
- Array of Task objects

### TaskService.complete_task(task_id)
Marks a task as complete. If the task has a recurrence pattern, creates the next occurrence.

**Parameters:**
- `task_id` (integer): ID of the task to complete

**Returns:**
- Completed Task object
- Optionally, the newly created recurring Task object if applicable

**Validation:**
- Task must exist
- If task has recurrence pattern, next occurrence must be created with updated due date

## CLI Commands

### add "task title" --due-date "YYYY-MM-DD" --recurrence "daily|weekly" --interval N
Adds a new task with optional due date and recurrence pattern.

### list --due-status "overdue|upcoming|all"
Lists tasks with optional filtering by due date status.

### complete <task_id>
Marks a task as complete and generates next occurrence if it's a recurring task.