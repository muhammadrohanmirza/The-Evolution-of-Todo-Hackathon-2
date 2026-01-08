# 📝 Todo In-Memory Python Console Application

A clean, spec-driven, and hackathon-ready **command-line Todo application** built with **Python 3.13+**, following **Spec-Kit Plus** methodology and assisted by **Qwen LLM**.  
This project demonstrates how to design and build a scalable MVP by evolving features from **Basic → Intermediate → Advanced** levels using disciplined software engineering practices.

---

## 🚀 Project Overview

This project is a **console-based todo manager** that stores all tasks **entirely in memory** and focuses on:

- Clear and maintainable architecture  
- Spec-driven development workflow  
- Incremental feature growth  
- Clean, readable, and modular Python code  

The application was developed in **structured phases**, where every feature originated from an approved specification, ensuring consistency between requirements, design, and implementation.  

This approach makes the project easy to explain, easy to evaluate, and ideal for hackathon environments.

---

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
