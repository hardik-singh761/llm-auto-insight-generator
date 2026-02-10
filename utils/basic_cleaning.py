import pandas as pd


def clean_dataset(input_csv, output_csv):
    """
    Cleans the dataset by handling missing values
    and removing empty columns.
    """

    df = pd.read_csv(input_csv)

    print("Original shape:", df.shape)

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    # Handle missing values
    for column in df.columns:
        if df[column].dtype in ["int64", "float64"]:
            # Fill numeric missing values with mean
            df[column] = df[column].fillna(df[column].mean())
        else:
            # Fill categorical missing values with mode
            df[column] = df[column].fillna(df[column].mode()[0])

    print("Cleaned shape:", df.shape)

    # Save cleaned dataset
    df.to_csv(output_csv, index=False)
    print(f"Cleaned dataset saved to: {output_csv}")


if __name__ == "__main__":
    clean_dataset(
        input_csv="../data/sample_data.csv",
        output_csv="../data/cleaned_data.csv"
    )
