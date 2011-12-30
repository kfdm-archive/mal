import requests
from xml.dom.minidom import parseString


class Mal(object):
    def anime_list(self, user):
        r = requests.get('http://myanimelist.net/malappinfo.php?u=%s&type=anime&status=all' % user)
        dom = parseString(r.content.encode('utf8'))
        self.anime = {}
        for anime in dom.getElementsByTagName('anime'):
            anime = Anime(anime)
            self.anime[anime.id] = anime
        return self.anime

    def manga_list(self, user):
        r = requests.get('http://myanimelist.net/malappinfo.php?u=%s&type=manga&status=all' % user)
        dom = parseString(r.content.encode('utf8'))
        self.manga = {}
        for manga in dom.getElementsByTagName('manga'):
            manga = Manga(manga)
            self.manga[manga.id] = manga
        return self.manga


class Media(object):
    def _getText(self, tag):
        rc = []
        for node in self.node.getElementsByTagName(tag)[0].childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        text = ''.join(rc)
        return text.encode('utf8')

    def _getInt(self, tag):
        try:
            return int(self._getText(tag))
        except:
            return 0

    def __repr__(self):
        return "%s:%s" % (self.id, self.title)


class Anime(Media):
    WATCHING = 1
    COMPLETED = 2
    ONHOLD = 3
    DROPPED = 4
    PLANTOWATCH = 6

    def __init__(self, node):
        self.node = node
        self.id = self._getInt('series_animedb_id')
        self.title = self._getText('series_title')
        self.synonyms = self._getText('series_synonyms')
        self.type = self._getText('series_type')
        self.episodes = self._getInt('series_episodes')
        self.status = self._getInt('series_status')
        self.start = self._getText('series_start')
        self.end = self._getText('series_end')
        self.image = self._getText('series_image')

        self.my_id = self._getInt('my_id')
        self.my_watched = self._getText('my_watched_episodes')
        self.my_start_date = self._getText('my_start_date')
        self.my_finish_date = self._getText('my_finish_date')
        self.my_score = self._getText('my_score')
        self.my_status = self._getInt('my_status')
        self.my_rewatching = self._getText('my_rewatching')
        self.my_rewatching_ep = self._getText('my_rewatching_ep')
        self.my_last_updated = self._getText('my_last_updated')
        self.my_tags = self.my_id = self._getText('my_tags')


class Manga(Media):
    READING = 1
    COMPLETED = 2
    ONHOLD = 3
    DROPPED = 4
    PLANTOREAD = 6

    def __init__(self, node):
        self.node = node
        self.id = self._getInt('series_mangadb_id')
        self.title = self._getText('series_title')
        self.synonyms = self._getText('series_synonyms')
        self.type = self._getText('series_type')
        self.chapters = self._getInt('series_chapters')
        self.volumes = self._getText('series_volumes')
        self.status = self._getText('series_status')
        self.start = self._getText('series_start')
        self.end = self._getText('series_end')
        self.image = self._getText('series_image')

        self.my_id = self._getText('my_id')
        self.my_read_chapters = self._getInt('my_read_chapters')
        self.my_read_volumes = self._getInt('my_read_volumes')
        self.my_start_date = self._getText('my_start_date')
        self.my_finish_date = self._getText('my_finish_date')
        self.my_score = self._getText('my_score')
        self.my_status = self._getInt('my_status')
        #self.my_rereading = self._getText('my_rereadingg')
        self.my_reareading_chapter = self._getInt('my_reareading_chapt')
        self.my_last_updated = self._getInt('my_last_updated')
        self.my_tags = self.my_id = self._getText('my_tags')
