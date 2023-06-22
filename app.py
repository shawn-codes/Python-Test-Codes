# Comment in Python

import random

song_requests = []

song_request = None

while True:
    song_request = input('Enter a song title: ')
    if song_request == 'Quit':
        break
    song_requests.append(song_request)

if (len(song_requests) > 0):
    print(random.choice(song_requests))
else:
    print('No songs were entered')
