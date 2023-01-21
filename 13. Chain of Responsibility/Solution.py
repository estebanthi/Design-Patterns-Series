from unittest.mock import Mock


sales_department = Mock()
sales_department.handle_order = Mock(side_effect=lambda order: print(f"Sales department handling order {order}"))
support_department = Mock()
support_department.handle_order = Mock(side_effect=lambda order: print(f"Support department handling order {order}"))
billing_department = Mock()
billing_department.handle_order = Mock(side_effect=lambda order: print(f"Billing department handling order {order}"))


class OrderHandler:
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def handle_order(self, order):
        if self._handle_order(order):
            return
        if self._next_handler:
            self._next_handler.handle_order(order)

    def _handle_order(self, order):
        raise NotImplementedError


class HighOrderHandler(OrderHandler):
    def _handle_order(self, order):
        if order["priority"] == "high":
            sales_department.handle_order(order)
            return True
        return False

class MediumOrderHandler(OrderHandler):
    def _handle_order(self, order):
        if order["priority"] == "medium":
            support_department.handle_order(order)
            return True
        return False

class LowOrderHandler(OrderHandler):
    def _handle_order(self, order):
        if order["priority"] == "low":
            billing_department.handle_order(order)
            return True
        return False


if __name__ == "__main__":
    order = {"priority": "low"}
    order_handler = HighOrderHandler(MediumOrderHandler(LowOrderHandler()))
    order_handler.handle_order(order)
