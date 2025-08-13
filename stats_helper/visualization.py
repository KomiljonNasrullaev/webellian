import matplotlib.pyplot as plt

def histogram(df, column, bins=10):
    df[column].hist(bins=bins)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def boxplot(df, column):
    df.boxplot(column=column)
    plt.title(f"Boxplot of {column}")
    plt.show()

def scatter_plot(df, col_x, col_y):
    df.plot.scatter(x=col_x, y=col_y)
    plt.title(f"Scatter Plot: {col_x} vs {col_y}")
    plt.show()
