# part 84 from 97

import requests
response = requests.get('https://barnamenevisan.org/')
# response = requests.get('https://githuhhb.com/EnAnsari')

print(response)
# print(response.text)

data = response.text
print(data[0])

# jsonData = response.json()
# print(jsonData[0])
#
# for course in jsonData:
#     print(course['teacher'])

# res = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
res = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId':1})
for data in res.json():
    print(data)
