from twisted.protocols.basic import LineReceiver


class ChatProtocol(LineReceiver):

    def __init__(self, users, queue):
        self.users = users
        self.queue = queue
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self.sendLine("What's your name?")

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_connect(line)
        else:
            self.handle_chat(line)

    def handle_connect(self, name):
        if name in self.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome %s!" % (name,))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"
        """ Send the store here. Something like:
            for line in store:
                sendLine(line)
        """

    def handle_chat(self, message):
        message = "<$s> %s" % (self.name, message)
        # put message on the queue and send it
        # add message to the store
