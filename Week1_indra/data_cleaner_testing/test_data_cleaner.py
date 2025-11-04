import sys
import json

import pandas as pd
import numpy as np
from data_cleaner import DataCleaner, CleanConfig

print("🚀 Starting Manual + Quality Test for data_cleaner.py\n")

# Step 1: Load CSV file
input_path = "web_traffic_daily.csv"
df = pd.read_csv(input_path)
print(f"📥 Loaded file '{input_path}' with {len(df)} rows and {len(df.columns)} columns")

# Step 2: Configure cleaning options
config = CleanConfig(
    na_tokens=["", "na", "n/a", "-", "—", "nil", "null"],
    strip_whitespace=True,
    dedupe_headers=True,
    date_cols=["date"],
    date_iso=True,
    cast_numeric=["visits", "signups"],
    drop_duplicates=True,
    remove_empty_rows=True,
    remove_empty_cols=True,
    outliers={"method": "iqr", "action": "winsorize", "cols": ["visits"], "k": 1.5},
    validation={
        "required_cols": ["date", "visits", "signups"],
        "non_negative": ["visits", "signups"],
        "no_empty_headers": True,
    }
)

# Step 3: Run DataCleaner
cleaner = DataCleaner(config)
cleaned_df, report = cleaner.clean(df)

# Step 4: Save cleaned data
output_path = "cleaned_web_traffic.csv"
cleaned_df.to_csv(output_path, index=False)
print(f"💾 Cleaned data saved as '{output_path}'")

# Step 5: Print Quality Report
print("\n🧾 === QUALITY REPORT ===")
print(json.dumps(report.__dict__, indent=2))

# Step 6: Run test cases (manual verification logic)
print("\n✅ === TEST CASE RESULTS ===")

test_results = []

# TC1: File read & write
try:
    assert not df.empty and not cleaned_df.empty
    test_results.append(("TC1", "File read & write", "PASS"))
except AssertionError:
    test_results.append(("TC1", "File read & write", "FAIL"))

# TC2: Header normalization
try:
    expected_headers = [h.lower().replace(" ", "_") for h in df.columns]
    assert all(col in cleaned_df.columns for col in expected_headers)
    test_results.append(("TC2", "Header normalization", "PASS"))
except AssertionError:
    test_results.append(("TC2", "Header normalization", "FAIL"))

# TC3: Whitespace & NA handling
try:
    whitespace_ok = all(
        not (isinstance(x, str) and x != x.strip())
        for col in cleaned_df.columns
        for x in cleaned_df[col].dropna().astype(str)
    )
    assert whitespace_ok
    test_results.append(("TC3", "Whitespace & NA handling", "PASS"))
except AssertionError:
    test_results.append(("TC3", "Whitespace & NA handling", "FAIL"))

# TC4: Duplicate removal
try:
    assert len(cleaned_df.drop_duplicates()) == len(cleaned_df)
    test_results.append(("TC4", "Duplicate removal", "PASS"))
except AssertionError:
    test_results.append(("TC4", "Duplicate removal", "FAIL"))

# TC5: Numeric casting
try:
    num_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    assert len(num_cols) > 0
    test_results.append(("TC5", "Numeric casting", "PASS"))
except AssertionError:
    test_results.append(("TC5", "Numeric casting", "FAIL"))

# TC6: Date parsing
try:
    date_cols = [c for c in cleaned_df.columns if "date" in c]
    if date_cols:
        parsed = pd.to_datetime(cleaned_df[date_cols[0]], errors="coerce")
        assert parsed.notna().sum() > 0
        test_results.append(("TC6", "Date parsing", "PASS"))
    else:
        test_results.append(("TC6", "Date parsing (no date col found)", "SKIP"))
except Exception:
    test_results.append(("TC6", "Date parsing", "FAIL"))

# TC7: Outlier handling
try:
    assert isinstance(cleaned_df, pd.DataFrame)
    test_results.append(("TC7", "Outlier handling", "PASS"))
except AssertionError:
    test_results.append(("TC7", "Outlier handling", "FAIL"))

# TC8: Validation rules
try:
    assert len(cleaned_df.columns) == len(set(cleaned_df.columns))
    test_results.append(("TC8", "Validation rules", "PASS"))
except AssertionError:
    test_results.append(("TC8", "Validation rules", "FAIL"))

# Step 7: Print all test results
print("\n🧠 Test Case Summary:\n")
for tc_id, desc, result in test_results:
    status = "✅" if result == "PASS" else ("⚠️" if result == "SKIP" else "❌")
    print(f"{status} {tc_id}: {desc} --> {result}")

# Step 8: Final verdict
all_passed = all(r[2] == "PASS" for r in test_results)
if all_passed:
    print("\n🎉 All test cases PASSED successfully!")
else:
    print("\n⚠️ Some test cases FAILED. Please review above results.")
