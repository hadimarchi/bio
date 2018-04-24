import os


def ensure_query_directory(download_path, query):
    if not os.path.exists(os.path.join(download_path, query)):
        os.mkdir(os.path.join(download_path, query))
