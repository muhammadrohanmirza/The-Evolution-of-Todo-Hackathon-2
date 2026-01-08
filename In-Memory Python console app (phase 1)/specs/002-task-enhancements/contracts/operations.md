# API Contract: Task Enhancement Operations

## Overview
This document defines the contract for the new operations added to the Todo In-Memory Python Console Application for task organization and usability enhancements.

## Operations

### 1. Update Task Priority
- **Operation**: Update an existing task's priority level
- **Input**: Task ID, Priority Level (HIGH, MEDIUM, LOW)
- **Output**: Confirmation of update or error message
- **Errors**: Invalid task ID, Invalid priority level

### 2. Search Tasks
- **Operation**: Find tasks containing a keyword in title or description
- **Input**: Search keyword
- **Output**: List of matching tasks
- **Errors**: None (returns empty list if no matches)

### 3. Filter Tasks
- **Operation**: Filter tasks by completion status or priority
- **Input**: Filter criteria (status: all/complete/incomplete, priority: all/high/medium/low)
- **Output**: List of tasks matching the criteria
- **Errors**: Invalid filter criteria

### 4. Sort Tasks
- **Operation**: Sort tasks by specified criteria
- **Input**: Sort criteria (field: title/priority/status, order: ascending/descending)
- **Output**: Sorted list of tasks
- **Errors**: Invalid sort criteria