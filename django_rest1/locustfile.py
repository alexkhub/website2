from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Время ожидания между запросами (от 1 до 3 секунд)

    @task
    def my_task(self):
        self.client.get("/product_category/monitory/")

    @task
    def my_task2(self):
        self.client.get("/product_category/smartfony/")




