import requests
import pandas as pd

# Official Himalayas API
URL = "https://himalayas.app/jobs/api"

params = {
    "limit": 20
}

print("Connecting to Himalayas...")

try:
    response = requests.get(URL, params=params, timeout=30)

    print("Status Code:", response.status_code)

    response.raise_for_status()

    data = response.json()

    jobs = data.get("jobs", [])

    print("Total jobs available:", data.get("totalCount"))
    print("Jobs received:", len(jobs))

    if jobs:
        for job in jobs[:5]:
            print("----------------------------")
            print("Title:", job.get("title"))
            print("Company:", job.get("companyName"))
            print("Location:", job.get("locationRestrictions"))
            print("URL:", job.get("applicationLink"))

        df = pd.DataFrame(jobs)

        df.to_csv(
            "himalayas_test.csv",
            index=False,
            encoding="utf-8-sig"
        )

        print("\nFile saved: himalayas_test.csv")

    else:
        print("No jobs found.")

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

except requests.exceptions.RequestException as e:
    print("Connection error:", e)

except ValueError:
    print("The response is not valid JSON.")
