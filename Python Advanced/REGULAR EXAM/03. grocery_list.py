def shop_from_grocery_list(budget, to_buy_list, *args):
    bought_products = set()
    to_buy_list = set(to_buy_list)
    result = []

    for product in args:
        if product[0] in to_buy_list:
            if product[0] not in bought_products:
                if budget - product[1] >= 0:
                    bought_products.add(product[0])
                    budget -= product[1]
                else:
                    break



    if to_buy_list.issubset(bought_products):
        result.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        not_matching = [el for el in to_buy_list if el not in bought_products]
        result.append(f"You did not buy all the products. Missing products: {', '.join([str(x) for x in not_matching])}.")

    return ''.join(result)




print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
