

class UrTube:
    users = []
    videos = []
    current_user = False
    def log_in( self, nickname, password):
        self.nickname = nickname
        self.password = password
        if nickname in UrTube.users and hash(password) in UrTube.users:
            self.current_user = True
        else:
            print('Токого пользователя не существует.')
    def register(self, nickname, password, age):
        self.age = age
        if nickname in UrTube.users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            UrTube.users.append(nickname)

    def log_out(self):
        print('Вы вышли.')

    def __add__(self, *other):
        self.other = other
        if other not in UrTube.videos:
            other += UrTube.videos
    def get_videos(self):
        pass


class Video:
    pass


class User:

    def __init__(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = password

# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')




