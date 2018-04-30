def parse_list(article_list):
    list_dict = {}
    for entry in range(0, len(article_list)):
        list_dict[entry] = parse_object(article_list, entry)
    return list_dict


def parse_dict(article_dict):
    list_dict = {}
    for k in article_dict.keys():
        list_dict[k] = parse_object(article_dict, k)
    return list_dict


def parse_object(article_object, entry):
    if isinstance(article_object[entry], list):
        return parse_list(article_object[entry])
    elif isinstance(article_object[entry], dict):
        return parse_dict(article_object[entry])
    else:
        return article_object[entry]


def write_without_key(value):
    if isinstance(value, dict):
        return "\n{}".format(write_dict(value))
    return "\n{}\n".format(value)


def write_with_key(key, value):
    if isinstance(value, dict):
        return "\n{}: {}".format(key, write_dict(value))
    return "\n{}: {}\n".format(key, value)


def write_dict(dictionary):
    dict_str = ""
    for k, v in dictionary.items():
        dict_str = dict_str + (
            write_without_key(v) if isinstance(k, int) else write_with_key(k, v)
            )

    return dict_str


def find_dict_element_from_key(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            element = find_dict_element_from_key(key, v)
            if element is not None:
                return element
