import requests
from xml.dom.minidom import parse, parseString

def _getText(node, tag):
    rc = []
    for node in node.getElementsByTagName(tag)[0].childNodes:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    text = ''.join(rc)
    return text.encode('utf8')

def _getInt(node, tag):
    try:
        return int(_getText(node, tag))
    except:
        return 0

class Mal(object):
    def anime_list(self, user):
        r = requests.get('http://myanimelist.net/malappinfo.php?u=%s'%user)
        dom = parseString(r.content.encode('utf8'))
        self.anime = {}
        for anime in dom.getElementsByTagName('anime'):
            anime = Anime(anime)
            self.anime[anime.id] = anime
        return self.anime


class Anime(object):
    WATCHING = 1
    COMPLETED = 2
    ONHOLD = 3
    DROPPED = 4
    PLANTOWATCH = 6
    def __init__(self,node):
        self.node = node
        self.id = _getInt(self.node,'series_animedb_id')
        self.title = _getText(self.node,'series_title')
        self.type = _getText(self.node, 'series_type')
        self.episodes = _getInt(self.node, 'series_episodes')
        self.status = _getInt(self.node, 'series_status')
        self.start = _getText(self.node, 'series_start')
        self.end = _getText(self.node, 'series_end')
        self.image = _getText(self.node, 'series_image')

        self.my_id = _getInt(self.node, 'my_id')
        self.my_watched = _getText(self.node, 'my_watched_episodes')
        self.my_start_date = _getText(self.node, 'my_start_date')
        self.my_finish_date = _getText(self.node, 'my_finish_date')
        self.my_score = _getText(self.node, 'my_score')
        self.my_status = _getInt(self.node, 'my_status')
        self.my_rewatching = _getText(self.node, 'my_rewatching')
        self.my_rewatching_ep = _getText(self.node, 'my_rewatching_ep')
        self.my_last_updated = _getText(self.node, 'my_last_updated')
        self.my_tags = self.my_id = _getText(self.node, 'my_tags')

    def __repr__(self):
        return "%s:%s"%(self.id, self.title)
