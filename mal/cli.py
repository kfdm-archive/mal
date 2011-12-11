#!/usr/bin/env python

from sys import argv
from mal import Mal

DISPLAY_FORMAT = '{:<50} ({:>2}/{:<2}) [{}]'

mal = Mal()

def main():
    print 'Currently Watching'
    print '-' * 80
    for anime in mal.anime_list(argv[1]).values():
        if anime.my_status is anime.WATCHING:
            print DISPLAY_FORMAT.format(
                anime.title,
                anime.my_watched,
                anime.episodes,
                anime.id
            )

    print 'Currently Reading'
    print '-' * 80
    for manga in mal.manga_list(argv[1]).values():
        if manga.my_status is manga.READING:
            print DISPLAY_FORMAT.format(
                manga.title,
                manga.my_read_chapters,
                manga.chapters,
                manga.id
            )

if __name__ == '__main__':
    main()
