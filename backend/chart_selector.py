"""
This file decides which type of chart
should be generated for each column.
"""

def select_charts(profile_info):
    """
    Input:
        profile_info (dict): Output from data_profiling.py

    Output:
        List of chart configurations
    """

    charts = []

    # Numerical columns → Histogram
    for col in profile_info["numerical"]:
        charts.append({
            "column": col,
            "chart_type": "histogram"
        })

    # Categorical columns → Bar chart
    for col in profile_info["categorical"]:
        charts.append({
            "column": col,
            "chart_type": "bar"
        })  

    return charts


# Testing the function
if __name__ == "__main__":
    sample_profile = {
        "numerical": ["Sales", "Profit"],
        "categorical": ["Category", "Region"]
    }

    selected = select_charts(sample_profile)
    print(selected)
