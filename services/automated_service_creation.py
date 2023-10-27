# Uncomment the following line if you are installing the 'requests' package.
import requests

def create_service(service_type, folder_path,service_name,local_boolean,github_boolean,ecr_boolean):
    # Make a POST request to your service
    payload = {
        'service_type': service_type,
        'folder_path': folder_path,
        'service_name': service_name,
        'local_boolean':local_boolean,
        'github_boolean': github_boolean,
        'ecr_boolean': ecr_boolean
    }
    response = requests.post("http://0.0.0.0:8100/create_service", json=payload)
    print("Post Request Create Service")
