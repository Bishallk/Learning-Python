
#- wap to ask user to input 3 movies name and store it into list
# fav_movies=[]

# movie1=input("enter movie1 name :")
# movie2=input("enter movie2 name :")
# movie3=input("enter movie3 name :")
# fav_movies.append(movie1)
# fav_movies.append(movie2)
# fav_movies.append(movie3)
# print(fav_movies)
# print(type(fav_movies))
#------------------------------------------------------------------

#-WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list=[1,2,3,2,1,4]

copy=list.copy()
copy.reverse()

if(list==copy):
    print(" is palindrome")
else:
    print("not palindrome")
