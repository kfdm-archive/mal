#!/usr/bin/env python

from sys import argv
from mal import Mal, Anime, Manga

ANIME_FORMAT = '{i.title:<50.50} [{i.id:>5}] ' +\
    '({i.my_watched:>3}/{i.episodes:<3})'
MANGA_FORMAT = '{i.title:<50.50} [{i.id:>5}] ' +\
    '({i.my_read_volumes:>3}/{i.volumes:<3}|{i.my_read_chapters:>3}/{i.chapters:<3})'
SCORE_FORMAT = ' <{i.my_score}>'


mal = Mal()


def query_and_format(method, filter, format):
    SORTER = lambda item: item.title.lower()
    for item in sorted(method(argv[1], filter=filter).values(), key=SORTER):
        print format.format(i=item)


def main():
    print 'Currently Watching'
    print '-' * 80
    query_and_format(mal.anime_list, Anime.WATCHING, ANIME_FORMAT)
    print
    print 'Currently Reading'
    print '-' * 80
    query_and_format(mal.manga_list, Manga.READING, MANGA_FORMAT)


def completed():
    print 'Completed Anime'
    print '-' * 80
    query_and_format(mal.anime_list, Anime.COMPLETED, ANIME_FORMAT + SCORE_FORMAT)
    print
    print 'Completed Manga'
    print '-' * 80
    query_and_format(mal.manga_list, Manga.COMPLETED, MANGA_FORMAT + SCORE_FORMAT)

if __name__ == '__main__':
    main()
