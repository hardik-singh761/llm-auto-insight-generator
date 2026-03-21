def build_prompt(column, stats, chart_type):

    return f"""
You are a data analyst.

Analyze the dataset column: {column}

Chart Type: {chart_type}

Statistics:
Mean: {stats.get('mean')}
Median: {stats.get('median')}
Max: {stats.get('max')}
Min: {stats.get('min')}

Explain the pattern or trend in simple language in 2 sentences.
"""