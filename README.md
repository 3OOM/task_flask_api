# Task Management System API
---
## Overview

This project is a RESTful API for a Task Management System, built using Flask and PostgreSQL. The API allows users to register, authenticate, manage tasks, and filter/search tasks. The project is Dockerized, making it easy to deploy and manage.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Assumptions and Approach](#assumptions-and-approach)
- [Troubleshooting](#troubleshooting)


## Project Structure

```plaintext
task_management/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── utils.py
│   └── config.py
│
├── migrations/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── tests/
    ├── test_auth.py
    ├── test_tasks.py
    └── __init__.py
```

## Features

- **User Registration and Authentication**
  - Secure user registration with password hashing.
  - JWT-based authentication for secure access to resources.

- **Task Management**
  - CRUD operations for tasks (Create, Read, Update, Delete).
  - Task assignment to specific users.
  - Filtering and searching of tasks based on status, priority, and due date.

- **Dockerized**
  - The application is containerized using Docker, making it easy to run in any environment.

## Installation

### Prerequisites

- Docker and Docker Compose installed on your local machine.
- Basic knowledge of Docker and Flask.

### Steps to Install

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/task_management.git
   cd task_management
   ```

2. **Build and Start the Docker Containers**

   ```bash
   docker-compose up --build
   ```

   This will build the Docker images and start the containers.

3. **Initialize the Database**

   Run the following commands to set up the database:

   ```bash
   docker-compose exec web flask db init
   docker-compose exec web flask db migrate -m "Initial migration"
   docker-compose exec web flask db upgrade
   ```

## Running the Application

- The application will be available at `http://localhost:5000`.
- pgAdmin will be accessible at `http://localhost:5050` with the following credentials:
  - **Email**: `admin@admin.com`
  - **Password**: `admin`

## API Documentation

### Postman Collection

A Postman collection is provided in the repository under the `documentation` folder. You can import it into Postman to explore the API endpoints.

### Example Endpoints

1. **User Registration**

   ```http
   POST /api/register
   ```

   **Request Body**:

   ```json
   {
       "username": "user1",
       "password": "password123"
   }
   ```

2. **User Login**

   ```http
   POST /api/login
   ```

   **Request Body**:

   ```json
   {
       "username": "user1",
       "password": "password123"
   }
   ```

3. **Create Task**

   ```http
   POST /api/tasks
   ```

   **Request Body**:

   ```json
   {
       "title": "New Task",
       "description": "Task description",
       "status": "Todo",
       "priority": "High",
       "due_date": "2024-07-31"
   }
   ```

4. **Get Tasks**

   ```http
   GET /api/tasks
   ```

5. **Update Task**

   ```http
   PUT /api/tasks/{taskId}
   ```

   **Request Body**:

   ```json
   {
       "title": "Updated Task",
       "description": "Updated description",
       "status": "In Progress",
       "priority": "Medium"
   }
   ```

6. **Delete Task**

   ```http
   DELETE /api/tasks/{taskId}
   ```

## Testing

Unit and integration tests are located in the `tests/` directory. To run the tests, use the following command:

```bash
docker-compose exec web pytest
```

## Assumptions and Approach

### Assumptions

- The API is designed for a single user type, with role-based access control as a future enhancement.
- The database schema is relatively simple and assumes that users will not be deleted, hence no cascading deletes.
- The JWT tokens are valid for a reasonable time, assuming regular token refreshes by clients.

### Approach

- **Modularity**: The project is designed with a modular approach, separating concerns such as routes, models, and configuration.
- **Security**: Passwords are securely hashed using `werkzeug.security`, and JWTs are used for authentication to protect API endpoints.
- **Extensibility**: The project is structured to allow easy extension, such as adding more models or integrating more features like role-based access control or pagination.
- **Dockerization**: Docker is used to ensure consistent environments across different stages (development, testing, production).

## Troubleshooting

- **Database Connection Issues**: Ensure that the `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` values in the `docker-compose.yml` file match your configuration.
- **JWT Authentication Issues**: Verify that the JWT_SECRET_KEY in the `app/config.py` is correctly set.


---

