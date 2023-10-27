from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб - канала"""

    api_key: str = os.getenv('API_KEY_YT')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
    Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.info = self.youtube.channels().list(
            part="snippet, contentDetails, statistics",
            id=self.channel_id).execute()
        self.id = self.info["items"][0]["id"]
        self.title = self.info["items"][0]["snippet"]["title"]
        self.overview = self.info["items"][0]["snippet"]["description"]
        self.url = ('https://www.youtube.com/channel/' +
                    self.info['items'][0]['id'])
        self.count_subscribe = int((
                    self.info)["items"][0]["statistics"]["subscriberCount"])
        self.video_count = self.info["items"][0]["statistics"]["videoCount"]
        self.video_count = self.info["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.count_subscribe + other.count_subscribe

    def __sub__(self, other):
        return self.count_subscribe - other.count_subscribe

    def __lt__(self, other):
        return self.count_subscribe < other.count_subscribe

    def __le__(self, other):
        return self.count_subscribe <= other.count_subscribe

    def __gt__(self, other):
        return self.count_subscribe > other.count_subscribe

    def __ge__(self, other):
        return self.count_subscribe >= other.count_subscribe

    def __eq__(self, other):
        return self.count_subscribe == other.count_subscribe

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube.channels().
                         list(part="snippet, contentDetails, statistics",
                              id=self.channel_id).execute(), indent=2,
                         ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    def to_json(self, path):
        with open(path, "w") as file:
            json.dump(self.info, file)

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, data):
        print("AttributeError: property 'channel_id' "
              "of 'Channel' object has no setter")
