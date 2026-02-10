import pandas as pd
from utils.basic_cleaning import clean_dataset
from utils.data_profiling import profile_dataset
from backend.chart_selector import select_charts
from visualization.chart_generator import generate_chart


def run_pipeline():
    clean_dataset(
        "data/sample_data.csv",
        "data/cleaned_data.csv"
    )

    df = pd.read_csv("data/cleaned_data.csv")

    profile = profile_dataset("data/cleaned_data.csv")
    charts = select_charts(profile)

    for chart in charts:
        generate_chart(df, chart)


if __name__ == "__main__":
    run_pipeline()
