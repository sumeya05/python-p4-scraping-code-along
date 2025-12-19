class Course:
    def __init__(self, title='', schedule='', description=''):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Schedule: {self.schedule}\n"
            f"Description: {self.description}\n"
            "------------------"
        )
