# OOP warpper

A **console-based mini project** built using **Python** to demonstrate core **Object-Oriented Programming (OOP)** concepts such as **Inheritance, Encapsulation, Polymorphism, Abstraction (via properties)**, and the modern ``** control structure**.

This project is ideal for **beginners and students** who want a clean, practical example of OOP for learning or showcasing on GitHub.

---

##   Features

* Create and manage:

  *  Person
  *  Employee
  *  Manager
* Demonstrates OOP principles:

  * Inheritance (`Person → Employee → Manager`)
  * Encapsulation (private attributes & properties)
  * Polymorphism (method overriding)
* Menu-driven interactive console program
* Clean and readable code structure

---

##  Technologies Used

* Object-Oriented Programming

---

##  Class Structure

### 1. Person Class

* Attributes:

  * `name`
  * `age`
* Method:

  * `display()` – shows basic details

### 2. Employee Class (inherits Person)

* Additional Attributes:

  * `__emp_id` (private)
  * `__salary` (private)
* Uses **@property** and **@setter** for salary
* Overrides `display()` method

### 3.Manager Class (inherits Employee)

* Additional Attribute:

  * `department`
* Overrides `display()` method

---

##  Menu Operations

```
1. Create Person
2. Create Employee
3. Create Manager
4. Show Details
5. Exit
```

Each option allows the user to interactively create objects or display stored data.

---

##  How to Run

1. Clone this repository:

```bash
git clone https://github.com/tejpatel1034-lang/oopwarpper
```

3. Navigate to the project folder:

```bash
cd oopwarapper
```

4. Run the program:

```bash
python main.py
```

---

##  Sample Output

```
---Python OOP Project: Employee Management System---

Choose an operation:
1. Create Person
2. Create Employee
3. Create Manager
4. Show Details
5. Exit
```

---

##  Learning Outcomes

* Strong understanding of Python OOP basics
* Practical use of inheritance and method overriding
* Real-world style project structure
* Experience with Python's modern `match-case` syntax

---

## Author By:

Patel Tej
