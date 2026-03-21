import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import os

OUTPUT_FOLDER = "visualization/outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_chart(df, chart):

    chart_type = chart["chart_type"]

    plt.figure(figsize=(6,4))

    # HISTOGRAM
    if chart_type == "histogram":

        column = chart["column"]
        sns.histplot(df[column], kde=True)

        filename = f"{column}_hist.png"


    # BOX PLOT
    elif chart_type == "box":

        column = chart["column"]
        sns.boxplot(x=df[column])

        filename = f"{column}_box.png"


    # BAR CHART
    elif chart_type == "bar":

        column = chart["column"]
        df[column].value_counts().head(10).plot(kind="bar")

        filename = f"{column}_bar.png"


    # PIE CHART
    elif chart_type == "pie":

        column = chart["column"]
        df[column].value_counts().head(5).plot(kind="pie", autopct='%1.1f%%')

        filename = f"{column}_pie.png"


    # SCATTER
    elif chart_type == "scatter":

        x = chart["x"]
        y = chart["y"]

        sns.scatterplot(x=df[x], y=df[y])

        filename = f"{x}_{y}_scatter.png"


    # HEATMAP
    elif chart_type == "heatmap":

        corr = df.select_dtypes(include=['int64','float64']).corr()

        sns.heatmap(corr, annot=True, cmap="coolwarm")

        filename = "correlation_heatmap.png"


    filepath = os.path.join(OUTPUT_FOLDER, filename)

    plt.title(chart_type.capitalize())
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()

    return filename