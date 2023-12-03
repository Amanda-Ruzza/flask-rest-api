import json
import requests 

# this link gets all the StackOverflow questions about GCP from 2023-07-06 to 2023-07-07
stack_ex_response = requests.get('https://api.stackexchange.com/2.3/questions?page=1&pagesize=10&fromdate=1688601600&todate=1688688000&order=desc&sort=activity&tagged=gcp&site=stackoverflow')

# prints the api response code = 200
print(stack_ex_response)

for question in stack_ex_response.json()['items']:
    if question ['answer_count'] == 0:
        print("This question hasn't been answered yet:")
        print(question['title'],"\n", question['link'], "\n")
    else:
        print("This question is being skipped as it was already answered! \n")