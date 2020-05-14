from apiclient.discovery import build
from pytube import YouTube

#function to download video
def dl_vid(vid_num, don, dol, i):
	ytd = YouTube(dol[don[vid_num]])
	videos = ytd.streams.filter(progressive=True)
	print('Select Video Quality: ')
	for vid in videos:
		if 'res=' in str(vid) and 'acodec=' in str(vid):
			print(str(i)+') Quality: '+str(vid).split('res="')[1].split('" fps')[0].strip()+', fps: '+str(vid).split('fps="')[1].split('" vcodec')[0].strip()+', vcodec: '+str(vid).split('vcodec="')[1].split('"')[0].strip())
			i = i + 1
	vqn = int(input('Enter Number: '))
	videos[vqn-1].download()
	print('Download Complete!')

#function to get top 10 most viewed videos	
def get_search_results(a, i):
	tl = {}
	nt = {}
	api_key = ''	#Enter your google developer project api key for Youtube Data Api v3
	youtube = build('youtube', 'v3', developerKey=api_key)
	res = youtube.search().list(q=a, part='snippet,id', type='video', order = 'viewCount', maxResults=10).execute()
	for item in res['items']:
		tl[item['snippet']['title']] = 'https://www.youtube.com/watch?v='+item['id']['videoId']
		nt[i] = item['snippet']['title']
		i = i+1
	return(nt, tl)

#Enter string to be searched on youtube, results will be the top 10 most viewed videos for the entered string
search_string = input('Search Videos: ')
l1, l2 = get_search_results(search_string, 1)

print('Select the Video to be downloaded')
for k, v in l1.items():
	print(str(k)+': '+v)
	
vid_num = int(input('Enter number: '))
dl_vid(vid_num, l1, l2, 1)