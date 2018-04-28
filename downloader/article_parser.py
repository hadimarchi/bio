
from .utils import epub_date
from bs4 import BeautifulSoup
from collections import OrderedDict


class ArticleParser:
    def __init__(self):
        pass

    def parse_article(self, article):
        self.article_dict = OrderedDict()
        self.soup = BeautifulSoup(article, "xml")

        self.get_ids()
        self.get_publication_date()
        self.get_article()

        return self.article_dict

    def get_ids(self):
        self.article_dict["IDS"] = {}
        ids = self.soup.find_all('article-id')
        for id in ids:
            self.article_dict["IDS"][id['pub-id-type']] = id.string

    def get_publication_date(self):
        try:
            self.article_dict["Publication Date"] = self.get_date()
        except Exception as e:
            print(str(e))
            self.article_dict["Publication Date"] = "Not Found"

    def get_date(self):
        date = self.soup.find(epub_date)
        date_dict = OrderedDict([("day", 0), ("month", 0), ("year", 0)])
        for date_info in date.children:
            date_dict[date_info.name] = date_info.string
        return date_dict

    def get_article(self):
        self.article_dict["Abstract"] = self.get_abstract()
        self.article_dict["Introduction"] = self.get_title_section("Introduction")
        try:
            self.article_dict["Methods"] = self.get_title_section("Materials and Methods")
        except Exception:
            self.article_dict["Methods"] = self.get_title_section("Methods")

        self.article_dict["Discussion"] = self.get_title_section("Discussion")

    def get_abstract(self):
        abstract = self.soup.find('abstract').find_all('p')
        abstract_str = self.get_paragraphs(abstract)
        return abstract_str

    def get_title_section(self, title_name):
        section = self.soup.find('title', string=title_name)
        if section is not None:
            siblings = list(section.next_siblings)
            section_str = self.get_paragraphs(siblings)

            return section_str
        return None

    def get_paragraphs(self, tags):
        paragraphs_str = ""
        for tag in tags:
            if tag.name == 'p':
                paragraphs_str = " ".join(
                    [paragraphs_str, self.get_paragraph(tag)])
            if tag.name == 'title':
                paragraphs_str = f"\n{tag.string}".join(
                    [paragraphs_str, self.get_paragraphs(tag)]
                )
        return paragraphs_str

    def get_paragraph(self, paragraph):
        paragraph_str = ""
        for line in paragraph.find_all(text=True):
            paragraph_str = " ".join([paragraph_str, line])

        return paragraph_str
