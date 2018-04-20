# parses articles to get a dict of strings to write to file

from collections import OrderedDict
from time import strptime, asctime
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
        refined_article = OrderedDict()

        refined_article['ArticleTitle'] = find('ArticleTitle',
                                               self.parsed_article)
        refined_article['Reference IDS'] = self.find_ids()
        refined_article['Publication Date'] = self.get_date()
        refined_article['Abstract'] = find('AbstractText',
                                           self.parsed_article)

        return refined_article

    def find_ids(self):
        id_dict = OrderedDict()
        ids = OrderedDict(find('ArticleIdList',
                               self.parsed_article))
        for v in ids.values():
            id_dict[v.attributes["IdType"]] = str(v)
        return id_dict

    def get_date(self):
        date = find('ArticleDate', self.parsed_article).get(0, None)
        print(date)
        if date is None:
            return
        date = asctime(strptime(f"{date['Day']} {date['Month']} {date['Year']}",
                       "%d %m %Y"))
        return date
