# ProjectManagement
Django REST API project with appropriate models, views, and serializers
Task Management System API
The Task Management System API is a Django-based RESTful API that allows users to manage projects, tasks, comments, and users within a task management system. It provides various endpoints for different user roles, such as Admin Users, Project Managers, Team Leads, and Team Members, with appropriate authentication and authorization mechanisms.





Admin Users:
GET /api/projects/: List all projects.
POST /api/projects/: Create a new project.
PUT /api/projects/<project_id>/: Update project details.
DELETE /api/projects/<project_id>/: Delete a project.
Project Manager:
GET /api/projects/: List all projects managed by the project manager.
GET /api/projects/<project_id>/: View details of a specific project managed by the project manager.
POST /api/projects/: Create a new project (project manager will be the manager).
PUT /api/projects/<project_id>/: Update project details (project manager can update only their managed projects).
DELETE /api/projects/<project_id>/: Delete a project (project manager can delete only their managed projects).
Team Lead:
GET /api/tasks/: List all tasks assigned to the team lead.
GET /api/tasks/<task_id>/: View details of a specific task assigned to the team lead.
POST /api/tasks/: Create a new task (assignee should be a team member of the team lead).
PUT /api/tasks/<task_id>/: Update task details (team lead can update only tasks assigned to their team).
DELETE /api/tasks/<task_id>/: Delete a task (team lead can delete only tasks assigned to their team).
Team Members:
GET /api/tasks/: List all tasks assigned to the team member.
GET /api/tasks/<task_id>/: View details of a specific task assigned to the team member.
PUT /api/tasks/<task_id>/: Update task details (team member can update only tasks assigned to them).
All Users:
POST /api/comments/: Add a comment to a task.
DELETE /api/comments/<comment_id>/: Delete a comment (users can delete only their own comments).
Authentication
The API uses token-based authentication. To access protected endpoints, obtain an access token by making a POST request to http://127.0.0.1:8000/api/token/. Provide your username and password in the request body to receive the access token.

admin 
username- amdin
password- 123