from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY_YT')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube.channels().
                         list(part="snippet, contentDetails, statistics",
                              id=self.channel_id).execute(), indent=2,
                         ensure_ascii=False))
