from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import User, Project, Task, Comment
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer

# Admin Users
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def project_list_create(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def project_detail_update_delete(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=404)

    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=204)

# Project Manager
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def project_manager_project_list_create(request):
    if request.method == 'GET':
        projects = Project.objects.filter(project_manager=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project_manager=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def project_manager_project_detail_update_delete(request, project_id):
    try:
        project = Project.objects.get(pk=project_id, project_manager=request.user)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found '}, status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=204)

# Team Lead
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def team_lead_task_list(request):
    tasks = Task.objects.filter(assignee=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def team_lead_task_detail_update_delete(request, task_id):
    try:
        task = Task.objects.get(pk=task_id, assignee=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)

# Team Member
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def team_member_task_list(request):
    tasks = Task.objects.filter(assignee=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def team_member_task_detail_update(request, task_id):
    try:
        task = Task.objects.get(pk=task_id, assignee=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# All Users
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(commented_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id, commented_by=request.user)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment not found '}, status=404)

    comment.delete()
    return Response(status=204)
