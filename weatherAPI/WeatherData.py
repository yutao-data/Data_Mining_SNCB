import sys
import requests
import csv
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

def fetch_data(api_key, lat, lon, start_timestamp, end_timestamp):
    url = f'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&start={start_timestamp}&end={end_timestamp}&appid={api_key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('list', [])
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OpenWeatherMap API: {e}")
    return []

def generate_data(api_key, lat, lon, start_timestamp, end_timestamp, output_file):
    current_date = datetime.utcfromtimestamp(start_timestamp)
    while current_date <= datetime.utcfromtimestamp(end_timestamp):
        interval_end_date = current_date + timedelta(days=7)
        interval_end_timestamp = int(interval_end_date.timestamp())

        relevant_data_list = fetch_data(api_key, lat, lon, int(current_date.timestamp()), interval_end_timestamp)

        # Write data to the CSV file
        with open(output_file, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for item in relevant_data_list:
                date_timestamp = item.get('dt', '')  # Use the original timestamp
                datetime_utc = datetime.utcfromtimestamp(date_timestamp)
                date = datetime_utc.strftime('%Y-%m-%d %H:%M:%S')
                weather_info = item.get('weather', [{}])[0]
                weather_id = weather_info.get('id', '')
                weather_main = weather_info.get('main', '')
                weather_wind = item.get('wind', {}).get('speed', '')
                weather_clouds = item.get('clouds', {}).get('all', '')
                csv_writer.writerow([
                    date,
                    lat,
                    lon,
                    weather_main,
                    item.get('main', {}).get('temp', ''),
                    item.get('main', {}).get('feels_like', ''),
                    item.get('main', {}).get('pressure', ''),
                    item.get('main', {}).get('humidity', ''),
                    weather_wind,
                    weather_clouds
                ])

        # Move to the next time interval
        current_date = interval_end_date

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py api_keys_file output_dir")
        sys.exit(1)

    # Extract api_keys_file and output_dir from command-line arguments
    api_keys_file = sys.argv[1]
    output_dir = sys.argv[2]

    # Read latitude and longitude data from result.csv
    df = pd.read_csv('position.csv')

    # Read API keys from the provided file
    with open(api_keys_file, 'r') as keys_file:
        api_keys = [key.strip() for key in keys_file.readlines()]

    # Convert date strings to UNIX timestamps
    start_timestamp = int(datetime(2023, 1, 1, 2).timestamp())  # Start from January 1, 2023, 02:00:00
    end_timestamp = int(datetime(2023, 10, 1, 2).timestamp())  # Set the end timestamp to October 1, 2023, 6:00:00

    with ThreadPoolExecutor(max_workers=len(api_keys)) as executor:
        futures = []
        for i, row in df.iterrows():
            lat = row['Rounded_Latitude']
            lon = row['Rounded_Longitude']
            key_index = i % len(api_keys)
            current_api_key = api_keys[key_index]
            output_file = f'{output_dir}/result_{key_index + 1}.csv'
            future = executor.submit(generate_data, current_api_key, lat, lon, start_timestamp, end_timestamp, output_file)
            futures.append(future)

        # Wait for all threads to complete
        for future in futures:
            future.result()

    print('All data generation for all points completed.')
