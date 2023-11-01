from googleapiclient.discovery import build
import os


class Video:
    api_key: str = os.getenv('API_KEY_YT')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video: str):  # , channel_id: str):
        #      super().__init__(channel_id)
        try:
            self.info = self.youtube.videos().list(
                part='snippet,statistics,contentDetails,topicDetails',
                id=id_video).execute()["items"][0]["kind"]
        except IndexError:
            self.info = None
            self.url = None
            self.video_title = None
            self.view_count = None
            self.like_count = None
        else:
            self.info = self.youtube.videos().list(
                part='snippet,statistics,contentDetails,topicDetails',
                id=id_video).execute()
            self.url = ('https://www.youtube.com/channel/' +
                        self.info['items'][0]['id'])
            self.video_title: str = self.info['items'][0]['snippet']['title']
            self.view_count: int = self.info['items'][0]['statistics']['viewCount']
            self.like_count: int = self.info['items'][0]['statistics']['likeCount']
        finally:
            self.video_id = id_video

    def __str__(self):
        return self.video_title


class PLVideo(Video):

    def __init__(self, id_video, pl_video):
        super().__init__(id_video)
        self.video_pl = pl_video
