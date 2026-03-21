import pandas as pd

from utils.basic_cleaning import clean_dataset
from utils.data_profiling import profile_dataset

from backend.chart_selector import select_charts
from backend.statistics_generator import generate_statistics

from visualization.chart_generator import generate_chart

from llm.prompt_builder import build_prompt
from llm.llm_client import call_llm


def run_pipeline(input_csv):
    
    clean_dataset(input_csv, "data/cleaned_data.csv")

    df = pd.read_csv("data/cleaned_data.csv")

    profile = profile_dataset("data/cleaned_data.csv")

    charts = select_charts(df)

    stats = generate_statistics(df)

    insights = []

    for chart in charts:

        chart_path = generate_chart(df, chart)

        chart_type = chart["chart_type"]

        # Scatter chart
        if chart_type == "scatter":
            column_name = f"{chart['x']} vs {chart['y']}"
            stats_data = {}

        # Heatmap chart
        elif chart_type == "heatmap":
            column_name = "Correlation Matrix"
            stats_data = {}

        # All other charts
        else:
            column_name = chart.get("column", "Unknown Column")
            stats_data = stats.get(column_name, {})

        prompt = build_prompt(column_name, stats_data, chart_type)

        insight = call_llm(prompt)

        insights.append({
            "column": column_name,
            "chart_type": chart_type,
            "insight": insight,
            "chart": chart_path
        })

    return insights