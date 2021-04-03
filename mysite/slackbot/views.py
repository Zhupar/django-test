
from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    #Добавьте в словарь workspace и его token
    SLACK_TOKEN = {
        'TestSlackBot': 'xoxb-1901386753110-1914773166133-ZV2AvfnemwZSM3Ow1RdrIAZG',
    }

    # Добавьте в список каналы
    SLACK_CHANNELS = ['new', 'test', 'general']
    return render(request, 'slackbot/index.html', { 'workspaces': SLACK_TOKEN, 'channels': SLACK_CHANNELS})
