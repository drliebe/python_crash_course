def sandwich_toppings(*toppings):
    print('Sandwich Toppings:')
    for topping in toppings:
        print(' - ' + topping)

sandwich_toppings('cheese', 'olives')
sandwich_toppings('peppers', 'onions', 'lettuce')
sandwich_toppings('mayo')    