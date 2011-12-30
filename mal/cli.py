#!/usr/bin/env python

from sys import argv
from mal import Mal

ANIME_FORMAT = '{:<50} [{:>5}] ({:>3}/{:<3})'
MANGA_FORMAT = '{:<50} [{:>5}] ({:>3}/{:<3}|{:>3}/{:<3})'

mal = Mal()


def main():
    print 'Currently Watching'
    print '-' * 80
    for anime in mal.anime_list(argv[1]).values():
        if anime.my_status is anime.WATCHING:
            print ANIME_FORMAT.format(
                anime.title,
                anime.id,
                anime.my_watched,
                anime.episodes,
            )
    print
    print 'Currently Reading'
    print '-' * 80
    for manga in mal.manga_list(argv[1]).values():
        if manga.my_status is manga.READING:
            print MANGA_FORMAT.format(
                manga.title,
                manga.id,
                manga.my_read_volumes,
                manga.volumes,
                manga.my_read_chapters,
                manga.chapters,
            )

if __name__ == '__main__':
    main()
