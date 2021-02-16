class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
    def get_graduated_students(self):
        # Find the students in the school who have successfully graduated.
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
        return passed_students
    def print_graduated_students(self, passed_students):
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')
    def send_congrats(self, passed_students):
        for s in passed_students:
            s.send_congrat_email()
    def find_top_students(self, passed_students):
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)
    def process_graduation(self):
        passed_students = self.get_graduated_students()

        self.print_graduated_students(passed_students)
        self.send_congrats(passed_students)
        self.find_top_students(passed_students)

students = [Student(2.1, 'Pinocchio'), Student(2.3, 'goku'), Student(2.7, 'toro'), 
            Student(3.9, 'naruto'), Student(3.2,'kami'), Student(3,'guts')]
school  = School(students)
school.process_graduation()