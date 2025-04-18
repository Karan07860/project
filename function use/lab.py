unwatched_movies = ("Running Point","Narcos","Power","Suits","Manifest",)
def update_movies(unwatched_movies):
    """add three movies to the tuple:
    -one at the beginning
    -one replacing the middle element
    -one at the end
    """
    movies_list = list(unwatched_movies)
    
    #Add movies
    movies_list.insert(0,"Running Point")
    
    #replace the middle element
    middle_index= len(movies_list) // 2
    movies_list[middle_index] = "Narcos"
    
    #Add movie at the end
    movies_list.append("Power")
    
    #Convert back to tuple
    updated_movies = tuple(movies_list)
    return updated_movies