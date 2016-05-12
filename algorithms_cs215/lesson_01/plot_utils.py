
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import math

def plot_data(x_vals,y_vals):
    fig, ax = plt.subplots()
    ax.plot(x_vals,y_vals)
    ax.grid(True,which="both")

    # Set the x spine
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    # Show the plot 
    plt.show()
