class Message(object):
    MSG_TYPE = 'MsgType'
    EVENT = 'Event'
    FROM_USER_NAME = 'FromUserName'
    TO_USER_NAME = 'ToUserName'
    CREATE_TIME = 'CreateTime'
    CONTENT = 'Content'
    MSG_ID = 'MsgId'
    MEDIA_ID = 'MediaId'
    FORMAT = 'Format'
    THUMB_MEDIA_ID = 'ThumbMediaId'
    LOCATION_X = 'Location_X'
    LOCATION_Y = 'Location_Y'
    SCALE = 'Scale'
    LABEL = 'Label'
    TITLE = 'Title'
    DESCRIPTION = 'Description'
    EVENT_KEY = 'EventKey'
    TICKET = 'Ticket'
    LATITUDE = 'Latitude'
    LONGTITUDE = 'Longitude'
    PRECISION = 'Precision'

    def __init__(self, data):
        super(Message, self).__init__()
        self.data = data

    def __getitem__(self, key):
        return self.data.get(key, '')

    def __setitem__(self, key, value):
        self.data[key] = value

    def is_type(self, type_name):
        return self[Message.MSG_TYPE] == type_name

    def is_event_type(self, event_type):
        return self[Message.EVENT] == event_type

    def is_event(self):
        return self.is_type('event')

    def is_text(self):
        return self.is_type('text')

    def is_image(self):
        return self.is_type('image')

    def is_voice(self):
        return self.is_type('voice')

    def is_video(self):
        return self.is_type('video')

    def is_short_video(self):
        return self.is_type('shortvideo')

    def is_location(self):
        return self.is_type('location')

    def is_link(self):
        return self.is_type('link')

    def is_subscribe(self):
        return self[Message.EVENT] == 'subscribe'

    def is_unsubscribe(self):
        return self[Message.EVENT] == 'unsubscribe'

    def check_event_key(self, key):
        return self[Message.EVENT_KEY] == key

    def is_qrcode(self, subscribe=True):
        if subscribe:
            return self[Message.EVENT_KEY] == 'SCAN'
        return (self.is_event_type('subscribe') and
                'Ticket' in self.data)

    def is_location_event(self):
        return self.is_event_type('LOCATION')

    def is_click_event(self):
        return self.is_event_type('CLICK')

    def is_view_event(self):
        return self.is_event_type('VIEW')

    def is_msg(self):
        return not self.is_event()
