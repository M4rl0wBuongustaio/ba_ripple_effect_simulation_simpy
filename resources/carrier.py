from config import ROUTING


class Carrier:
    def __init__(self, env, delivery):
        self.env = env
        self.delivery = delivery

    def deliver(self):
        debtor_address = self.delivery.get_debtor().get_address()
        yield self.env.timeout(ROUTING[debtor_address])
        self.delivery.get_debtor().receive_delivery(self.delivery)
