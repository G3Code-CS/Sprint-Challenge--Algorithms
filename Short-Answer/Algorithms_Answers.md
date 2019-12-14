#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) At the first look, there is one while loop. This while loop is based on the condition of n*n*n and
n\*n is getting added in the inside. However, the whole loop is based on the value of n. With one while loop
which is based on the value of n, the run time complexity will be O(n).

b) This code snippet has two loops and they are nested - one for loop with a while loop within O(n^2). However, on closer
examination we find that, the value of j within for-loop is always 1 and j is always going to be less than n. Even
if the while loop was not present, the code snipped could have been implemented and this looping will be a O(log n). In summary,
the outer loop is O(n) and inner loop is O(log n). Therefore, the runtime complexity is O(n log n).

c) The catch in this function is this is a recursive function. The return is a constant time. This function is recursive till
bunnies gets to 0 (where bunnies is n). Hence the run time complexity of this function is O(n)

## Exercise II

### Algorithm for devising the least broken eggs:

From the problem statement: "Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f."

This is a perfect problem to be solved using binary search. We have to find that floor from when on wards the egg will start breaking.

Note: For binary search the main criteria is the list that we are searching has to be sorted. The building in this cases is like a sorted array list.

Following will be the steps I will device to find the floor when the egg starts to break:

1. Find the middle floor and drop the egg.
   ---> If the egg breaks then we need to move to the lower list of floors else we will need to move to higher list of floors.
   Assuming the egg breaks:

2. From the lower list of floors, we will find the middle floor and drop the egg.
   ---> If the egg breaks then we need to move to the lower list of floors else we will need to move to higher list of floors.
   Assuming the egg breaks:

As you can see we find a pattern for recursion here. We will recursively use this strategy to find the exact floor where the egg will break.

3. Finally, we will come to a point where we might have just only two floors or one floor. At that point, if there is only one floor we will
   return the floor or if there are two floors we can check in which floor the egg breaks and return that floor value.

## A simple pseudo code to understand the logic

eggbreak( floor_list)
if number of floors length is 0
return 0
if number of floor length is 1
return that floor
if number of floor length is 2
find which floor the egg breaks and return that floor
floor_list/2
if egg breaks
return eggbreak(bottom floor list)
else
return eggbreak(top floor list)

As we can see we do not iterate through the entire array / set of floors to find which floor. Rather we work
on a subset of the floors narrowing the possibility. Hence the run time complexity will be O(log n)
