from django.shortcuts import render

# Create your views here.
def index(requests):

  name = 'KEVIN'
  info={
    'name':'KEVIN',
    'age':21,
    'color':['red', 'black', 'whithe']
  }

  return render(requests, 'articles/index.html', {'info':info})