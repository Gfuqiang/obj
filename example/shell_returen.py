import os, requests

if __name__ == '__main__':
    private_token = 'hxqD8busfSssXbTZLCrB'
    headers = {'Private-Token': private_token}
    url = f'http://39.97.247.230:8251/api/v4/projects?order_by=id&sort=asc&per_page=35'
    # url = f'http://39.97.247.230:8251/api/v4/users/1/projects'
    res = requests.get(url, headers=headers)

    url1 = f'http://39.97.247.230:8251/api/v4/projects/2/repository/tags'
    res1 = requests.get(url1, headers=headers)
    print(res1.text)
    for tag in res1.json()[:10]:
        print(tag['name'])


    # print(res.text)
    print(res.json())
    # for project in res.json():
    #     if project['name'] == 'reef':
    #         print(project['tag_list'])

    # tag
    url = f'https://gitlab.example.com/api/v4/projects/5/protected_tags'