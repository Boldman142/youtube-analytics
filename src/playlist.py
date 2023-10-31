import os
import datetime
import isodate
from googleapiclient.discovery import build


class PlayList:
    api_key: str = os.getenv('API_KEY_YT')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, pl_id):
        self.__playlist_videos = self.youtube.playlistItems().list(
            playlistId=pl_id,
            part='contentDetails',
            maxResults=50, ).execute()
        # self.laylist_videos = self.youtube.playlistItems().list(
        # playlistId=pl_id,
        # part='contentDetails',
        # maxResults=50,
        # ).execute()
        self.title = self.youtube.playlistItems().list(
            playlistId=pl_id,
            part='snippet', maxResults=50, ).execute()
        self.url = "https://www.youtube.com/playlist?list=" + pl_id
        self.__video_ids = [video['contentDetails']['videoId']
                            for video in self.__playlist_videos['items']]
        self.__video_response = self.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(self.__video_ids)
        ).execute()

    @property
    def total_duration(self):
        total = datetime.timedelta(seconds=0, minutes=0, hours=0)
        for video in self.__video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total += duration
        return total

    # @property
    # def video_response(self):
    #     return self.__video_response
    #
    # @property
    # def video_ids(self):
    #     return self.__video_ids

    def show_best_video(self):
        id_best_video = ""
        like_best_video = 0
        for vid_id in self.__video_ids:
            video_info = self.youtube.videos().list(
                part='snippet,statistics,contentDetails,topicDetails',
                id=vid_id).execute()
            like_count = int(video_info['items'][0]['statistics']['likeCount'])
            if like_count > like_best_video:
                like_best_video = like_best_video
                id_best_video = vid_id
        return f"https://youtu.be/{id_best_video}"

    @classmethod
    def total_seconds(cls):
        return cls.total_duration.timestamp()

# a = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
#
# print(a.url)
# print(a.laylist_videos)
# print(a.total_duration)
# print(a.title)
# print(a.total_duration.total_seconds())
# print(a.show_best_video())
# # for video_id in a.video_ids:#['items'][0]['statistics']['likeCount']:
#
#     print(video_id)
