from catalog import LESSONS
def visible_titles(query):
    return [x["title"] for x in LESSONS if x["published"] and query.lower() in x["title"].lower()]
