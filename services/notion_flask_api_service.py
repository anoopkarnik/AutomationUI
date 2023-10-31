# Uncomment the following line if you are installing the 'requests' package.
import requests

def update_books(url,service_details):
    # Make a POST request to your service
    request_url = f"{url}:{service_details['port_no']}/update_books"
    response = requests.post(request_url)
    print("Books Update")


def update_movies_tvshows(url,service_details):
    # Make a POST request to your service\
    print(service_details)
    request_url = f"{url}:{service_details['port_no']}/update_movies_tvshows"
    response = requests.post(request_url)
    print("Movies Tv Shows Updated")

def update_dashboard_status(url,service_details):
    # Make a POST request to your service
    request_url = f"{url}:{service_details['port_no']}/update_dashboard_status"
    response = requests.post(request_url)
    print("Update Dashboard Status Updates") 

def add_to_calendar(url,service_details):
    # Make a POST request to your service
    request_url = f"{url}:{service_details['port_no']}/add_to_calendar"
    response = requests.post(request_url)
    print("Added to Calendar")

