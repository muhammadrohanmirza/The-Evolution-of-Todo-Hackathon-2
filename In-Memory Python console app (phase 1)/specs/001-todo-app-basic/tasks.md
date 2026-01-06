# Implementation Tasks: Todo In-Memory Python Console App

**Feature**: Todo In-Memory Python Console App - Basic Level
**Branch**: `001-todo-app-basic`
**Input**: Feature specification and implementation plan from `/specs/001-todo-app-basic/`

## Phase 1: Setup

- [X] T001 Create project structure with src/, specs_history/, and README.md
- [X] T002 Initialize Python project with UV (uv init, uv venv)
- [X] T003 Create initial git repository and commit constitution.md
- [X] T004 Create specs_history directory and copy spec.md as specify_v1.md

## Phase 2: Foundational

- [X] T005 [P] Create src/__init__.py file
- [X] T006 [P] Create models.py with Task dataclass containing id, title, description, complete
- [X] T007 [P] Create todo_manager.py with TodoManager class skeleton
- [X] T008 Create main.py with basic structure and menu loop

## Phase 3: User Story 1 - Add New Tasks (Priority: P1)

- [X] T009 [US1] Implement Task creation with auto-incrementing ID in TodoManager
- [X] T010 [US1] Implement add_task method in TodoManager to add tasks with title and optional description
- [X] T011 [US1] Add input validation for empty titles in add_task method
- [X] T012 [US1] Create CLI menu option for adding tasks in main.py
- [X] T013 [US1] Test adding a task with title and description, verify it appears with unique ID and incomplete status
- [X] T014 [US1] Test adding a task with only a title, verify it appears with empty description
- [X] T015 [US1] Test adding a task with empty title, verify appropriate error message

## Phase 4: User Story 2 - View Task List (Priority: P1)

- [X] T016 [US2] Implement get_all_tasks method in TodoManager to return all tasks
- [X] T017 [US2] Implement formatted display of tasks with ID, title, status indicator ([❌] or [✔️]), and description
- [X] T018 [US2] Handle empty task list case with appropriate message
- [X] T019 [US2] Create CLI menu option for viewing tasks in main.py
- [X] T020 [US2] Test viewing task list with multiple tasks, verify proper display format
- [X] T021 [US2] Test viewing empty task list, verify appropriate message
- [X] T022 [US2] Test viewing task list with both completed and incomplete tasks, verify status indicators

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P2)

- [X] T023 [US3] Implement mark_task_complete method in TodoManager to toggle completion status by ID
- [X] T024 [US3] Add validation to ensure task exists before marking as complete
- [X] T025 [US3] Create CLI menu option for marking tasks as complete in main.py
- [X] T026 [US3] Test marking an incomplete task as complete, verify status change
- [X] T027 [US3] Test marking a complete task again, verify status toggles back to incomplete
- [X] T028 [US3] Test marking a task with invalid ID, verify appropriate error message

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

- [X] T029 [US4] Implement update_task method in TodoManager to modify title or description by ID
- [X] T030 [US4] Add validation to ensure task exists before updating
- [X] T031 [US4] Create CLI menu option for updating tasks in main.py
- [X] T032 [US4] Test updating task title, verify change is reflected
- [X] T033 [US4] Test updating task description, verify change is reflected
- [X] T034 [US4] Test updating a task with invalid ID, verify appropriate error message

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

- [X] T035 [US5] Implement delete_task method in TodoManager to remove tasks by ID
- [X] T036 [US5] Add validation to ensure task exists before deleting
- [X] T037 [US5] Ensure other task IDs remain unchanged after deletion
- [X] T038 [US5] Create CLI menu option for deleting tasks in main.py
- [X] T039 [US5] Test deleting a task from multiple tasks, verify it's removed and others remain
- [X] T040 [US5] Test deleting the only task in the list, verify list becomes empty
- [X] T041 [US5] Test deleting a task with invalid ID, verify appropriate error message

## Phase 8: Polish & Cross-Cutting Concerns

- [X] T042 Add comprehensive input validation and error handling throughout the application
- [X] T043 Implement graceful handling of invalid inputs with helpful error messages
- [X] T044 Add docstrings to all functions and classes
- [X] T045 Write README.md with UV setup and run instructions
- [X] T046 Perform manual testing of all 5 features to ensure they work without crashes
- [X] T047 Verify tasks persist during session and clear status indicators are displayed
- [X] T048 Run full demo to ensure all features work together properly
- [X] T049 Commit all files to the repository
- [X] T050 Ensure repository is public and complete with all required files

## Dependencies

- User Story 1 (Add Tasks) and User Story 2 (View Tasks) can be developed in parallel after foundational tasks are complete
- User Story 3 (Mark Complete), User Story 4 (Update), and User Story 5 (Delete) depend on foundational tasks and can be developed in parallel after US1 and US2

## Parallel Execution Examples

- Tasks T005-T007 can be executed in parallel as they create separate files
- User Stories 3, 4, and 5 can be developed in parallel after US1 and US2 are complete
- Testing tasks within each user story can be done independently

## Implementation Strategy

- MVP first: Implement User Story 1 (Add Tasks) and User Story 2 (View Tasks) to have a basic working application
- Incremental delivery: Add each additional feature one by one, testing as you go
- Focus on core functionality first, then add error handling and polish