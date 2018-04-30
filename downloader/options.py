import json
import os
from configparser import SafeConfigParser


class Options:
    def __init__(self):
        self.config = SafeConfigParser()
        self.config_file = os.path.join(os.getcwd(), "downloader/downloader.cfg")
        self.config.read(self.config_file)
        self.ids = {}
        self.get_options()
        self.get_queries()
        self.get_ids()

    def get_options(self):
        self.email = self.config.get("general", "email")
        self.database = self.config.get("downloading", "db")
        self.articles_path = self.config.get("downloading", "articles_path")
        self.download_path = self.config.get("downloading", "download_path")

    def get_queries(self):
        self.queries = os.listdir(self.articles_path)

    def get_ids(self):
        for query in self.queries:
            with open(os.path.join(self.articles_path,
                                   query,
                                   "{}_{}ids.json".format(
                                    query, self.database)), "r") as id_file:
                self.ids[query] = json.load(id_file)
