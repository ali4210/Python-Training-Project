import requests
import json
import argparse
import logging


def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"Other error occurred: {err}")



def save_data_to_file(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data: {e}")


def parse_arguments():
    parser = argparse.ArgumentParser(description='CLI Data Processor')
    parser.add_argument('--api_url', type=str, required=True, help='API URL to fetch data from')
    parser.add_argument('--file_path', type=str, required=True, help='Path to save JSON data')
    return parser.parse_args()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    args = parse_arguments()
    logging.info("Started fetching data...")
    data = fetch_data(args.api_url)
    if data:
        save_data_to_file(data, args.file_path)


####Run it from the command line
#python "C:\Users\User\PycharmProjects\pythonProject3\Mini_project(Building a CLI Data Processor).py" --api_url "https://jsonplaceholder.typicode.com/posts" --file_path "output.json"






