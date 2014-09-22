import plistlib
import requests
import datetime
from urllib import urlencode

tracks = plistlib.readPlist('/Users/aashford/Desktop/Library.xml')['Tracks']
songs = [tracks[i] for i in tracks if tracks[i].get('Genre', None) not in ('Podcast', None)]

play_counts = {}
ages = {}
song_ranks = {}

for song in songs:
	if 'Artist' in song:
		if song['Artist'] not in play_counts:
			play_counts[song['Artist']] = song.get('Play Count', 0)
		else:
			play_counts[song['Artist']] += song.get('Play Count', 0)

for song in songs:
	if 'Artist' in song:

		age_of_song = (datetime.datetime.now() - song['Date Added']).total_seconds()
		
		if song['Artist'] not in ages:
			ages[song['Artist']] = age_of_song
		else:
			ages[song['Artist']] = max(ages[song['Artist']], age_of_song)

for k, v in play_counts.iteritems():
	song_ranks[k] = ages[k] / max(v, 1)


counts_as_list = [{'name': key, 'play_count': value} for key, value in play_counts.iteritems()]

ranks_as_list = [{'name': key, 'rank': value} for key, value in song_ranks.iteritems()]


sorted_count_list = sorted(counts_as_list, key = lambda k: k['play_count'], reverse = True)

sorted_rank_list = sorted(ranks_as_list, key = lambda k: k['rank'])



# for i in sorted_count_list[:100]:
# 	print i['name']

# for i in sorted_rank_list[:100]:
# 	print i['name']











