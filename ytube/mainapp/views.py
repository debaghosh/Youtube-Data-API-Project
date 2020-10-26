from django.shortcuts import render, HttpResponse
import requests, isodate
from django.conf import settings

def home(request):
    if(request.method=='POST'):
        if(request.POST['searchOption']=='1'):
            return video(request)
        else: #if(request.POST['searchOption'=='2']):
            return channel(request)
    else:
        return render(request,'mainapp/home.html')


def video(request):
    videos=[]

    if(request.method == 'POST'):
        search_url='https://www.googleapis.com/youtube/v3/search'
        video_url ='https://www.googleapis.com/youtube/v3/videos'

        params = {
            'part':'snippet',
            'q': request.POST['search'],
            'maxResults':15,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'type':'video'
        }

        r = requests.get(search_url,params=params)

        results = r.json()['items']

        for result in results:
            videos.append(result['id']['videoId'])

        params2={
            'part':'snippet, contentDetails, statistics',
            'key': settings.YOUTUBE_DATA_API_KEY,
            'id': ','.join(videos)
        }

        r = requests.get(video_url,params=params2)

        results = r.json()['items']
        videos = []
        statistics = []
        for result in results:
            video_data = {
                'title':result['snippet']['title'],
                'id': result['id'],
                'duration': isodate.parse_duration(result['contentDetails']['duration']),
                'thumbnail':result['snippet']['thumbnails']['high']['url'],
                'likes':result['statistics']['likeCount'],
                'dislikes':result['statistics']['dislikeCount'],
                'views':result['statistics']['viewCount']

                }
            videos.append(video_data)

    
    context = {
        'videos': videos
    }
    
    return render(request, 'mainapp/video.html',context)

def channel(request):
    
    channel_data={}
      
    if(request.method=='POST'):
        search_url='https://www.googleapis.com/youtube/v3/search'
        channel_url='https://www.googleapis.com/youtube/v3/channels'

        #Search for the channel id
        param = {
            'part':'snippet',
            'q': request.POST['search'],
            'type':'channel',
            'maxResults':1,
            'key': settings.YOUTUBE_DATA_API_KEY

        }
        result = requests.get(search_url,params=param)
        channel_id = result.json()['items'][0]['id']['channelId']

        #Search for the channel basic details
        param2 = {
            'part':'contentDetails,contentOwnerDetails,snippet,id,statistics,status,topicDetails',
            'id':channel_id,
            'key': settings.YOUTUBE_DATA_API_KEY

        }
        result = requests.get(channel_url,params=param2).json()['items'][0]
        channel_data={
            'title': result['snippet']['title'],
            'description': result['snippet']['description'],
            'published':result['snippet']['publishedAt'],
            'thumbnail': result['snippet']['thumbnails']['default']['url'],
            'country':result['snippet']['country'],
            'viewcount':result['statistics']['viewCount'],
            'subscount':result['statistics']['subscriberCount'],
            'videocount':result['statistics']['videoCount'],
            'id':channel_id
        }

        #get all the videos of that channel,using the pageNexttoken
        param3 = {
            'key': settings.YOUTUBE_DATA_API_KEY,
            'channelId':channel_id,
            'maxResults':50,
            'order':'date',
            'type':'video',
            'part':'id'
        }
        result = requests.get(search_url,params=param3)
        npt = result.json()['nextPageToken']
        tr = result.json()['pageInfo']['totalResults']
        rpp = result.json()['pageInfo']['resultsPerPage']
        #print(result.text)
        #resultlist = result.json()[]
        """
        videos=[]
        npt = ''
        c=0
        print('tr = '+str(tr))
        while(tr!=0):
            for i in range (0,rpp):
                    print('i= '+str(i))
                    try:
                        npt = result.json()['nextPageToken']
                    except:
                        pass
                    videos.append(result.json()['items'][i]['id']['videoId']) 
                    tr=tr-1
                    c=c+1
                    print('c= '+str(c))
            if tr!=0:
                param3['pageToken']=npt
                result = requests.get(search_url,params=param3)
                if tr<rpp:
                    rpp=tr
                
                
        #print(videos)
        #print(npt)
        #print(c)    
        """
    context={
        'channel_data':channel_data
    }


    return render(request,'mainapp/channel.html',context)





