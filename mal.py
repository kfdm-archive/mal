#!/usr/bin/env python

from sys import argv
from mal import Mal

print 'Currently Watching'
print '-'*80
for anime in Mal().anime_list(argv[1]).values():
    if anime.my_status is anime.WATCHING:
        print '{:<40} ({:>2}/{:<2}) [{}]'.format(
            anime.title,
            anime.my_watched,
            anime.episodes,
            anime.id
        )

