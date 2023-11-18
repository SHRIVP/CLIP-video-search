import os
import json
import requests

dir = "/Users/pushkar/projects/video_search/CLIP-video-search/examples/test_videos/"

file_list = os.listdir(dir)

url = 'http://localhost:3000/insert'

for file in file_list:
    # print(file)
    if file.endswith(".mp4"):
        payload = {"videoURI": dir + file}
        print(payload)
        response = requests.post(url, json=payload)
        print(response.text)
        # # Accessing the request details
        # request_details = response.request
        # print(f"Request Method: {request_details.method}")
        # print(f"Request URL: {request_details.url}")
        # print("Request Headers:")
        # for header, value in request_details.headers.items():
        #     print(f"  {header}: {value}")
        # print("Request Body:")
        # print(request_details.body.decode('utf-8'))
        # break