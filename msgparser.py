import xml.etree.ElementTree as ET
import message
import event


class MessageParser(object):
    MSG_TYPES = {
        'text': message.Text,
        'image': message.Image,
        'voice': message.Voice,
        'video': message.Video,
        'shortvideo': message.ShortVideo,
        'location': message.Location,
        'link': message.Link,
        'event': event.EventParser
    }

    def __init__(self):
        super(MessageParser, self).__init__()

    def parse(self, xml_string):
        root = ET.fromstring(xml_string)
        msg_type = root.findtext('MsgType')
        cls = MessageParser.MSG_TYPES.get(msg_type)
        if cls is not None:
            return cls.from_xml(xml_string)
        return None
