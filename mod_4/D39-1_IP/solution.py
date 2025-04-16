"""
Написать класс Twitter, в котором есть следующие методы:

    __init__(self), который инициализирует класс
    post_tweet(self, user_id, tweet_id), который создает новый
твит с идентификатором tweet_Id по идентификатору пользователя
user_id. Каждый вызов этой функции будет осуществляться с
уникальным идентификатором твита. Желательно, чтобы впоследствии
твиты можно было бы быстро получить по user_id.
    get_news_feed(self, user_id), который получает 10 последних
идентификаторов твитов в ленте новостей пользователя. Каждый
элемент в ленте новостей должен быть опубликован пользователями,
на которых подписан пользователь. Твиты должны быть упорядочены
от самого позднего до самого раннего. Подумайте, как организовать
упорядочивание твитов по времени:
возможно для этого лучше записывать в структуру данных
с твитами информацию о твите (то есть tweet_id) какое то число,
отвечающее за время (например какой нибудь счетчик)
и это например завернуть в кортеж
    follow(self, follower_id, followee_id), в котором пользователь
с идентификатором follower_id подписался на пользователя с
идентификатором followee_id. Желательно, чтобы впоследствии
подписки можно было бы быстро получить по follower_id.
    unfollow(self, follower_id, followee_id), в котором пользователь
с идентификатором follower_id отписался от пользователя с
идентификатором followee_id.


Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from typing import List

class Twitter:

   def __init__(self):
       # YOUR CODE HERE

   def post_tweet(self, user_id, tweet_id):
       # YOUR CODE HERE

   def get_news_feed(self, user_id) -> List[int]:
       # YOUR CODE HERE

   def follow(self, follower_id, followee_id):
       # YOUR CODE HERE

   def unfollow(self, follower_id, followee_id):
       # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

Пример 1
    Входные данные
        twitter = Twitter()
        twitter.follow(1, 2)
        twitter.follow(1, 3)
        twitter.post_tweet(2, 4)
        twitter.post_tweet(2, 6)
        twitter.post_tweet(3, 2)
        twitter.post_tweet(3, 7)
        twitter.post_tweet(3, 3)
        twitter.post_tweet(3, 8)
        twitter.post_tweet(2, 1)
        twitter.post_tweet(2, 9)
        twitter.follow(1, 4)
        twitter.post_tweet(4, 5)
        twitter.post_tweet(4, 10)
        twitter.unfollow(1, 2)
        twitter.post_tweet(5, 11)
        twitter.post_tweet(5, 12)
        twitter.post_tweet(5, 13)
        twitter.post_tweet(6, 14)
        twitter.follow(1, 5)
        twitter.post_tweet(7, 15)
        twitter.post_tweet(7, 16)
        twitter.post_tweet(7, 17)
        twitter.post_tweet(7, 18)
        twitter.follow(1, 7)
        print(twitter.get_news_feed(1))
    Выходные данные
        [18, 17, 16, 15, 13, 12, 11, 10, 5, 8]

"""


from typing import List

class Twitter:
    def __init__(self):
        # создаем словари
        self.user_tweet = dict()
        self.user_follow = dict()
        self.pos = 0

    def post_tweet(self, user_id, tweet_id):
        self.pos += 1 # устанавливаем счетчик на  tweet
        # проверяем наличие user_id в словаре
        if not self.user_tweet.get(user_id):
            self.user_tweet[user_id] = []
        # вносим  tweet
        self.user_tweet[user_id].append((self.pos, tweet_id))

    def get_news_feed(self, user_id) -> List[int]:
        r = list()  # создаем пустой список tweet
        # проверяем наличие follow
        for id_user in self.user_follow[user_id]:
            # добавляем при наличие tweet в сисок tweet
            if self.user_tweet.get(id_user):
                r = r + self.user_tweet[id_user]
        # добавляем при наличие tweet пользоваиля в сисок
        if self.user_tweet.get(user_id):
            r = r + self.user_tweet[user_id]
        # сортируем сисок tweet и выводим только tweet
        rang = sorted(r, key=lambda item: item[0], reverse=True)
        return [x[1] for x in rang[:10]]

    def follow(self, follower_id, followee_id):
        # проверяем наличия пользоваиля в сиске user_follow
        if not self.user_follow.get(follower_id):
            self.user_follow[follower_id] = []
        # добавляем followee_id к ключу follower_id в сиске
        # в сисок user_follo
        self.user_follow[follower_id].append(followee_id)

    def unfollow(self, follower_id, followee_id):
        if self.user_follow.get(follower_id):
            follows = list(self.user_follow[follower_id])
            if followee_id in follows:
                follows.remove(followee_id)
                self.user_follow[follower_id] = follows

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

twitter = Twitter()
twitter.follow(1, 2)
twitter.follow(1, 3)
twitter.post_tweet(2, 4)
twitter.post_tweet(2, 6)
twitter.post_tweet(3, 2)
twitter.post_tweet(3, 7)
twitter.post_tweet(3, 3)
twitter.post_tweet(3, 8)
twitter.post_tweet(2, 1)
twitter.post_tweet(2, 9)
twitter.follow(1, 4)
twitter.post_tweet(4, 5)
twitter.post_tweet(4, 10)
twitter.unfollow(1, 2)
twitter.post_tweet(5, 11)
twitter.unfollow(1, 2)

twitter.post_tweet(5, 12)
twitter.post_tweet(5, 13)
twitter.post_tweet(6, 14)
twitter.follow(1, 5)
twitter.post_tweet(7, 15)
twitter.post_tweet(7, 16)
twitter.post_tweet(7, 17)
twitter.post_tweet(7, 18)
twitter.follow(1, 7)

print(twitter.get_news_feed(1))
