"""Q5: Functions, parameters, return values and scope."""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def bill(subtotal, gst_rate=0.05, *, discount=0):
    gst = (subtotal - discount) * gst_rate
    total = subtotal - discount + gst
    return total, gst

global_count = 0

def demonstrate_global():
    global global_count
    global_count += 1
    return global_count

def outer():
    message = "outer"
    def inner():
        nonlocal message
        message = "changed by inner"
    inner()
    return message

def local_example():
    local_value = "exists only inside this function"
    return local_value

if __name__ == "__main__":
    print("Buggy shared default:")
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Defaults:", add_item_buggy.__defaults__)
    print("Correct independent orders:")
    for customer, item in enumerate(("Tea", "Vada", "Coffee"), start=1):
        print(f"Customer {customer}:", add_item(item))
    total, gst = bill(200, gst_rate=0.05, discount=10)
    print("Total:", round(total, 2), "GST:", round(gst, 2))
    print("Global:", demonstrate_global())
    print("Nonlocal:", outer())
    print("Local:", local_example())
