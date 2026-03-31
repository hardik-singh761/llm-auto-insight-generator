import pandas as pd

def select_charts(df, selected=None):

    charts = []

    if selected is None:
        selected = ["histogram","box","bar","pie","scatter","heatmap"]

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns


    # HISTOGRAM
    if "histogram" in selected:
        for col in numeric_cols:
            charts.append({
                "column": col,
                "chart_type": "histogram"
            })


    # BOX PLOT
    if "box" in selected:
        for col in numeric_cols:
            charts.append({
                "column": col,
                "chart_type": "box"
            })


    # BAR CHART
    if "bar" in selected:
        for col in categorical_cols[:2]:
            charts.append({
                "column": col,
                "chart_type": "bar"
            })


    # PIE CHART
    if "pie" in selected:
        for col in categorical_cols[:2]:
            charts.append({
                "column": col,
                "chart_type": "pie"
            })


    # FEATURE vs FEATURE SCATTER
    if "scatter" in selected:

        numeric_cols = list(numeric_cols)

        # choose first feature as reference
        base_feature = numeric_cols[0] if len(numeric_cols) > 0 else None

        if base_feature:

            for col in numeric_cols[1:4]:   # limit to avoid too many graphs

                charts.append({
                    "x": base_feature,
                    "y": col,
                    "chart_type": "scatter"
                })


    # HEATMAP
    if "heatmap" in selected:

        charts.append({
            "chart_type": "heatmap"
        })


    return charts