#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from _class import *

def barchart():
    #labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    #mal_quantity = [20, 34, 30, 35, 27]
    mall = Mall()
    labels = mall_nameList
    mal_quantity = mall_qtyList

    
    x = np.arange(len(labels))  # the label locations
    width = 0.5  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, mal_quantity, width, label='qty')
    #rects2 = ax.bar(x + width/2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('quantity')
    ax.set_title('TEST bar chart')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    #ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def draw_plot():
    print('matplotlib init')
    plt.plot([1,2,3,4])
    plt.ylabel('y-xis')
    plt.show()

#if __name__ == "__main__":
    