#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) At the first look, there is one while loop. This while loop is based on the condition of n*n*n and
n\*n is getting added in the inside. However, the whole loop is based on the value of n. With one while loop
which is based on the value of n, the run time complexity will be O(n).

b) This code snippet has two loops and they are nested - one for loop with a while loop within O(n^2). However, on closer
examination we find that, the value of j within for-loop is always 1 and j is always going to be less than n. Even
if the while loop was not present, the code snipped could have been implemented and this looping will be a O(log n). In summary,
the outer loop is O(n) and inner loop is O(log n). Therefore, the runtime complexity is O(n log n).

c)

## Exercise II
