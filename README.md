# RDash

RDash is a web application built using Django that allows users to create, assign, and manage tasks effectively. This README provides an overview of the application's features and instructions on how to get started.

## Features

1. **Task Creation**
   - Users can create tasks with the following details:
     - Title
     - Description
     - Due Date
     - Assignee(s)

2. **Task Assignment**
   - Any task can be assigned to at least one user or more users.

3. **Task Viewing**
   - Users can see all the tasks assigned to them.
   - Users can see all the tasks created by them.

4. **Task Filtering**
   - Users can filter tasks based on various criteria:
     - Due Date
     - Creator
     - Assignee

5. **Email Notifications**
   - Users receive email notifications when a new task is assigned to them.

## Django Models

### Task Model

- Fields:
  - Id (Auto-generated)
  - Title
  - Description
  - Due Date
  - Assignee(s)
  - Created By (Username fetched from session cookie by Django)
  - Creation Time

### User Model (Extended from Django's AbstractUser)

- Additional Fields:
  - Email
  - Creation Time

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django (3.2 or higher)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/harshalgadhe/Rdash.git
   cd Rdash
   ```
2. Run migrations:

```bash
python manage.py migrate
```

3. Create a superuser (admin) account:

```bash
python manage.py createsuperuser
```

4. Start the development server:

```bash
python manage.py runserver
```
