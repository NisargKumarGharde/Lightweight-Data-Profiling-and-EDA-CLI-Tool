import pandas as pd
import os
import argparse

def get_csv_insights(file_path):
    """
    Reads a CSV file, provides quick insights, and saves cleaned data.

    Args:
        file_path (str): The path to the CSV file.
    """
    try:
        # 1. Read the CSV file
        df = pd.read_csv(file_path)
        print(f"\n--- Insights for '{file_path}' ---")

        # 2. Show file structure (columns, types, non-null counts)
        print("\n--- File Structure (Columns, Data Types, Non-Null Counts) ---")
        df.info()

        # 3. Show top 5 rows
        print("\n--- Top 5 Rows ---")
        print(df.head().to_markdown(index=False)) # Using to_markdown for better display

        # 4. Show bottom 5 rows
        print("\n--- Bottom 5 Rows ---")
        print(df.tail().to_markdown(index=False)) # Using to_markdown for better display

        # 5. Count of unique values per column
        print("\n--- Unique Values Per Column ---")
        unique_counts = {}
        for col in df.columns:
            unique_counts[col] = df[col].nunique()
        print(pd.Series(unique_counts).to_markdown()) # Display as a Series for neatness

        # 6. Save cleaned data to a new CSV
        # Basic cleaning: dropping duplicate rows
        initial_rows = len(df)
        df_cleaned = df.drop_duplicates()
        rows_after_cleaning = len(df_cleaned)

        print(f"\n--- Data Cleaning ---")
        if initial_rows > rows_after_cleaning:
            print(f"Removed {initial_rows - rows_after_cleaning} duplicate row(s).")
        else:
            print("No duplicate rows found or removed.")

        # Construct new file name
        base_name = os.path.basename(file_path)
        dir_name = os.path.dirname(file_path)
        new_file_name = f"cleaned_data_{base_name}"
        output_file_path = os.path.join(dir_name, new_file_name)

        df_cleaned.to_csv(output_file_path, index=False)
        print(f"Cleaned data saved to: '{output_file_path}'")
        print("\n--- Analysis Complete ---")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Lightweight CSV Data Profiler and Cleaner.")
    parser.add_argument(
        "-f", "--file", 
        required=True, 
        help="Absolute or relative path to the target CSV file"
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    print("Starting the CSV Quick Insights Tool...")
    get_csv_insights(args.file)
