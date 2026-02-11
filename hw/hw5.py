class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration} min)"

    def __add__(self, other):
        return self.duration + other.duration

    def __eq__(self, other):
        return self.title == other.title and self.duration == other.duration


class Library:
    def __init__(self, movies):
        self.movies = movies

    def __getitem__(self, index):
        return self.movies[index]

    def __len__(self):
        return len(self.movies)

    def __str__(self):
        result = ""
        for i in range(len(self.movies)):
            result += f"{i+1}. {self.movies[i]}\n"
        return result.strip()


class User:
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def __call__(self):
        print(f"User {self.name} is watching movies")

    def __str__(self):
        return f"User: {self.name} | Movies: {len(self.library)}"


m1 = Movie("Matrix", 136)
m2 = Movie("Inception", 148)
m3 = Movie("Interstellar", 169)

library = Library([m1, m2, m3])
user = User("Alex", library)

print(m1)
print(m1 + m2)
print(m1 == m2)
print(library[1])
print(len(library))
print(library)
print(user)
user()
