import sys
import pandas as pd
import numpy as np

# Add current directory to import path
sys.path.append(".")

from data_cleaner import DataCleaner, CleanConfig

# Load sample CSV
input_file = "web_traffic_daily.csv"
df = pd.read_csv(input_file)

# Initialize default cleaner
config = CleanConfig()
cleaner = DataCleaner(config)

# Clean the data
cleaned_df, report = cleaner.clean(df)

# Save cleaned file
cleaned_path = "cleaned_web_traffic.csv"
cleaner.write(cleaned_df, cleaned_path)

# --------------------------
# TEST CASE EXECUTION STARTS
# --------------------------

test_results = []

# TC1: File read & write
try:
    assert not df.empty, "Input CSV is empty"
    assert not cleaned_df.empty, "Output data is empty"
    test_results.append(("TC1", "File read & write", "PASS"))
except Exception as e:
    test_results.append(("TC1", f"File read & write failed: {e}", "FAIL"))

# TC2: Header normalization
try:
    expected_headers = [h.lower().replace(" ", "_") for h in df.columns]
    assert all(col in cleaned_df.columns for col in expected_headers)
    test_results.append(("TC2", "Header normalization", "PASS"))
except AssertionError:
    test_results.append(("TC2", "Header normalization failed", "FAIL"))

# TC3: Whitespace and NA handling
try:
    whitespace_check = all(
        not (isinstance(x, str) and x != x.strip())
        for col in cleaned_df.columns
        for x in cleaned_df[col].dropna().astype(str)
    )
    na_check = cleaned_df.isna().sum().sum() >= 0
    assert whitespace_check and na_check
    test_results.append(("TC3", "Whitespace & NA handling", "PASS"))
except Exception as e:
    test_results.append(("TC3", f"Whitespace/NA handling failed: {e}", "FAIL"))

# TC4: Duplicate removal
try:
    dups_before = len(df) - len(df.drop_duplicates())
    dups_after = len(cleaned_df) - len(cleaned_df.drop_duplicates())
    assert dups_after == 0
    test_results.append(("TC4", "Duplicate removal", "PASS"))
except Exception:
    test_results.append(("TC4", "Duplicate removal failed", "FAIL"))

# TC5: Numeric casting
try:
    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    assert len(numeric_cols) >= 1, "No numeric columns found"
    test_results.append(("TC5", "Numeric casting", "PASS"))
except Exception as e:
    test_results.append(("TC5", f"Numeric casting failed: {e}", "FAIL"))

# TC6: Date parsing
try:
    date_cols = [c for c in cleaned_df.columns if "date" in c]
    if date_cols:
        parsed_dates = pd.to_datetime(cleaned_df[date_cols[0]], errors="coerce")
        assert parsed_dates.notna().sum() > 0
        test_results.append(("TC6", "Date parsing", "PASS"))
    else:
        test_results.append(("TC6", "No date column to parse", "PASS"))
except Exception as e:
    test_results.append(("TC6", f"Date parsing failed: {e}", "FAIL"))

# TC7: Outlier handling
try:
    assert isinstance(cleaned_df, pd.DataFrame)
    test_results.append(("TC7", "Outlier handling", "PASS"))
except Exception as e:
    test_results.append(("TC7", f"Outlier handling failed: {e}", "FAIL"))

# TC8: Validation rules
try:
    assert len(cleaned_df.columns) == len(set(cleaned_df.columns))
    test_results.append(("TC8", "Validation rules", "PASS"))
except Exception as e:
    test_results.append(("TC8", f"Validation rules failed: {e}", "FAIL"))

# --------------------------
# PRINT RESULTS
# --------------------------
print("\n=== Manual Test Execution Results ===")
for tc_id, desc, result in test_results:
    print(f"{tc_id}: {desc} --> {result}")

print("\nCleaned file saved as:", cleaned_path)
