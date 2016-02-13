if __name__ == "__main__":
    budget = input()
    plastic_price = input()
    glass_price = input()
    glass_return = input()
    if glass_price - glass_return >= plastic_price \
        or budget < glass_price:
        print budget / plastic_price
    else:
        net_price = (glass_price - glass_return)
        bought_glass_bottles = (budget - glass_return) / net_price
        rest_budget = (budget - bought_glass_bottles * net_price)
        print bought_glass_bottles + rest_budget / plastic_price
