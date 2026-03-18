def build_prompt(column, stats, chart_type):
    prompt = f"""
    Column Name: {column}
    Chart Type: {chart_type}
    Statistics: {stats}

    Explain the main insight in simple language.
    """
    return prompt