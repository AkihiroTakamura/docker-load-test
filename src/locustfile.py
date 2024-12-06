from locust import HttpUser, task, constant_pacing

class HelloWorld(HttpUser):
    #  1タスク = 1秒間に1回リクエストを送信する
    wait_time = constant_pacing(1)

    @task
    def helloworld(self):
        with self.client.get(url="/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"statusCode is {response.status_code}")