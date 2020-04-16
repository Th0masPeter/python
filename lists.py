"""list used to store a collection of information. it allow us to organize the data.
while creating a list 1st we need to give a descriptive name.here my list name is friends.
and a list is always put inside a square brackets.and we add some values inside a list"""
# we can put strings,numbers, boolean....inside a list.
#           0         1       2   - are the index positions.
#          -3       -2     -1     - is also the -ve index positions.
friends = ["kevin","karen","jim","oscar","toby"]
#index positions are the positions of the element in that list.
# printing actual list.
print(friends)
#inorder to  print a specific element in that list we can write the index position of that element in square brackets.
print(friends[1]) # here karen is printed.
#using -ve index values and printing the elements in the lists
print(friends[-1]) # here the element jim gets printed.
""" if we need to select more than 1 element from a list,
we can use the ":" sign to print more than 1 values present in the list"""
print(friends[1:]) # here from the index value 1 to infinity no:- of elements present in the list will be printed.
# here the values that get printed are from karen(1) to jim(2).
# we can also limit hte value of index position to be printed by entering the specific value as shown below;
print(friends[0:3]) # it starts from index number 0.
#but here the element having index position 3 is not included.i.e;oscar is not included.
#we can also modify elements in a lists.
""" if we want to modify a value in tht string;
    1st access into that value. and then edit the value;
    then we can use the print statement to see the output."""
friends = ["kevin","karen","jim","oscar","toby"]
friends[1] = "mike" # here the element karen is chaged into mike.
print(friends[1]) # her only the element at index position 5 is printed.

