# Research: Time-Aware and Recurring Tasks

## Decision: Representation of due dates (date vs datetime) and validation rules
**Rationale**: The feature specification allows for both date and date-time, but for simplicity and consistency with the existing console application, we'll use datetime objects with date parsing that defaults to the start of the day if no time is specified. This provides flexibility while maintaining simplicity.
**Alternatives considered**: 
- Date-only objects (simpler but less flexible)
- String storage with parsing (more complex, harder to validate)

## Decision: How overdue tasks are identified and displayed
**Rationale**: Overdue tasks will be identified by comparing the due date with the current datetime. In the CLI, overdue tasks will be displayed with a special indicator (e.g., [OVERDUE]) and potentially highlighted in red text.
**Alternatives considered**:
- Separate overdue task list (would require more complex UI)
- Color coding only (might not be accessible)

## Decision: Recurring task model (interval-based vs rule-based recurrence)
**Rationale**: For simplicity and to meet the requirements of daily/weekly patterns, we'll implement an interval-based recurrence model. This stores a frequency (daily, weekly) and interval count. This is simpler than a full rule-based system (like iCalendar) but sufficient for the requirements.
**Alternatives considered**:
- Full rule-based recurrence (e.g., cron expressions) - too complex for this feature
- Fixed patterns only (daily, weekly) - too limiting if we want to extend later

## Decision: Strategy for generating the next task occurrence upon completion
**Rationale**: When a recurring task is marked as complete, the system will create a new task with the same properties but with the due date adjusted according to the recurrence pattern. The original task will be marked as complete and not deleted to maintain history.
**Alternatives considered**:
- Modifying the existing task (would lose completion history)
- Creating a separate recurrence scheduler (violates constraint of no background schedulers)

## Decision: Date input format and parsing
**Rationale**: The system will accept multiple common date formats (e.g., YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY) and use Python's dateutil.parser for flexible parsing, with validation to ensure dates are reasonable.
**Alternatives considered**:
- Single strict format (user-unfriendly)
- Custom parsing (error-prone and complex)

## Decision: Handling of recurring tasks that would create past-due occurrences
**Rationale**: When completing a recurring task, if the next occurrence would be in the past, the system will create it with the next valid future date based on the recurrence pattern.
**Alternatives considered**:
- Skip to the next valid occurrence (might miss intended repetition)
- Create with past date (would immediately be overdue)