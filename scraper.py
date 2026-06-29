import requests
import pandas as pd
import logging
import logger



def fetch_jobs(results):
    """
    Fetch remote jobs from the RemoteOK API and
    return both the job DataFrame and validation results.
    """

    logging.info("Started reading RemoteOK API")

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "twp-python-cookbook/1.0"
    }

    try:
        # Send API request
        response = requests.get(url, headers=headers, timeout=15)

        # Validate status code
        if response.status_code == 200:

            logging.info("API returned status code 200")

            results.append({
                "Validation": "API Status Code",
                "Status": "PASS",
                "Message": "API returned status code 200"
            })

        else:

            error_msg = f"Expected 200 but received {response.status_code}"

            logging.error(error_msg)

            results.append({
                "Validation": "API Status Code",
                "Status": "FAIL",
                "Message": error_msg
            })

            raise Exception(error_msg)

        # Convert JSON into Python objects
        raw_data = response.json()

        # Skip metadata
        jobs_list = raw_data[1:]

        logging.info(f"Fetched {len(jobs_list)} jobs")

        results.append({
            "Validation": "Job Count",
            "Status": "PASS",
            "Message": f"Fetched {len(jobs_list)} jobs"
        })

        # Convert to DataFrame
        df = pd.DataFrame(jobs_list)

        logging.info("DataFrame created successfully")

        return df, results

    except Exception as e:

        logging.exception("Unexpected error while fetching jobs")

        results.append({
            "Validation": "Execution",
            "Status": "FAIL",
            "Message": str(e)
        })

        return pd.DataFrame(), results


"""# Run the function
jobs_df, results = fetch_jobs()

# Validation report
report_df = pd.DataFrame(results)

print(report_df)
print(jobs_df.head())
"""