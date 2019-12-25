# -*- coding: utf-8 -*-

"""
__init__.py

Crée par Flavien-hugs - 2019/12/05/.
Copyright (c) 2019 unsta. All rights reserved.

"""
__author__ = 'Flavien-hugs <flavienhugs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta projet youtube_api_search'


import requests
from django.conf import settings
from django.shortcuts import render, redirect
from isodate import parse_duration


# Create your views here.

def index(request):
    # tableau vide de recuperation de toutes les videos retrouvees
    videos = []

    if request.method == 'POST':
        url_recherche = 'https://www.googleapis.com/youtube/v3/search'
        url_video = 'https://www.googleapis.com/youtube/v3/videos'

        # parametre de recherche
        params_recherche = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 8,
            'type' : 'video'
        }
        r = requests.get(url_recherche, params=params_recherche)
        resultats = r.json()['items']

        # tableau vide de recuperation de toutes les videos retrouvees
        ids_video = []
        for resultat in resultats:
            ids_video.append(resultat['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ids_video[0]}')

        # parametre de recherche videos
        params_videos = {
            'part' : 'snippet,contentDetails,statistics',
            'id' : ','.join(ids_video),
            'key' : settings.YOUTUBE_DATA_API_KEY,
        }
        r = requests.get(url_video, params=params_videos)
        resultats = r.json()['items']

        for result in resultats:
            # affiche les details d'une vidéo
            detail_video = {
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={result["id"]}',
                'title' : result['snippet']['title'],
                'stat' : result['statistics']['likeCount'],
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
                'duree' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            }
            videos.append(detail_video)


    template = 'ysearch/index.html'
    context = {'videos': videos}
    return render(request, template, context)
