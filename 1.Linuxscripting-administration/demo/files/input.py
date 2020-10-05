import json

with open('input.json', 'r') as input:
    obj = json.load(input)
    print('hello, ' + obj['name'])
    with open('output.txt', 'w') as output:
        output.write(obj['name'] + "'s Hobbies are as below: \n\t")
        for hobby in obj['hobbies']:
            output.write(hobby + "\n\t")
