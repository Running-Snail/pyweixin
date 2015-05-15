class MsgHandleController(object):
    """docstring for MsgHandleController"""
    def __init__(self):
        super(MsgHandleController, self).__init__()
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle(self, msg):
        for h in self.handlers:
            if h.match(msg):
                return h.handle(msg)
            else:
                try:
                    return h.handle_not_match(msg)
                except NotImplementedError:
                    pass
        return False
