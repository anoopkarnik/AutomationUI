# Uncomment the following line if you are installing the 'requests' package.
import requests

def create_service(url,service_details,service_type, folder_path,service_name,service_port,local_boolean,github_boolean,ecr_boolean):
    # Make a POST request to your service
    payload = {
        'service_type': service_type,
        'folder_path': folder_path,
        'service_name': service_name,
        'service_port': service_port,
        'local_boolean':local_boolean,
        'github_boolean': github_boolean,
        'ecr_boolean': ecr_boolean
    }
    request_url = f"{url}:{service_details['port_no']}/create_service"
    response = requests.post(request_url, json=payload)
    print("Post Request Create Service")


def delete_service(url,service_details,service_type, folder_path,service_name,local_boolean,github_boolean,ecr_boolean,container_boolean,image_boolean):
    # Make a POST request to your service
    payload = {
        'service_type': service_type,
        'folder_path': folder_path,
        'service_name': service_name,
        'local_boolean':local_boolean,
        'github_boolean': github_boolean,
        'ecr_boolean': ecr_boolean,
        'container_boolean': container_boolean,
        'image_boolean': image_boolean
    }
    request_url = f"{url}:{service_details['port_no']}/delete_service"
    response = requests.post(request_url, json=payload)
    print("Post Request Create Service")
