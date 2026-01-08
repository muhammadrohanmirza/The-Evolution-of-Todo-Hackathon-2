# Data Model: Task Organization and Usability Enhancements

## Extended Task Entity

### Fields
- **id**: Unique integer identifier (existing field, unchanged)
- **title**: String representing the task title (existing field, unchanged)
- **description**: Optional string with detailed task information (existing field, unchanged)
- **complete**: Boolean indicating completion status (existing field, unchanged)
- **priority**: Enum value representing priority level (HIGH, MEDIUM, LOW) (new field)

### Relationships
- No new relationships introduced; remains a standalone entity

### Validation Rules
- **priority**: Must be one of the predefined enum values (HIGH, MEDIUM, LOW)
- **id**: Must be unique across all tasks
- **title**: Cannot be empty or null

### State Transitions
- **complete**: Can transition from False to True (mark as complete) or True to False (mark as incomplete)
- **priority**: Can be updated to any of the valid enum values at any time

## Priority Enum

### Values
- **HIGH**: Represents high priority tasks requiring immediate attention
- **MEDIUM**: Represents medium priority tasks of standard importance
- **LOW**: Represents low priority tasks that can be deferred

## Search Query Entity (Conceptual)

### Fields
- **keyword**: String to search for in task titles and descriptions
- **search_scope**: Enum indicating where to search (TITLE_ONLY, DESCRIPTION_ONLY, BOTH)

## Filter Criteria Entity (Conceptual)

### Fields
- **status_filter**: Enum for completion status (ALL, COMPLETE_ONLY, INCOMPLETE_ONLY)
- **priority_filter**: Enum for priority level (ALL, HIGH_ONLY, MEDIUM_ONLY, LOW_ONLY)

## Sort Criteria Entity (Conceptual)

### Fields
- **sort_field**: Enum indicating which field to sort by (TITLE, PRIORITY, COMPLETION_STATUS)
- **sort_order**: Enum for sort direction (ASCENDING, DESCENDING)