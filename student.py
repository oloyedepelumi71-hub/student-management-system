class Student:
    total_students = 0

    def __init__(self, name, level, score):
        self.name = name
        self._level = level
        self.score = score
        Student.total_students += 1

    def update_score(self, new_score):
        if 0 <= new_score <= 100:
            self.score = new_score

    def check_pass_fail(self):
        if self.score < 40:
            return "failed"
        elif self.score < 70:
            return "pass"
        else:
            return "Excellent"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Score: {self.score}\n"
            f"Grade: {self.grade}"
        )

    @property
    def grade(self):
        if 70 <= self.score <= 100:
            return "A"
        elif 60 <= self.score <= 69:
            return "B"
        elif 50 <= self.score <= 59:
            return "C"
        elif 45 <= self.score <= 49:
            return "E"
        else:
            return "F"

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level < 0:
            new_level = 100
        if new_level > 500:
            new_level = 500
        if 100 <= new_level <= 500:
            self._level = new_level
