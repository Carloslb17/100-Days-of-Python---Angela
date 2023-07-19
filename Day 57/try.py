
import requests

name="Katie"

response_gender = requests.get(f"https://gender-api.com/get?name={name}&key=RjKRRD8q5C7v7w75MYVHjAJK9HhPa8FaraQN")
gender_dict = response_gender.json() # This method is convenient when the API returns JSON


response_agify = requests.get(f"https://api.agify.io?name={name}")
agify_dict = response_agify.json() # This method is convenient when the API returns JSON


print(gender_dict['gender'])
print(agify_dict['age'])
