# Implementation Tasks: Time-Aware and Recurring Tasks

**Feature**: Time-Aware and Recurring Tasks | **Branch**: `003-time-aware-tasks`
**Generated from**: spec.md, plan.md, data-model.md, contracts/, research.md

## Implementation Strategy

Build the time-aware and recurring tasks feature incrementally, starting with the foundational model extensions, followed by service logic, and finally CLI updates. Each user story should be independently testable, with User Story 1 (P1) forming the MVP.

## Dependencies

- US2 (Identify and Display Overdue Tasks) depends on US1 (Assign Due Dates to Tasks)
- US3 (Define Simple Recurring Tasks) depends on US1 (Assign Due Dates to Tasks)

## Parallel Execution Examples

- T005-T007 (Model, Service, CLI for due dates) can be developed in parallel by different developers
- T015-T017 (Model, Service, CLI for recurring tasks) can be developed in parallel after US1 completion

---

## Phase 1: Setup

Initialize project structure and dependencies for the time-aware and recurring tasks feature.

- [X] T001 Create src/models/__init__.py if it doesn't exist
- [X] T002 Create src/services/__init__.py if it doesn't exist
- [X] T003 Create src/cli/__init__.py if it doesn't exist
- [X] T004 Create src/lib/__init__.py if it doesn't exist
- [X] T005 Create tests/unit/models/__init__.py if it doesn't exist
- [X] T006 Create tests/unit/services/__init__.py if it doesn't exist
- [X] T007 Create tests/unit/cli/__init__.py if it doesn't exist
- [X] T008 Create tests/integration/__init__.py if it doesn't exist
- [X] T009 Create tests/contract/__init__.py if it doesn't exist

---

## Phase 2: Foundational Components

Implement foundational components needed by multiple user stories.

- [X] T010 [P] Create date_utils.py in src/services/ with date parsing and comparison functions
- [X] T011 [P] Create validators.py in src/lib/ with date and recurrence pattern validation functions
- [X] T012 [P] Create unit tests for date_utils.py
- [X] T013 [P] Create unit tests for validators.py

---

## Phase 3: User Story 1 - Assign Due Dates to Tasks (Priority: P1)

Power users need to assign due dates to their tasks to prioritize and track deadlines effectively. This enables them to manage their time better and ensures important tasks are completed on schedule.

**Independent Test**: Can be fully tested by creating a task with a due date and verifying it appears in the task list with the date displayed. The feature delivers value by allowing users to track deadlines.

- [X] T014 [US1] Extend Task model in src/models/task.py with due_date and created_at attributes
- [X] T015 [US1] Update Task model validation rules for due_date in src/models/task.py
- [X] T016 [US1] Create unit tests for extended Task model in tests/unit/models/test_task.py
- [X] T017 [US1] Update TaskService to handle due dates in src/services/task_service.py
- [X] T018 [US1] Add create_task method with due_date support in src/services/task_service.py
- [X] T019 [US1] Create unit tests for TaskService due date functionality in tests/unit/services/test_task_service.py
- [X] T020 [US1] Update CLI to support adding tasks with due dates in src/cli/cli.py
- [X] T021 [US1] Update CLI to display due dates in task list in src/cli/cli.py
- [X] T022 [US1] Create unit tests for CLI due date functionality in tests/unit/cli/test_cli.py
- [X] T023 [US1] Create integration test for due date assignment in tests/integration/test_task_service.py

---

## Phase 4: User Story 2 - Identify and Display Overdue Tasks (Priority: P2)

Power users need to quickly identify tasks that have passed their due date so they can prioritize catching up on missed deadlines.

**Independent Test**: Can be tested by creating tasks with past due dates and verifying they are highlighted or grouped separately in the task list. Delivers value by surfacing urgent tasks.

- [X] T024 [US2] Add get_overdue_tasks method to TaskService in src/services/task_service.py
- [X] T025 [US2] Add filter_by_due_date_status method to TaskService in src/services/task_service.py
- [X] T026 [US2] Create unit tests for overdue task functionality in tests/unit/services/test_task_service.py
- [X] T027 [US2] Update CLI to highlight overdue tasks in src/cli/cli.py
- [X] T028 [US2] Update CLI to add overdue filter option in src/cli/cli.py
- [X] T029 [US2] Create unit tests for overdue task display in tests/unit/cli/test_cli.py
- [X] T030 [US2] Create integration test for overdue task identification in tests/integration/test_task_service.py

---

## Phase 5: User Story 3 - Define Simple Recurring Tasks (Priority: P3)

Power users need to create recurring tasks (daily, weekly) to represent routine activities without having to manually create them each time.

**Independent Test**: Can be tested by creating a recurring task and verifying it generates future occurrences. Delivers value by eliminating the need to recreate routine tasks.

- [X] T031 [US3] Create RecurrencePattern model in src/models/task.py
- [X] T032 [US3] Add recurrence_pattern attribute to Task model in src/models/task.py
- [X] T033 [US3] Add validation rules for recurrence_pattern in src/models/task.py
- [X] T034 [US3] Create unit tests for RecurrencePattern model in tests/unit/models/test_task.py
- [X] T035 [US3] Add recurrence pattern handling to TaskService in src/services/task_service.py
- [X] T036 [US3] Implement recurring task generation logic in src/services/task_service.py
- [X] T037 [US3] Create unit tests for recurring task functionality in tests/unit/services/test_task_service.py
- [X] T038 [US3] Update CLI to support creating recurring tasks in src/cli/cli.py
- [X] T039 [US3] Update CLI to handle recurring task completion in src/cli/cli.py
- [X] T040 [US3] Create unit tests for recurring task CLI functionality in tests/unit/cli/test_cli.py
- [X] T041 [US3] Create integration test for recurring task generation in tests/integration/test_task_service.py

---

## Phase 6: Polish & Cross-Cutting Concerns

Address cross-cutting concerns and finalize the implementation.

- [X] T042 Update README.md with new due date and recurring task features
- [ ] T043 Add contract tests for new API endpoints in tests/contract/test_task_api.py
- [X] T044 Perform end-to-end testing of all user stories
- [X] T045 Update documentation with usage examples for new features
- [X] T046 Run all tests to ensure no regressions in basic functionality
- [X] T047 Perform code review and address feedback
- [X] T048 Refactor any duplicated code across the new modules