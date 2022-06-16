import enum

from ..utils.enum import AutoName


class ChatAction(str, AutoName):
    """
    This object represents bot actions.

    Choose one, depending on what the user is about to receive:
        • typing for text messages,
        • upload_photo for photos,
        • record_video or upload_video for videos,
        • record_voice or upload_voice for voice notes,
        • upload_document for general files,
        • choose_sticker for stickers,
        • find_location for location data,
        • record_video_note or upload_video_note for video notes.

    Source: https://core.telegram.org/bots/api#sendchataction
    """

    TYPING: str = enum.auto()
    UPLOAD_PHOTO: str = enum.auto()
    RECORD_VIDEO: str = enum.auto()
    UPLOAD_VIDEO: str = enum.auto()
    RECORD_AUDIO: str = enum.auto()
    UPLOAD_AUDIO: str = enum.auto()
    RECORD_VOICE: str = enum.auto()
    UPLOAD_VOICE: str = enum.auto()
    UPLOAD_DOCUMENT: str = enum.auto()
    FIND_LOCATION: str = enum.auto()
    RECORD_VIDEO_NOTE: str = enum.auto()
    UPLOAD_VIDEO_NOTE: str = enum.auto()
    CHOOSE_STICKER: str = enum.auto()
