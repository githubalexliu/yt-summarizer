from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'zh-Hant', 'zh-TW', 'zh-CN'])
    return ' '.join([entry['text'] for entry in transcript])
