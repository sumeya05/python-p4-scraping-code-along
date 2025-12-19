from bs4 import BeautifulSoup
import requests
from Course import Course

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        """Fetches HTML document from the courses page"""
        doc = BeautifulSoup(
            requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text,
            'html.parser'
        )
        return doc

    def get_courses(self):
        """Returns a list of BeautifulSoup Tag elements containing each course"""
        return self.get_page().select('.post')

    def make_courses(self):
        """Creates Course objects for each course element and stores them in self.courses"""
        for course in self.get_courses():
            title = course.select("h2")[0].text if course.select("h2") else ''
            schedule = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            new_course = Course(title, schedule, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        """Prints all the courses in self.courses"""
        for course in self.make_courses():
            print(course)

# Uncomment to run directly and see output
# if __name__ == "__main__":
#     Scraper().print_courses()
