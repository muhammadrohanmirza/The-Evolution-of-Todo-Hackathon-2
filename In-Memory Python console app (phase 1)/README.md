<<<<<<< HEAD
# 📝 Todo In-Memory Python Console Application

A clean, spec-driven, and hackathon-ready **command-line Todo application** built with **Python 3.13+**, following **Spec-Kit Plus** methodology and assisted by **Qwen LLM**.  
This project demonstrates how to design and build a scalable MVP by evolving features from **Basic → Intermediate → Advanced** levels using disciplined software engineering practices.
=======
# Todo Application with Time-Aware and Recurring Tasks

This is an in-memory Python console application that allows users to manage their tasks with advanced time-aware and recurring capabilities.
>>>>>>> 61ca486 (update repo)

---

<<<<<<< HEAD
## 🚀 Project Overview

This project is a **console-based todo manager** that stores all tasks **entirely in memory** and focuses on:

- Clear and maintainable architecture  
- Spec-driven development workflow  
- Incremental feature growth  
- Clean, readable, and modular Python code  
=======
- **Add Tasks**: Create new tasks with optional descriptions
- **Due Dates**: Assign due dates to tasks to track deadlines
- **Overdue Task Identification**: Automatically identify and display overdue tasks
- **Recurring Tasks**: Create tasks that repeat on a daily, weekly, monthly, or yearly basis
- **Task Management**: Update, delete, and mark tasks as complete/incomplete
- **Filtering**: Filter tasks by due date status (overdue, upcoming, none)
- **Search**: Search tasks by title or description

## Installation

1. Make sure you have Python 3.13+ installed
2. Clone the repository
3. Navigate to the project directory
4. Run the application with `python main.py`
>>>>>>> 61ca486 (update repo)

The application was developed in **structured phases**, where every feature originated from an approved specification, ensuring consistency between requirements, design, and implementation.  

<<<<<<< HEAD
This approach makes the project easy to explain, easy to evaluate, and ideal for hackathon environments.
=======
Run the application:

```bash
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
>>>>>>> 61ca486 (update repo)

---

<<<<<<< HEAD
## 🎯 Key Objectives

- Demonstrate **Spec-Driven Development** using Spec-Kit Plus  
- Build a fully functional and usable **CLI Todo Application**  
- Maintain simplicity while supporting advanced task behaviors  
- Follow clean code and modular design principles  
- Stay hackathon-safe: no over-engineering, no unnecessary dependencies  

---

## 🧱 Feature Breakdown

### ✅ Basic Level (Core MVP)

Essential functionality required for any todo application:

- Add new tasks with title and description  
- View all tasks with clear completion status indicators  
- Update existing task details  
- Delete tasks by unique ID  
- Mark tasks as complete or incomplete  

---

### 🟡 Intermediate Level (Organization & Usability)

Enhancements that improve task organization and usability:

- Task priorities (High / Medium / Low)  
- Categories or tags for better organization  
- Search tasks by keyword (title or description)  
- Filter tasks by status or priority  
- Sort tasks alphabetically or by priority  

---

### 🔴 Advanced Level (Intelligent Behavior)

Time-aware and recurring task capabilities:

- Assign due dates (date or date-time) to tasks  
- Identify and display overdue tasks  
- Define recurring tasks (e.g., daily or weekly)  
- Automatically generate the next occurrence when a recurring task is completed  

> ⚠️ **Note:**  
> All advanced features remain fully **in-memory and deterministic**.  
> No background schedulers, notifications, databases, or persistence are used.

---

## 🧠 Architecture & Design Principles

- **Spec-Driven Development** – No code is written without an approved specification  
- **Modular Design** – Clear separation between models, services, and CLI logic  
- **In-Memory Storage** – Simple Python data structures, no persistence  
- **Clean Code** – PEP-8 compliant, readable, and maintainable  
- **Incremental Development** – Each level builds safely on the previous one  

---

## 🛠️ Technology Stack

- **Python** 3.13+  
- **UV** package manager  
- **Spec-Kit Plus** for specification management  
- **Qwen LLM** for specification authoring and refinement  
- **Python Standard Library only**  

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

git clone <your-repository-url>
cd todo-in-memory-python-app

### 2️⃣ Install Dependencies (using UV)
uv sync

### 3️⃣ Run the Application
python src/main.py

---

## 🧪 Testing & Validation

- Core logic is validated using deterministic checks

- Manual testing ensures all success criteria are met

- Testing scope is intentionally lightweight to align with hackathon constraints

- No external testing frameworks are required

---

## 🏁 Why This Project Stands Out

- Fully spec-driven, not ad-hoc coding

- Clear evolution from MVP to advanced features

- Strong focus on clarity, maintainability, and scope control

- Hackathon-ready: easy to demo and easy to explain

- Demonstrates real-world engineering discipline in a simple console app

---

## 📜 License

- This project is created for educational and hackathon purposes.

---

## 🙌 Acknowledgements

- Spec-Kit Plus for structured specification workflows

- Qwen LLM for assistance in specification authoring

- The Python open-source community ❤️

---
=======
The application follows a modular design:

- `src/models/task.py`: Contains the Task and RecurrencePattern data models
- `src/services/task_service.py`: Business logic for task operations
- `src/services/date_utils.py`: Date and time utility functions
- `src/lib/validators.py`: Validation functions for dates and recurrence patterns
- `src/cli/cli.py`: Command-line interface
- `main.py`: Application entry point

## Testing

Unit tests are located in the `tests/` directory:
- `tests/unit/models/`: Tests for data models
- `tests/unit/services/`: Tests for service layer
- `tests/unit/lib/`: Tests for utility functions
- `tests/integration/`: Integration tests

To run the tests:
```bash
python -m pytest
```

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
>>>>>>> 61ca486 (update repo)
