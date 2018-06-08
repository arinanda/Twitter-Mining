import json

#http://jsonviewer.stack.hu

if __name__ == '__main__':
    user_json = '{"user_id": "1", "name": "Marco"}'
    user_data = json.loads(user_json)
    print(user_data['name'])

    user_data['likes'] = ['Python', 'Data Mining']
    user_json = json.dumps(user_data, indent=4)
    print(user_json)