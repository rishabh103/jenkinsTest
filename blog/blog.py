from post import Post


class Blog:
    def __init__(self,title,author) -> None:
        self.title = title
        self.author = author
        self.posts = []
    
    def __repr__(self) -> str:
        return f'{self.title} is written by {self.author}'

    def create_post(self,title,content):
        p = Post(title,content)
        self.posts.append(p)
    
    def json(self):
        return {
            'title':self.title,
            'author':self.author,
            'posts':self.posts
        }


        


