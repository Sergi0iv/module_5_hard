import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in( self, nickname, password):
        self.nickname = nickname
        self.password = password
        if nickname in self.users and hash(password) in self.users:
            self.current_user = nickname
        else:
            print('Токого пользователя не существует.')
    def register(self, nickname, password, age):
        self.age = age
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.users.append(nickname)

    def log_out(self):
        self.current_user = None
        print('Вы вышли.')

    def add(self, *other):
        self.other = other
        if other not in self.videos:
            self.videos.append(other)

    def get_videos(self, other):
        self.other = other
        list1 = []
        for i in self.videos:
            if other.lower() in i.lower():
                i.append(list1)
            else:
                print('не чего не найдено')
            return i

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт')
            return
        for video in self.videos:
            if title == Video.title:
                if Video.adult_mode and self.current_user.age >= 18:
                    while Video.time_now < Video.duration:
                        Video.time_now += 1
                        print(Video.time_now, end=' ')
                        time.sleep(1)
                    Video.time_now = 0
                    print('Конец видео')






class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class User:

    def __init__(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = password

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')




