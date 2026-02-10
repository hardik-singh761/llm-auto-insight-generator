import matplotlib.pyplot as plt


def generate_chart(df, chart_config):
    column = chart_config["column"]
    chart_type = chart_config["chart_type"]

    plt.figure()

    if chart_type == "histogram":
        df[column].hist()
        plt.title(f"Distribution of {column}")

    elif chart_type == "bar":
        df[column].value_counts().plot(kind="bar")
        plt.title(f"{column} Distribution")

    plt.tight_layout()
    plt.savefig(f"visualization/outputs/{column}_{chart_type}.png")
    plt.close()