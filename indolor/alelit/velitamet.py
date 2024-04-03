from datetime import datetime

# Replace 'past_date' with the date you're interested in
past_date = datetime(2024, 3, 22)  # Format: (year, month, day)
current_date = datetime.now()

# Calculate the difference
time_span = current_date - past_date

print(f"Time elapsed since {past_date.strftime('%Y-%m-%d')}:")
print(f"{time_span.days} days")
