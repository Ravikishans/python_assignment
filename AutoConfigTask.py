import json
import flask
from flask import Flask, jsonify
import os

app = Flask(__name__)

fpath = "config.ini"

def read_config(file_path):
    config_data = {}  # Initialize an empty dictionary to store config data
    current_section = None  # Variable to keep track of the current section
    
    try:
        with open(file_path, mode='r') as file:
            lines=file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    current_section = line[1:-1]  # Extract section name without '[' and ']'
                    config_data[current_section] = {}  # Initialize a nested dictionary for the section
                elif '=' in line and current_section:
                    key, value = line.split('=')
                    config_data[current_section][key.strip()] = value.strip()  # Add key-value pair to nested dictionary
                # else:
                #     print(f"Ignoring line: {line}")  # Print a message for invalid lines
            return config_data    
    except FileNotFoundError:
        # print('The file was not found')
        return None
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None
    # return config_data  # Return the dictionary containing config data

# config_dict = read_config(fpath)

def save_to_database(data):
    try:
        with open('output.json', "w") as outfile:
            json.dump(data, outfile)
    except Exception as e:
        print(f"Error saving data ro database: {e}")

@app.route('/get_config', methods=['GET'])
def get_config():
    config_data = read_config('config.ini')
    if config_data:
        save_to_database(config_data)
        return jsonify(config_data)
    else:
        return "Error: Configuration file not found or could not be read."

if __name__ == '__main__':
    app.run(debug=True)            