import os
from .utils import write_dict


class ArticleWriter:
    def __init__(self, articles_path):
        self.articles_path = articles_path

    def write_article(self, article, query):
        try:
            with open("{}.md".format(
                    os.path.join(self.articles_path,
                                 query,
                                 (article['ArticleTitle'].replace("/", "_")))),
                      "w") as md_article:

                md_article.write("#### {}:\n**{}**\n".format('Article Title',
                                                             article['ArticleTitle'].strip("[].")))
                del article['ArticleTitle']
                for k, v in article.items():
                    if isinstance(v, dict):
                        md_str = "#### {}:\n{}\n".format(k, write_dict(v))
                    else:
                        md_str = "#### {}:\n{}\n".format(k, v)
                    md_article.write(md_str)
        except Exception as e:
            print(str(e))
            pass
