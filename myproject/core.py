import matplotlib.pyplot as plt
import matplotlib.patches as mpa

def get_circle_plot():
    """This function plots a circle."""
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    ax.add_patch(mpa.Circle([.5, .5], 0.25))
    return fig
