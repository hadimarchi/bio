from configparser import SafeConfigParser
import os


class Options:
    def __init__(self):
        self.config = SafeConfigParser()
        self.config_path = os.path.join(os.getcwd(), "pubmed/searcher.cfg")
        self.config.read(self.config_path)
        self.get_options()

    def get_options(self):
        self.max_hits = int(self.config.get('searching', 'max_hits'))
        self.search_method = self.config.get('searching', 'method')
        self.database = self.config.get('searching', 'db')
        self.email = self.config.get('general', 'email')
        self.articles_path = self.config.get('paths', 'articles_path')
