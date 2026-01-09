# Data Model: Time-Aware and Recurring Tasks

## Task Entity

The existing Task entity will be extended with additional attributes to support time-aware and recurring functionality:

### Attributes
- **id**: Unique integer identifier (existing)
- **title**: String representing the task title (existing)
- **description**: Optional string with detailed task information (existing)
- **completed**: Boolean indicating completion status (existing)
- **due_date**: Optional datetime object representing the task deadline (new)
- **recurrence_pattern**: Optional RecurrencePattern object defining repetition rules (new)
- **created_at**: datetime object representing when the task was created (new)
- **completed_at**: Optional datetime object representing when the task was completed (new)

### Validation Rules
- due_date must be a valid datetime object or None
- recurrence_pattern must be a valid RecurrencePattern object or None
- If recurrence_pattern is set, the task should have a due_date
- completed_at must be None if completed is False

## RecurrencePattern Entity

### Attributes
- **frequency**: String representing the recurrence frequency ("daily", "weekly", "monthly", "yearly") (new)
- **interval**: Integer representing how often the pattern repeats (e.g., every 2 weeks) (new)
- **end_condition**: Optional object defining when recurrence ends (new)
  - **type**: String ("after_occurrences", "on_date", "never") (new)
  - **value**: Integer or datetime depending on type (new)

### Validation Rules
- frequency must be one of the allowed values
- interval must be a positive integer
- end_condition.type must be one of the allowed values
- if end_condition.type is "after_occurrences", end_condition.value must be a positive integer
- if end_condition.type is "on_date", end_condition.value must be a valid datetime

## State Transitions

### Task Completion with Recurrence
1. When a task with recurrence_pattern is marked as complete:
   - A new task is created with the same properties
   - The new task's due_date is calculated based on the recurrence pattern
   - The original task is marked as completed and its completion date is recorded

### Due Date Status
- **Upcoming**: due_date is in the future
- **Overdue**: due_date is in the past and task is not completed
- **None**: task has no due_date

## Relationships
- A Task may have zero or one RecurrencePattern
- A RecurrencePattern belongs to exactly one Task