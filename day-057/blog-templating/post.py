import requests


class Post:
    def __init__(self):
        response = requests.get(
            "https://api.npoint.io/c790b4d5cab58020d391")
        self.all_posts = response.json()

    def fetch_post(self, post_id):
        for post in self.all_posts:
            if post["id"] == post_id:
                return post
        return None
