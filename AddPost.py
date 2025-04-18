from locust import HttpUser, task, between
import random

class AddPostUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/users/sign-in", json={"userId":"topojs15",
                                                 "password":"123"})

    @task
    def add_post(self):
        self.client.post("/posts", json={
            "name":"테스트 게시글" + str(random.randint(1, 100000)),
            "contents":"테스트 컨텐츠"+ str(random.randint(1, 100000)),
            "categoryId":random.randint(1, 10),
            "fileId":random.randint(1, 10),
            "tagDTOList": [
                {"name": "자유게시판1", "url": "127.0.0.1"},
                {"name": "개발블로그", "url": "127.0.0.1"}
            ]
        })