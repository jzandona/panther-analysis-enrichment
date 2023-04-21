import os
import requests
import json

def query_1password_api(api_token, base_url):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    
    # Get the list of vaults
    vaults_url = f'{base_url}/v1/vaults'
    vaults_response = requests.get(vaults_url, headers=headers)
    vaults = vaults_response.json()
    
    # Get all items from each vault
    all_items = []
    for vault in vaults:
        vault_id = vault['id']
        items_url = f'{base_url}/v1/vaults/{vault_id}/items'
        items_response = requests.get(items_url, headers=headers)
        items = items_response.json()
        all_items.extend(items)
    
    # Save the results to a JSON file
    with open('1password_items.json', 'w') as json_file:
        json.dump(all_items, json_file, indent=4)

if __name__ == '__main__':
    # Retrieve the 1Password API token and base URL from environment variables
    api_token = os.environ['ONEPASSWORD_API_TOKEN']
    base_url = os.environ['ONEPASSWORD_API_BASE_URL']
    query_1password_api(api_token, base_url)
