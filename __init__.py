from couchpotato.core.logger import CPLog
from .main import TorrentLeech

lob = CPLog(__name__)

def autoload():
	return TorrentLeech()

config = [{
    'name': 'torrentleech',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'TorrentLeech',
            'description': '<a href="https://torrentleech.org">TorrentLeech</a>',
            'wizard': True,
            'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACHUlEQVR4AZVSO48SYRSdGTCBEMKzILLAWiybkKAGMZRUUJEoDZX7B9zsbuQPYEEjNLTQkYgJDwsoSaxspEBsCITXjjNAIKi8AkzceXgmbHQ1NJ5iMufmO9/9zrmXlCSJ+B8o75J8Pp/NZj0eTzweBy0Wi4PBYD6f12o1r9ebTCZx+22HcrnMsuxms7m6urTZ7LPZDMVYLBZ8ZV3yo8aq9Pq0wzCMTqe77dDv9y8uLyAWBH6xWOyL0K/56fcb+rrPgPZ6PZfLRe1fsl6vCUmGKIqoqNXqdDr9Dbjps9znUV0uTqdTjuPkDoVCIfcuJ4gizjMMm8u9vW+1nr04czqdK56c37CbKY9j2+1WEARZ0Gq1RFHAz2q1qlQqXxoN69HRcDjUarW8ZD6QUigUOnY8uKYH8N1sNkul9yiGw+F6vS4Rxn8EsodEIqHRaOSnq9T7ajQazWQycEIR1AEBYDabSZJyHDucJyegwWBQr9ebTCaKvHd4cCQANUU9evwQ1Ofz4YvUKUI43GE8HouSiFiNRhOowWBIpVLyHITJkuW3PwgAEf3pgIwxF5r+OplMEsk3CPT5szCMnY7EwUdhwUh/CXiej0Qi3idPz89fdrpdbsfBzH7S3Q9K5pP4c0sAKpVKoVAQGO1ut+t0OoFAQHkH2Da/3/+but3uarWK0ZMQoNdyucRutdttmqZxMTzY7XaYxsrgtUjEZrNhkSwWyy/0NCatZumrNQAAAABJRU5ErkJggg==',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]

