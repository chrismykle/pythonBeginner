class Student:  # Class is a datatype where you can define your own datatype, here my datatype is Student.

    def __init__(self, name, major, gpa, is_on_probation):  # init defines the attributes,

        self.name = name                                    # in the () there is attributes for the Object Student
        self.major = major                                  # "self" is referring to the Object
        self.gpa = gpa
        self.is_on_probation = is_on_probation
