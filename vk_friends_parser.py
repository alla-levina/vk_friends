import requests
import tqdm
import argparse

ID = '3607717'
TOKEN = ''


def get_friends(id):
    try:
        return set(
            requests.get('https://api.vk.com/method/friends.get?user_id=' + id + '&access_token=' + TOKEN).json()[
                'response'])
    except:
        return set()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parser for downloading a network user's friends from the VK")
    parser.add_argument("id", help="User id")
    parser.add_argument("token", help="Access token from VK app")
    parser.add_argument("--file", default='vk_friends.csv', help="File to save the edges of the graph")
    (args) = parser.parse_args()

    ID = args.id
    token = args.token
    file_name = args.file

    friends = get_friends(ID)

    with open(file_name,'w') as file:
        file.write('source, target' + '\n')
        for friend in tqdm.tqdm(friends):
            for f in (get_friends(friend) - set([id])) & friends:
                file.write(str(friend), ',', str(f))


