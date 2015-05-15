class MsgHandler(object):
    def __init__(self):
        super(MsgHandler, self)

    def match(self, msg):
        raise NotImplementedError()

    def handle(self, msg):
        raise NotImplementedError()

    def handle_not_match(self, msg):
        raise NotImplementedError()
