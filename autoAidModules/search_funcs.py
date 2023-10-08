from serpapi import GoogleSearch
from .sample_res import res
from boilerpy3 import extractors
from fake_useragent import UserAgent

import requests

extractor = extractors.ArticleExtractor()

preferred_forums = {
    "BMW": ["bimmerforums.com"]
}

ua = UserAgent()

"""
Website data: 
[

{
    "title":"",
    "link": "",
    "date": "", # prioritise older posts for older cars?,
    "full-text": "",
},

]
"""

def find_preferred_forums(make):
    if make not in preferred_forums:
        return None
    return preferred_forums[make]

def get_preferred_forums(make):
    if make not in preferred_forums:
        return find_preferred_forums(make)
    return preferred_forums[make]

def parse_page(url):
    content = extractor.get_content_from_url(url)
    return content


def search_on_forum(forum, query, max_results: int = 5):
    params = {
        "q": query + f" {forum}",
        "location": "Austin, Texas, United States",
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key": "KEY"
    }
    #search = GoogleSearch(params)
    #results = search.get_dict()

    results = res
    if results["search_metadata"]['status'] == "Success":
        data = []
        for idx, result in enumerate(results["organic_results"]):
            if idx >= max_results:
                break
            new_dict = {
                "title": result["title"],
                "link": result["link"],
                "full-text": ""
            }
            try:
                resp = requests.get(result["link"], headers={"User-Agent": ua.random})
                new_dict["full-text"] = extractor.get_content(resp.text)
            except Exception as e:
                print(f"Error parsing page {result['link']}: {e}")
            data.append(new_dict)
        return data
    else:
        return []