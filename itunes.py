import plistlib
import requests
from urllib import urlencode

print urlencode(payload)

tracks = plistlib.readPlist('/Users/aashford/Desktop/Library.xml')['Tracks']
songs = [tracks[i] for i in tracks if tracks[i].get('Genre', None) not in ('Podcast', None)]

play_counts = {}

for song in songs:
	if 'Artist' in song:
		if song['Artist'] not in play_counts:
			play_counts[song['Artist']] = song.get('Play Count', 0)
		else:
			play_counts[song['Artist']] += song.get('Play Count', 0)

new_list = [{'name': key, 'play_count': value} for key, value in play_counts.iteritems()]

sorted_list = sorted(new_list, key = lambda k: k['play_count'], reverse = True)

for i in sorted_list[:100]:
	print i['name']















