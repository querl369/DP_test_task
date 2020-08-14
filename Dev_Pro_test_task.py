#First Task
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('some_URL')


def scroll():
    return 'next 10'

def is_displayed():
    return True if 'some condition' else False

def scroll_to(item):
    if is_displayed is True: # if element displayed so we can get it
        driver.find_elemet_by_id(f'{item}') # or it can be found by css selector for example
        return True
    else:
        return False


# Second Task
# just wanted to check myself


# def get_product_by_id(id):
#     names = {
#         1 : 'Burger',
#         2 : 'Shawarma',
#         3 : 'Sandwich',
#         4 : 'Hot Dog'
#     }
#     if id in names.keys():
#         return names[id]
#
# def get_extra_products(get_product_by_id):
#     ingridients = {
#         'Burger' : ['Cheese', 'Bread', 'Salad', 'Meat'],
#         'Shawarma' :  ['Pita', 'Salad', 'Cheese', 'Meat', 'Ketchup', 'Carrot', 'Mustard'],
#         'Sandwich' :  ['Bread', 'Salad', 'Meat', 'Ketchup'],
#         'Hot Dog' : ['Bun', 'Sausage', 'Mayonaise', 'Ketchup', 'Mustard']
#     }
#     if get_product_by_id in ingridients.keys():
#         return ingridients[get_product_by_id]



def count_extra_products():
    products = {}
    for j in range(1, 11):
        for i in get_extra_products(get_product_by_id(j)):
            if i in products.keys():
                products[i] += 1
            else:
                products[i] = 1
    return products

