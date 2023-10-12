def orders(orders):
    sorted_orders = {1:[], 2:[], 3:[]}
    for order in orders.split(' '):
        sorted_orders[int(order[0])].append(int(order[1:]))
    print(sorted_orders)
    
    out_of_order = 0
    for kiosk in sorted_orders:
        try:
            max_order = sorted_orders[kiosk][0]
        except IndexError:
            continue
        for order in sorted_orders[kiosk]:
            if order < max_order:
                out_of_order += 1
            if order > max_order:
                max_order = order
    print(out_of_order)

orders('328 105 267 269 108 266')