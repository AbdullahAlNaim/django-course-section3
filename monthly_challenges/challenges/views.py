from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def monthly_challenge(request, month):
  challenge_text = None
  if month == 'january':
      challenge_text = '<h1>exercise daily</h1>'
  elif month == 'february':
      challenge_text = '<h1>eat clean daily</h1>'
  elif month == 'march':
      challenge_text = '<h1>run 1 mile a day</h1>'
  else: 
      challenge_text = '<h1>Sorry I can\'t help you with?</h1>'

  return HttpResponse(challenge_text)
