from . import config
from googleapiclient.discovery import build

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query_term, max_result_number=3):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_resource = youtube.search()
    list_request = search_resource.list(
        q=query_term,
        part='snippet',
        maxResults=max_result_number
    )
    search_response = list_request.execute()

    results = []
    for item in search_response["items"]:
        results.append({
            "id" : item["id"],
            "title" : item["snippet"]["title"]
        })
    return results