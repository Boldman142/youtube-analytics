from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.video_title is None  # при предыдущих итерациях этот
    # атрибут у меня назван по другому.
    assert broken_video.like_count is None
