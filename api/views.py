from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from .models import Note
from .serializers import NoteSerialzer



@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-created')
    serializer = NoteSerialzer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, id):
    note = Note.objects.get(id = id)
    serializer = NoteSerialzer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def newNote(request):
    res = json.dumps(request.data)
    data = json.loads(res)
    note = Note.objects.create(note = data['note'])
    return Response('New Note Added')

@api_view(['DELETE'])
def deleteNote(request, id):
    note = Note.objects.get(id = id)
    note.delete()
    return Response('Note deleted')


@api_view(['PUT'])
def updateNote(request, id):
    data = request.data
    note = Note.objects.get(id = id)
    serializer = NoteSerialzer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)