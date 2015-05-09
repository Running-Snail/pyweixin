import time
import helper


class Message(object):
    def __init__(self, data):
        super(Message, self).__init__()
        self.to_user_name = data.get('ToUserName', '')
        self.from_user_name = data.get('FromUserName', '')
        self.msg_type = data.get('MsgType', '')
        self.create_time = str(data.get('CreateTime', int(time.time())))

    @staticmethod
    def from_xml(xml_string):
        return Message(helper.xml2dict(xml_string))


class Text(Message):
    """docstring for Text"""
    def __init__(self, data):
        super(Text, self).__init__(data)
        self.content = data.get('Content', '')

    @staticmethod
    def from_xml(xml_string):
        return Text(helper.xml2dict(xml_string))


class Image(Message):
    """docstring for Image"""
    def __init__(self, data):
        super(Image, self).__init__(data)
        self.picurl = data.get('PicUrl', '')
        self.media_id = data.get('MediaId', '')

    @staticmethod
    def from_xml(xml_string):
        return Image(helper.xml2dict(xml_string))


class Voice(Message):
    def __init__(self, data):
        super(Voice, self).__init__(data)
        self.format = data.get('Format', '')
        self.media_id = data.get('MediaId', '')
        self.recognition = data.get('Recognition', '')

    @staticmethod
    def from_xml(xml_string):
        print helper.xml2dict(xml_string)
        return Voice(helper.xml2dict(xml_string))


class Video(Message):
    def __init__(self, data):
        super(Video, self).__init__(data)
        self.thumb_media_id = data.get('ThumbMediaId', '')
        self.media_id = data.get('MediaId', '')

    @staticmethod
    def from_xml(xml_string):
        return Video(helper.xml2dict(xml_string))


class ShortVideo(Message):
    def __init__(self, data):
        super(ShortVideo, self).__init__(data)
        self.thumb_media_id = data.get('ThumbMediaId', '')
        self.media_id = data.get('MediaId', '')

    @staticmethod
    def from_xml(xml_string):
        return ShortVideo(helper.xml2dict(xml_string))


class Location(Message):
    def __init__(self, data):
        super(Location, self).__init__(data)
        self.location_x = float(data.get('Location_X', 0))
        self.location_y = float(data.get('Location_Y', 0))
        self.scale = data.get('Scale', '')
        self.label = data.get('Label', '')

    @staticmethod
    def from_xml(xml_string):
        return Location(helper.xml2dict(xml_string))


class Link(Message):
    def __init__(self, data):
        super(Link, self).__init__(data)
        self.title = data.get('Title', '')
        self.description = data.get('Description', '')
        self.url = data.get('Url', '')

    @staticmethod
    def from_xml(xml_string):
        return Link(helper.xml2dict(xml_string))
