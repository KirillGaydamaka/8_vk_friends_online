import vk


APP_ID = 7159466


def get_user_login():
    return input('Введите логин: ')


def get_user_password():
    return input('Введите пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    response = api.friends.get(v='5.101', fields='online')
    friends = response['items']
    return ['{} {}'.format(friend['first_name'], friend['last_name'])
            for friend in friends if friend['online'] == 1]


def output_friends_to_console(friends_online):
    print(*friends_online, sep = '\n')


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
