import sys
import os
import pandas as pd
from scraper import fetch_jobs
from data_cleaner import clean_data


def main():

    # Shared validation results for the entire execution
    results = []

    if len(sys.argv) < 2:
        print("Usage: python main.py <keyword>")
        print("Example: python main.py python")
        sys.exit(1)

    # Read the search keyword
    keyword = sys.argv[1].lower()

    print(f"\n🔍 Searching for '{keyword}' jobs on RemoteOK...\n")

    # Fetch data from the API
    raw_df, results = fetch_jobs(results)

    # Clean and filter the data
    clean_df = clean_data(raw_df, keyword, results)

    # Exit if no matching jobs are found
    if clean_df.empty:
        results.append({
            "Validation": "Keyword Filter",
            "Status": "FAIL",
            "Message": f"No jobs found for '{keyword}'."
        })

        print(f"\nNo jobs found for '{keyword}'. Try a different keyword.")
        sys.exit(0)

    # Create output folder if it doesn't exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Save cleaned data
    csv_path = os.path.join(output_folder, "jobs_clean.csv")
    clean_df.to_csv(csv_path, index=False)

    results.append({
        "Validation": "CSV Export",
        "Status": "PASS",
        "Message": f"CSV saved to {csv_path}"
    })

    # Save validation report
    report_df = pd.DataFrame(results)

    report_path = os.path.join(output_folder, "validation_report.csv")
    report_df.to_csv(report_path, index=False)

    print("\n" + "=" * 50)
    print("✅ All done!")
    print(f"Keyword    : {keyword}")
    print(f"Jobs found : {len(clean_df)}")
    print(f"CSV        : {csv_path}")
    print("=" * 50)

    print("\nValidation Results")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()