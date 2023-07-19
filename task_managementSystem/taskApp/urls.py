
from django.urls import path
from .views import (
    project_list_create, project_detail_update_delete,
    project_manager_project_list_create, project_manager_project_detail_update_delete,
    team_lead_task_list, team_lead_task_detail_update_delete,
    team_member_task_list, team_member_task_detail_update,
    comment_create, comment_delete,
)

urlpatterns = [
    # Admin Users
    path('api/projects/', project_list_create, name='project-list'),
    path('api/projects/<int:project_id>/', project_detail_update_delete, name='project-detail'),
    # Project Manager
    path('api/project-manager/projects/', project_manager_project_list_create, name='project-manager-project-list'),
    path('api/project-manager/projects/<int:project_id>/', project_manager_project_detail_update_delete, name='project-manager-project-detail'),
    # Team Lead
    path('api/team-lead/tasks/', team_lead_task_list, name='team-lead-task-list'),
    path('api/team-lead/tasks/<int:task_id>/', team_lead_task_detail_update_delete, name='team-lead-task-detail'),

    # Team Member
    path('api/team-member/tasks/', team_member_task_list, name='team-member-task-list'),
    path('api/team-member/tasks/<int:task_id>/', team_member_task_detail_update, name='team-member-task-detail'),


    # All Users
    path('api/comments/', comment_create, name='comment-create'),
    path('api/comments/<int:comment_id>/', comment_delete, name='comment-delete'),
]
