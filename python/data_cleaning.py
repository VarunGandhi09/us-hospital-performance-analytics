
# ============================================================
# PROJECT: US Hospital Performance & Patient Experience
# MODULE: Initial Dataset Inspection
# AUTHOR: Varun Gandhi
# ============================================================

import pandas as pd
from pathlib import Path

# STEP 1: Locate the main project folder
BASE_DIR = Path(__file__).resolve().parents[1]

# STEP 2: Define the CSV file locations
hospital_file = (
    BASE_DIR / "data" / "raw" /
    "hospital_general_information.csv"
)

hcahps_file = (
    BASE_DIR / "data" / "raw" /
    "hcahps_patient_survey.csv"
)

# STEP 3: Check whether files exist
print("\n========== FILE VALIDATION ==========")

print("Hospital dataset exists:", hospital_file.exists())
print("HCAHPS dataset exists:", hcahps_file.exists())

# Stop if a file is missing
if not hospital_file.exists() or not hcahps_file.exists():
    raise FileNotFoundError(
        "One or both healthcare CSV files are missing. "
        "Please verify the filenames and data/raw folder."
    )

# STEP 4: Read first 5 records from each dataset
# dtype=str preserves IDs and ZIP codes as text.

hospitals = pd.read_csv(
    hospital_file,
    nrows=5,
    dtype=str
)

hcahps = pd.read_csv(
    hcahps_file,
    nrows=5,
    dtype=str
)

# STEP 5: Inspect Hospital General Information
print("\n========== HOSPITAL DATASET ==========")

print("Sample rows:", len(hospitals))
print("Total columns:", len(hospitals.columns))

print("\nColumn names:")
print(hospitals.columns.tolist())

print("\nFirst five records:")
print(hospitals.to_string(index=False))

# STEP 6: Inspect HCAHPS Patient Survey
print("\n========== HCAHPS DATASET ==========")

print("Sample rows:", len(hcahps))
print("Total columns:", len(hcahps.columns))

print("\nColumn names:")
print(hcahps.columns.tolist())

print("\nFirst five records:")
print(hcahps.to_string(index=False))

# STEP 7: Completion message
print("\n======================================")
print("INITIAL DATASET INSPECTION COMPLETED")
print("======================================")
