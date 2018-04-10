import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
DPI = 100

def create_summary_graph(title, y_axis_label, labels, values, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, dpi=DPI):
    """Create summary (column) graph for any measurement."""
    N = len(values)
    indexes = np.arange(N)

    #fig = plt.figure()
    fig, ax = plt.subplots(figsize=(1.0 * width / dpi, 1.0 * height / dpi), dpi=dpi)

    plt.xlabel("call #")
    plt.ylabel(y_axis_label)
    plt.grid(True)
    plt.xticks(indexes, labels)
    locs, plt_labels = plt.xticks()
    #plt.setp(plt_labels, rotation=90)
    plt.bar(indexes, values, 0.80, color='yellow',
            edgecolor='black', label=title)

    # plt.legend(loc='lower right')

    for tick in plt_labels:
        tick.set_horizontalalignment("left")
        tick.set_verticalalignment("top")
        tick.set_visible(False)

    for tick in plt_labels:
        tick.set_visible(True)

    plt.tick_params(axis='x', which='major', labelsize=10)

    fig.subplots_adjust(bottom=0.1)
    fig.suptitle(title)
    return fig


def save_graph(fig, imageFile, dpi=DPI):
    """Save graph into the raster or vector file."""
    plt.savefig(imageFile, facecolor=fig.get_facecolor(), dpi=dpi)


def main():
    fig = create_summary_graph("pokus", "cas", ["a", "b", "c", "d"], [1,2,3,4])
    save_graph(fig, "test.png")
    plt.close(fig)


if __name__ == "__main__":
    main()
