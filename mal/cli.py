#!/usr/bin/env python

import argparse
from mal import Mal, Anime, Manga

ANIME_FORMAT = '{i.title:<50.50} [{i.id:>5}] ' +\
    '({i.my_watched:>3}/{i.episodes:<3})'
MANGA_FORMAT = '{i.title:<50.50} [{i.id:>5}] ' +\
    '({i.my_read_volumes:>3}/{i.volumes:<3}|{i.my_read_chapters:>3}/{i.chapters:<3})'
SCORE_FORMAT = ' <{i.my_score}>'


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

list_parser = subparsers.add_parser('list', help="Show a user's list")
list_parser.add_argument('-a', '--anime', help="Show anime list",
    action='store_true')
list_parser.add_argument('-m', '--manga', help="Show manga list",
    action='store_true')
list_parser.add_argument('-c', '--completed', help="Show completed entries",
    action='store_true')
list_parser.add_argument('user', type=str, help="MAL Username")

update_parser = subparsers.add_parser('update', help='Update an anime or manga')

mal = Mal()


def query_and_format(method, user, filter, format):
    SORTER = lambda item: item.title.lower()
    for item in sorted(method(user, filter=filter).values(), key=SORTER):
        print format.format(i=item)


def main():
    args = parser.parse_args()
    if args.anime:
        filter = Anime.COMPLETED if args.completed else Anime.WATCHING
        print
        print 'Currently Watching'
        print '-' * 80
        query_and_format(mal.anime_list, args.user, filter, ANIME_FORMAT)
    if args.manga:
        filter = Manga.COMPLETED if args.completed else Manga.READING
        print
        print 'Currently Reading'
        print '-' * 80
        query_and_format(mal.manga_list, args.user, filter, MANGA_FORMAT)

if __name__ == '__main__':
    main()
