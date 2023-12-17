import sys
import requests
import csv
from datetime import datetime, timedelta
import pandas as pd

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 5:
    print("Usage: python script.py api_key n1 n2 output_file")
    sys.exit(1)

# Extract api_key, n1, n2, and output_file from command-line arguments
api_key = sys.argv[1]
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
output_file = sys.argv[4]

# Define the OpenWeatherMap API endpoint for air pollution data
api_endpoint = 'http://api.openweathermap.org/data/2.5/air_pollution/history'

# Read latitude and longitude data from result.csv, considering only rows from n1 to n2
df = pd.read_csv('position.csv', skiprows=range(1, n1), nrows=(n2 - n1 + 1))

# Write header to the CSV file
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['datetime', 'lat', 'lon', 'aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'])

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    lat = row['Rounded_Latitude']
    lon = row['Rounded_Longitude']
    # Convert date strings to UNIX timestamps
    start_timestamp = int(datetime(2023, 1, 1, 2).timestamp())  # Start from January 1, 2023, 02:00:00
    end_timestamp = int(datetime(2023, 10, 1, 2).timestamp())  # Set the end timestamp to October 1, 2023, 6:00:00
    # Construct the API URL for the current interval
    url = f'{api_endpoint}?lat={lat}&lon={lon}&start={start_timestamp}&end={end_timestamp}&appid={api_key}'

    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the relevant information from the response
        relevant_data_list = data.get('list', [])

        # Append data to the CSV file
        with open(output_file, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for item in relevant_data_list:
                date_timestamp = item.get('dt', '')  # Use the original timestamp
                datetime_utc = datetime.utcfromtimestamp(date_timestamp)
                date = datetime_utc.strftime('%Y-%m-%d %H:%M:%S')

                main_data = item.get('main', {})
                components_data = item.get('components', {})

                csv_writer.writerow([
                    date,
                    lat,
                    lon,
                    main_data.get('aqi', ''),
                    components_data.get('co', ''),
                    components_data.get('no', ''),
                    components_data.get('no2', ''),
                    components_data.get('o3', ''),
                    components_data.get('so2', ''),
                    components_data.get('pm2_5', ''),
                    components_data.get('pm10', ''),
                    components_data.get('nh3', ''),
                ])

    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    # Print a message after generating data for the current point
    print(f'All data for Lat: {lat}, Lon: {lon} generated.')

# Print a final message after generating data for all points
print('All data generation for all points completed.')
