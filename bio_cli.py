"""bio_arguments

Usage:
    bio_cli.py <command> [<args>...]

Options:
    - h --help          Show this screen

Subcommands:
    query <query_str>   Query pubmed
    download_all        Download all available full text articles from PMC

"""

from docopt import docopt
from downloader.downloader import Downloader
from pubmed.search import EntrezDbSearcher


class BioCli:
    def __init__(self):
        self.searcher = EntrezDbSearcher()
        self.downloader = Downloader()
        self.bio_arguments = docopt(__doc__)

    def search(self):
        """
            Usage:
            bio_cli.py search <query>
        """
        search_arguments = docopt(self.search.__doc__)
        self.searcher.search(search_arguments['<query>'])

    def download_all(self):
        self.downloader.download_all()

    def download_by_query(self):
        """
            Usage:
            bio_cli.py download_by_query <query>
        """
        downloader_arguments = docopt(self.download_by_query.__doc__)
        self.downloader.download_by_query(downloader_arguments['<query>'])

    def execute(self):
        function = getattr(self, self.bio_arguments.pop('<command>'))
        function()


if __name__ == "__main__":
    bio_arguments = docopt(__doc__)
    bio_cli = BioCli()
    bio_cli.execute()
