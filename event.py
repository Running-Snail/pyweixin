import helper
import time


class Event(object):
    def __init__(self, data):
        super(Event, self).__init__()
        self.to_user_name = data.get('ToUserName', '')
        self.from_user_name = data.get('FromUserName', '')
        self.msg_type = data.get('MsgType', '')
        self.create_time = str(data.get('CreateTime', int(time.time())))
        self.event = data.get('Event', '')

    @staticmethod
    def from_xml(xml_string):
        return Event(helper.xml2dict(xml_string))


class SubscribeEvent(Event):
    def __init__(self, data):
        super(SubscribeEvent, self).__init__(data)

    @staticmethod
    def from_xml(xml_string):
        return SubscribeEvent(helper.xml2dict(xml_string))


class UnsubscribeEvent(Event):
    def __init__(self, data):
        super(UnsubscribeEvent, self).__init__(data)

    @staticmethod
    def from_xml(xml_string):
        return UnsubscribeEvent(helper.xml2dict(xml_string))


class EventParser(object):
    EVENT_TYPE = {
        'subscribe': SubscribeEvent,
        'unsubscribe': UnsubscribeEvent
    }

    def __init__(self):
        super(EventParser, self).__init__()

    @staticmethod
    def from_xml(xml_string):
        xml_dict = helper.xml2dict(xml_string)
        cls = EventParser.EVENT_TYPE.get(xml_dict['Event'])
        if cls is not None:
            return cls.from_xml(xml_string)
        return None


