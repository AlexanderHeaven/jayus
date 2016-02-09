from twisted.internet.protocol import Factory

from collections import deque
from Queue import Queue


class ChatProtoFactory(Factory):

    def __init__(self):
        self.users = {}     # Map of users to chat instances
        self.store = deque({}, 100)    # 100 entry map user to message
        self.queue = Queue(0)       # Infinitely long queue

    def build_chat_protocol(self):
        pass
