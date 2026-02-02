#1
movie_list = [ "the resident evil", "the matrix", "the lord of the rings", "the godfather", "the dark knight" ]
movie_list.insert(2, "the avengers")
movie_list.insert(4, "the inception")
print(movie_list)

movie_list.remove("the resident evil")
print(movie_list)

movie_list.sort()
print(movie_list)

movie_list[3]= "the terminator"
print(movie_list)

#2
set1 = {1,2,3,4,5}
set2 = {2,4,6,8,10}

set_union = set1.union(set2)
print("union is:", set_union )

set_intersection = set1.intersection(set2)
print("Intersection is:", set_intersection)

set_difference = set1.difference(set2)
print("Difference is:", set_difference)

set1.add(6)
print("After adding new element:" ,set1)
set2.add(12)
print("After adding new element:", set2)

#3
courses_tuple = ("math", ("algebra", "Geometry"), "science")
print("Accesing element:",courses_tuple[0])
print("Accesing sub element:",courses_tuple[1][1])
new_courses = ("chemistry", "physics")
all_courses = courses_tuple + new_courses
print("After concatinating:", all_courses)

#4
my_dict = {
    "Name": "VIDIT KOTHARI",
    "Age": 19,
    "City": "pune"
    }

my_dict["Country"] = "india"
print( "Adding new element:",my_dict)

my_dict["Age"] = 19
print( "Updating element:", my_dict)

removed = my_dict.pop("City", None)
print("After removal:", my_dict)


new_dict = {
    "hobby": "basketball"
}
my_dict.update(new_dict)
print("Merging both dictionary :", my_dict)