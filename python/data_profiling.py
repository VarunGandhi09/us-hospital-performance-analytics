
# ============================================================
# PROJECT: US Hospital Performance & Patient Experience
# MODULE: Full Dataset Profiling
# AUTHOR: Varun Gandhi
# ============================================================

import pandas as pd
from pathlib import Path

# STEP 1: Project directory
BASE_DIR = Path(__file__).resolve().parents[1]

# STEP 2: Dataset paths
hospital_file = BASE_DIR / "data" / "raw" / "hospital_general_information.csv"
hcahps_file = BASE_DIR / "data" / "raw" / "hcahps_patient_survey.csv"

# STEP 3: Create reports folder
REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

print("\nLoading complete healthcare datasets...")

# STEP 4: Load complete datasets
hospitals = pd.read_csv(hospital_file, dtype=str, low_memory=False)
hcahps = pd.read_csv(hcahps_file, dtype=str, low_memory=False)

# STEP 5: Basic dataset information
print("\n========== DATASET OVERVIEW ==========")

print("\nHospital Dataset")
print("Total records:", hospitals.shape[0])
print("Total columns:", hospitals.shape[1])

print("\nHCAHPS Dataset")
print("Total records:", hcahps.shape[0])
print("Total columns:", hcahps.shape[1])

# STEP 6: Missing value analysis
def missing_value_report(df, dataset_name):

    missing = df.isnull().sum()

    report = pd.DataFrame({
        "Column": missing.index,
        "Missing_Count": missing.values,
        "Missing_Percentage": (
            missing.values / len(df) * 100
        ).round(2)
    })

    report = report.sort_values(
        by="Missing_Percentage",
        ascending=False
    )

    report.to_csv(
        REPORT_DIR / f"{dataset_name}_missing_values.csv",
        index=False
    )

    print(f"\n{dataset_name} - Missing Values")
    print(report.head(15).to_string(index=False))

# Generate missing value reports
missing_value_report(hospitals, "hospital")
missing_value_report(hcahps, "hcahps")

# STEP 7: Duplicate record analysis
print("\n========== DUPLICATE ANALYSIS ==========")

print(
    "Hospital duplicate rows:",
    hospitals.duplicated().sum()
)

print(
    "HCAHPS duplicate rows:",
    hcahps.duplicated().sum()
)

# STEP 8: Facility ID analysis
hospital_ids = hospitals["Facility ID"].dropna().str.strip()
hcahps_ids = hcahps["Facility ID"].dropna().str.strip()

unique_hospital_ids = set(hospital_ids.unique())
unique_hcahps_ids = set(hcahps_ids.unique())

common_ids = unique_hospital_ids.intersection(
    unique_hcahps_ids
)

print("\n========== FACILITY ID ANALYSIS ==========")

print("Unique hospital IDs:", len(unique_hospital_ids))
print("Unique HCAHPS hospital IDs:", len(unique_hcahps_ids))
print("Matching Facility IDs:", len(common_ids))

print(
    "Hospital IDs without HCAHPS match:",
    len(unique_hospital_ids - unique_hcahps_ids)
)

print(
    "HCAHPS IDs without hospital match:",
    len(unique_hcahps_ids - unique_hospital_ids)
)

# STEP 9: Hospital identifier duplicate check
print("\nHospital Facility ID duplicate count:",
      hospital_ids.duplicated().sum())

# STEP 10: Save dataset summary
summary = pd.DataFrame({
    "Dataset": ["Hospital General Information", "HCAHPS Patient Survey"],
    "Total_Rows": [len(hospitals), len(hcahps)],
    "Total_Columns": [len(hospitals.columns), len(hcahps.columns)],
    "Duplicate_Rows": [
        hospitals.duplicated().sum(),
        hcahps.duplicated().sum()
    ]
})

summary.to_csv(
    REPORT_DIR / "dataset_summary.csv",
    index=False
)

print("\n========== PROFILING COMPLETED ==========")
print("Reports saved in:", REPORT_DIR)
