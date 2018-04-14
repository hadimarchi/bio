# parses articles to get a dict of strings to write to file

import textwrap
import json

from .utils import parse_list, parse_dict, find_dict_element_from_key as find


class ArticleParser:
    def __init__(self):
        self.parsed_article = {}
        pass

    def parse_article(self, article):
        for k, v in article.items():
            if isinstance(v, dict):
                self.parsed_article[k] = parse_dict(v)
            elif isinstance(v, list):
                self.parsed_article[k] = parse_list(v)
            else:
                self.parsed_article[k] = v
        return self.refine_article()

    def refine_article(self):
        refined_article = {}
        abstract = find('AbstractText', self.parsed_article)
        refined_article['AbstractText'] = abstract if abstract is not None else "NO ABSTRACT"
        refined_article['ArticleTitle'] = find('ArticleTitle',
                                               self.parsed_article)
        return refined_article
