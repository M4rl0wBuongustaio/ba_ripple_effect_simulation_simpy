from resources import order


class Customer:
    def __init__(self, env, quantity, wholesaler, address, delivery_monitoring, iteration):
        self.env = env
        self.quantity = quantity
        self.wholesaler = wholesaler
        self.address = address
        self.delivery_monitoring = delivery_monitoring
        self.iteration = iteration

    def get_quantity(self):
        return self.quantity

    def get_wholesaler(self):
        return self.wholesaler

    def get_address(self):
        return self.address

    def get_id(self):
        return id(self)

    def place_order(self):
        self.wholesaler.receive_order(order.Order(self.quantity, self))

    def receive_delivery(self, delivery):
        self.delivery_monitoring[0].append(self.iteration)
        self.delivery_monitoring[1].append(self.env.now)
        # Record remaining shelf life.
        self.delivery_monitoring[2].append(delivery.get_product_batch()[0].get_expiration_date() - self.env.now)
