from twisted.internet.protocol import Factory

from collections import deque
from Queue import Queue

from protocol import ChatProtocol


class ChatProtoFactory(Factory):

    def __init__(self):
        self.users = {}     # Map of users to chat instances
        self.store = deque(maxlen=100)    # Store last 100 messages
        self.queue = Queue(0)       # Infinitely long queue

    def build_chat_protocol(self, addr):
        return ChatProtocol(self.users, self.queue)
