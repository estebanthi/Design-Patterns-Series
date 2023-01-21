from unittest.mock import Mock


sales_department = Mock()
sales_department.handle_order = Mock(side_effect=lambda order: print(f"Sales department handling order {order}"))
support_department = Mock()
support_department.handle_order = Mock(side_effect=lambda order: print(f"Support department handling order {order}"))
billing_department = Mock()
billing_department.handle_order = Mock(side_effect=lambda order: print(f"Billing department handling order {order}"))


def process_order(order):
    if order["priority"] == "high":
        sales_department.handle_order(order)
    elif order["priority"] == "medium":
        support_department.handle_order(order)
    elif order["priority"] == "low":
        billing_department.handle_order(order)


if __name__ == "__main__":
    order = {"priority": "low"}
    process_order(order)
