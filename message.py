class Message(object):
    MSG_TYPE_KEY = 'MsgType'
    EVENT_KEY = 'Event'

    def __init__(self, data):
        super(Message, self).__init__()
        self.data = data

    def __getitem__(self, key):
        return self.data.get(key, '')

    def __setitem__(self, key, value):
        self.data[key] = value

    def is_type(self, type_name):
        return self[Message.MSG_TYPE_KEY] == type_name

    def is_event_type(self, event_type):
        return self[Message.EVENT_KEY] == event_type

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
        return self[Message.EVENT_KEY] == 'subscribe'

    def is_unsubscribe(self):
        return self[Message.EVENT_KEY] == 'unsubscribe'

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
