#!/usr/bin/env python

from sys import argv
from mal import Mal

ANIME_FORMAT = '{a.title:<50.50} [{a.id:>5}] ' +\
    '({a.my_watched:>3}/{a.episodes:<3})'
MANGA_FORMAT = '{m.title:<50.50} [{m.id:>5}] ' +\
    '({m.my_read_volumes:>3}/{m.volumes:<3}|{m.my_read_chapters:>3}/{m.chapters:<3})'

mal = Mal()

SORTER = lambda item: item.title.lower()


def main():
    print 'Currently Watching'
    print '-' * 80
    for anime in sorted(mal.anime_list(argv[1]).values(), key=SORTER):
        if anime.my_status is anime.WATCHING:
            print ANIME_FORMAT.format(a=anime)
    print
    print 'Currently Reading'
    print '-' * 80
    for manga in sorted(mal.manga_list(argv[1]).values(), key=SORTER):
        if manga.my_status is manga.READING:
            print MANGA_FORMAT.format(m=manga)


def completed():
    AFORMAT = ANIME_FORMAT + ' <{a.my_score}>'
    MFORMAT = MANGA_FORMAT + ' <{m.my_score}>'
    print 'Completed Anime'
    print '-' * 80
    for anime in sorted(mal.anime_list(argv[1]).values(), key=SORTER):
        if anime.my_status is anime.COMPLETED:
            print AFORMAT.format(a=anime)
    print
    print 'Completed Manga'
    print '-' * 80
    for manga in sorted(mal.manga_list(argv[1]).values(), key=SORTER):
        if manga.my_status is manga.COMPLETED:
            print MFORMAT.format(m=manga)

if __name__ == '__main__':
    main()
