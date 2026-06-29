import pandas as pd
import logging
import logger


def clean_data(df, keyword, results):
    """
    Clean and filter job data based on the search keyword.
    """

    logging.info("-------- Starting data cleaning --------")

    # Keep only the columns required for analysis.
    columns_we_want = [
        "id",
        "company",
        "position",
        "tags",
        "salary_min",
        "salary_max",
        "date",
    ]

    existing_columns = [col for col in columns_we_want if col in df.columns]
    df = df[existing_columns].copy()

    results.append({
        "Validation": "Column Selection",
        "Status": "PASS",
        "Message": f"Kept {len(existing_columns)} columns: {existing_columns}"
    })

    # Convert salary columns to numeric values.
    if "salary_min" in df.columns:
        df["salary_min"] = pd.to_numeric(
            df["salary_min"], errors="coerce"
        ).fillna(0)

    if "salary_max" in df.columns:
        df["salary_max"] = pd.to_numeric(
            df["salary_max"], errors="coerce"
        ).fillna(0)

    # Remove duplicate jobs based on the job ID.
    rows_before = len(df)

    if "id" in df.columns:
        df = df.drop_duplicates(subset=["id"])

    rows_after = len(df)
    duplicates_removed = rows_before - rows_after

    results.append({
        "Validation": "Duplicate Check",
        "Status": "PASS",
        "Message": f"Removed {duplicates_removed} duplicate rows. {rows_after} rows remaining."
    })

    keyword_lower = keyword.lower()

    # Filter jobs where the keyword appears in either tags or position.
    if "tags" in df.columns:

        df["tags_str"] = df["tags"].apply(
            lambda x: ",".join(x) if isinstance(x, list) else ""
        )

        tag_match = df["tags_str"].str.contains(
            keyword_lower,
            case=False,
            na=False,
        )

        position_match = df["position"].str.contains(
            keyword_lower,
            case=False,
            na=False,
        )

        df = df[tag_match | position_match]

    else:

        df = df[
            df["position"].str.contains(
                keyword_lower,
                case=False,
                na=False,
            )
        ]

    results.append({
        "Validation": "Keyword Filter",
        "Status": "PASS",
        "Message": f"Found {len(df)} matching jobs for '{keyword}'."
    })

    # Remove the temporary helper column.
    if "tags_str" in df.columns:
        df = df.drop(columns=["tags_str"])

    # Reset index after filtering.
    df = df.reset_index(drop=True)

    logging.info("Data cleaning completed successfully.")

    return df