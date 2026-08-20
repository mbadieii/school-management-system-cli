# School Management System

A command-line school management system built with Python to manage essential school information, including students, teachers, courses, and school data. The application provides a simple and interactive terminal-based interface that allows users to work with different entities within a school management environment.

The project is designed around fundamental Python programming concepts and provides a structured approach to organizing and managing data during runtime. It focuses on creating a clear and functional command-line application while keeping the implementation simple and easy to understand.

## Models

The following tables describe the main models of the system, including their attributes, methods, and relationships.

### Course

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Course identifier |
| `name` | `str` | Course name |
| `units` | `int` | Number of course units |
| `score` | `float` | Course score |

| Method | Parameters |
|---|---|
| `__init__()` | `id`, `name`, `units` |

### Student

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Student identifier |
| `name` | `str` | Student's first name |
| `family` | `str` | Student's family name |
| `courses` | `list[Course]` | Courses taken by the student |

| Method | Parameters |
|---|---|
| `__init__()` | `id`, `name`, `family` |

### Teacher

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Teacher identifier |
| `name` | `str` | Teacher's first name |
| `family` | `str` | Teacher's family name |
| `grade` | `str` | Teacher's grade |
| `courses` | `list[Course]` | Courses taught by the teacher |

| Method | Parameters |
|---|---|
| `__init__()` | `id`, `name`, `family`, `grade` |

### Classroom

| Attribute | Type | Description |
|---|---|---|
| `id` | `int` | Classroom identifier |
| `name` | `str` | Classroom name |
| `course` | `Course` | Course assigned to the classroom |
| `teacher` | `Teacher` | Teacher assigned to the classroom |
| `students` | `list[Student]` | Students in the classroom |

| Method | Parameters |
|---|---|
| `__init__()` | `id`, `name` |

### School

| Attribute | Type | Description |
|---|---|---|
| `name` | `str` | School name |
| `courses` | `list[Course]` | Courses offered by the school |
| `teachers` | `list[Teacher]` | Teachers in the school |
| `students` | `list[Student]` | Students in the school |

| Method | Parameters |
|---|---|
| `__init__()` | `name` |

### Relationships

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