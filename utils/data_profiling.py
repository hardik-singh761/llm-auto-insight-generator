import pandas as pd


def profile_dataset(csv_path):
    """
    Reads a CSV file and prints basic profiling information.
    """

    df = pd.read_csv(csv_path)

    print("----- DATASET OVERVIEW -----")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}\n")

    # Identify column types
    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()

    print("----- COLUMN TYPES -----")
    print(f"Numeric columns ({len(numeric_columns)}): {numeric_columns}")
    print(f"Categorical columns ({len(categorical_columns)}): {categorical_columns}\n")

    # Basic statistics for numeric columns
    if numeric_columns:
        print("----- BASIC STATISTICS (NUMERIC) -----")
        print(df[numeric_columns].describe())
        print()

    # Missing values
    print("----- MISSING VALUES -----")
    print(df.isnull().sum())
    print()

    # Detect columns suitable for charts
    chart_candidates = {
        "numerical": numeric_columns,
        "categorical": [
            col for col in categorical_columns if df[col].nunique() < 20
        ]
    }

    print("----- CHART-SUITABLE COLUMNS -----")
    print("Numerical (histogram / line):", chart_candidates["numerical"])
    print("Categorical (bar chart):", chart_candidates["categorical"])

    return chart_candidates


if __name__ == "__main__":
    # Example usage
    profile_dataset("data/sample_data.csv")
