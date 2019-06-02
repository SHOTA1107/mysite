from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Hello, world. You're at the polls index")

def detail(request, question_id):
  return HttpResponse("You're looking at Question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %2."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're looking at Question %s." % question_id)
