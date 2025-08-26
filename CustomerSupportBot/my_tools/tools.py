from agents import function_tool

# Simulated orders database
orders = {
    "101": "Order 123 has been placed",
    "102": "Please wait for the order to be processed",
    "103": "Delivery has been confirmed",
}

def order_tool_error(order_id):
    return f"Sorry, no order found with ID {order_id}."

#run_context to chwck query
def is_order_query(run_context, _tool=None):
    query = str(run_context)
    return "order" in query.lower()

@function_tool(is_enabled=is_order_query)
def get_order_status(order_id: str) -> str:
    status = orders.get(order_id)
    if status:
        return f"Order {order_id} is currently {status}."
    else:
        return order_tool_error(order_id)
