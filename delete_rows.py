import smartsheet
from datetime import datetime, timezone

# Initialize the Smartsheet client with your API token
api_token = '**API_TOKEN**'
sheet_id = 1540875498770308  # Replace with your sheet ID

smartsheet_client = smartsheet.Smartsheet(api_token)

# Define the target date as a timezone-aware datetime
target_date = datetime(2024, 8, 20, tzinfo=timezone.utc)

# Get the sheet
sheet = smartsheet_client.Sheets.get_sheet(sheet_id)

# Function to delete rows in smaller batches
def delete_rows_in_batches(rows_to_delete, batch_size=100):
    for i in range(0, len(rows_to_delete), batch_size):
        batch = rows_to_delete[i:i + batch_size]
        row_ids = [row.id for row in batch]
        smartsheet_client.Sheets.delete_rows(sheet_id, row_ids)
        print(f"Deleted {len(batch)} rows.")

rows_to_delete = []

# Iterate through rows to find those that match the criteria
for row in sheet.rows:
    if row.created_at >= target_date:
        rows_to_delete.append(row)

# Delete the rows in batches
if rows_to_delete:
    delete_rows_in_batches(rows_to_delete)
    print(f"Total rows deleted: {len(rows_to_delete)}")
else:
    print("No rows found to delete.")
