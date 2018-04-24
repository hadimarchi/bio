from .handlemanager import efetchmanager
from .options import Options
from .utils import ensure_query_directory
from Bio import Entrez
import os
import lxml.etree as ET


class Downloader:
    def __init__(self):
        self.options = Options()
        Entrez.email = self.options.email

    def download_all(self):
        for query in self.options.queries:
            ensure_query_directory(self.options.download_path, query)
            for id in self.options.ids[query]:
                print(id)
                with efetchmanager(db=self.options.database, id=id) as handle:
                    article = ET.parse(handle)
                    self.write_article(query, id, article)

    def write_article(self, query, id, article):
        with open(os.path.join(
                                self.options.download_path,
                                query,
                                f"{id}.xml"), "w") as full_article:
            full_article.write(ET.tostring(article,
                                           encoding='unicode',
                                           pretty_print=True))
