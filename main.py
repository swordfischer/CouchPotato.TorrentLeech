from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import simplifyString, tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback
import cookielib
import urllib2
import time
import six

log = CPLog(__name__)

class TorrentLeech(TorrentProvider, MovieProvider):

    urls = {
        'test': 'https://www.torrentleech.org/',
        'login': 'https://www.torrentleech.org/user/account/login/',
        'login_check': 'https://torrentleech.org/user/messages',
        'detail': 'https://www.torrentleech.org/torrent/%s',
        'search': 'https://www.torrentleech.org/torrents/browse/index/query/%s/categories/%d',
        'download': 'https://www.torrentleech.org%s',
    }

    cat_ids = [
        ([13], ['720p', '1080p', 'bd50']),
        ([8], ['cam']),
        ([9], ['ts', 'tc']),
        ([10], ['r5', 'scr']),
        ([11], ['dvdrip']),
        ([14], ['brrip']),
        ([12], ['dvdr']),
    ]

    https_time_between_calls = 1  # Seconds
    cat_backup_id = None

    def buildUrl(self, title, media, quality):
        return (
            tryUrlencode(title.replace(':', '')),
            self.getCatId(quality)[0]
       ) 

    def _searchOnTitle(self, title, media, quality, results):

        url = self.urls['search'] % self.buildUrl(title, media, quality)

        data = self.getHTMLData(url)

        if data:
            html = BeautifulSoup(data)

            try:
                result_table = html.find('table', attrs = {'id': 'torrenttable'})
                if not result_table:
                    return

                entries = result_table.find_all('tr')

                for result in entries[1:]:

                    link = result.find('td', attrs = {'class': 'name'}).find('a')
                    url = result.find('td', attrs = {'class': 'quickdownload'}).find('a')
                    details = result.find('td', attrs = {'class': 'name'}).find('a')

                    results.append({
                        'id': link['href'].replace('/torrent/', ''),
                        'name': six.text_type(link.string),
                        'url': self.urls['download'] % url['href'],
                        'detail_url': self.urls['download'] % details['href'],
                        'size': self.parseSize(result.find_all('td')[4].string),
                        'seeders': tryInt(result.find('td', attrs = {'class': 'seeders'}).string),
                        'leechers': tryInt(result.find('td', attrs = {'class': 'leechers'}).string),
                    })

            except:
                log.error('Failed to parsing %s: %s', (self.getName(), traceback.format_exc()))

    def getLoginParams(self):
        return {
            'username': self.conf('username'),
            'password': self.conf('password'),
            'remember_me': 'on',
            'login': 'submit',
        }

    def loginSuccess(self, output):
        return '/user/account/logout' in output.lower() or 'welcome back' in output.lower()

    loginCheckSuccess = loginSuccess


