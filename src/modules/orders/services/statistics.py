from functools import reduce

import matplotlib.pyplot as plt

from ..models import Order


def get_total_income():
    """
    Return total income of all the orders.

    Get the prices from DB in dollars.
    """
    prices = Order.objects.values_list('price_in_dollars', flat=True)
    total_income = reduce(lambda a, b: a + b, prices)
    return total_income


def visualize_table_of_orders():
    pass


def visualize_graph_of_orders():
    """
    Creates a graph with x-axis of dates and y-axis of incomes.
    """
    x=[1,3,5,7]
    y=[2,4,6,1]
    plt.plot(x,y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("A simple line graph")
    plt.show()