# School Management System

A command-line school management system built with Python to manage essential school information, including students, teachers, courses, classrooms, and school data. The application provides a simple and interactive terminal-based interface that allows users to manage different entities within a school management environment.

The project is designed around fundamental Python programming concepts, including classes, objects, lists, methods, object comparison, and command-line interaction. It focuses on creating a structured and functional application while keeping the implementation simple and easy to understand.

## Models

The following tables describe the main models of the system, including their attributes, methods, and relationships.

### Course

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Course identifier |
| `name` | `str` | Course name |
| `units` | `int` | Number of course units |
| `score` | `float` | Course score |

| Method | Parameters | Description |
|---|---|---|
| `__init__()` | `id`, `name`, `units` | Initializes a course |
| `__str__()` | - | Returns a string representation of the course |
| `__eq__()` | `other` | Compares the course with another object |

### Student

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Student identifier |
| `name` | `str` | Student's first name |
| `family` | `str` | Student's family name |
| `courses` | `list[Course]` | Courses taken by the student |

| Method | Parameters | Description |
|---|---|---|
| `__init__()` | `id`, `name`, `family` | Initializes a student |
| `__str__()` | - | Returns a string representation of the student |
| `__eq__()` | `other` | Compares the student with another object |

### Teacher

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Teacher identifier |
| `name` | `str` | Teacher's first name |
| `family` | `str` | Teacher's family name |
| `grade` | `str` | Teacher's grade |
| `courses` | `list[Course]` | Courses taught by the teacher |

| Method | Parameters | Description |
|---|---|---|
| `__init__()` | `id`, `name`, `family`, `grade` | Initializes a teacher |
| `__str__()` | - | Returns a string representation of the teacher |
| `__eq__()` | `other` | Compares the teacher with another object |

### Classroom

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Classroom identifier |
| `name` | `str` | Classroom name |
| `course` | `Course` | Course assigned to the classroom |
| `teacher` | `Teacher` | Teacher assigned to the classroom |
| `students` | `list[Student]` | Students in the classroom |

| Method | Parameters | Description |
|---|---|---|
| `__init__()` | `id`, `name` | Initializes a classroom |

### School

| Attribute | Type | Description |
|---|---|---|
| `name` | `str` | School name |
| `courses` | `list[Course]` | Courses offered by the school |
| `teachers` | `list[Teacher]` | Teachers in the school |
| `students` | `list[Student]` | Students in the school |

| Method | Parameters | Description |
|---|---|---|
| `__init__()` | `name` | Initializes a school |
| `show_students()` | - | Displays all students |
| `show_teachers()` | - | Displays all teachers |
| `show_courses()` | - | Displays all courses |
| `add_student()` | `s` | Adds a student if they do not already exist |
| `add_teacher()` | `t` | Adds a teacher if they do not already exist |
| `add_course()` | `c` | Adds a course if it does not already exist |
| `delete_student()` | `id` | Removes a student |
| `delete_teacher()` | `id` | Removes a teacher |
| `delete_course()` | `id` | Removes a course |

## Relationships

| Class | Relationship | Related Class |
|---|---|---|
| `Student` | takes | `Course` |
| `Teacher` | teaches | `Course` |
| `Classroom` | has | `Course` |
| `Classroom` | has | `Teacher` |
| `Classroom` | contains | `Student` |
| `School` | offers | `Course` |
| `School` | employs | `Teacher` |
| `School` | enrolls | `Student` |

## Features

- Add students, teachers, and courses
- Display students, teachers, and courses
- Edit student information
- Edit teacher information
- Edit course information
- Delete students, teachers, and courses
- Prevent adding duplicate students, teachers, and courses
- Compare objects using `__eq__()`
- Display object information using `__str__()`
- Navigate through the application using a command-line menu