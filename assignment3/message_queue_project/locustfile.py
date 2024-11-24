from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def send_email(self):
        self.client.post("/tasks/send-email/", {
            'recipient': 'test@example.com',
            'subject': 'Test Subject',
            'body': 'Test Body'
        })
