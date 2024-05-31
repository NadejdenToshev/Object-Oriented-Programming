class Person:
    def __init__(self, age, name, occupation):
        self.age = age
        self.name = name
        self.occupation = occupation

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}"


# Create an instance of Person
person1 = Person(26, "Joe", "Software Engineer")

# Print the details of the person
print(person1)
