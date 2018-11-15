# function to return count of possible paths
# to reach cell at row number m and column 
# number n from the topmost leftmost 
# cell (cell at 1, 1) 
def numberOfPaths(m, n):
    # If either given row number is first
    # or given column number is first
    if (m == 1 or n == 1):
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)


# Driver program to test above function
m = 3
n = 3
print(numberOfPaths(m, n))


# Second approach
def numberOfPaths(m, n):
    # Create a 2D table to store
    # results of subproblems
    count = [[0 for x in range(m)] for y in range(n)]

    # Count of paths to reach any
    # cell in first column is 1
    for i in range(m):
        count[i][0] = 1;

        # Count of paths to reach any
    # cell in first column is 1
    for j in range(n):
        count[0][j] = 1;

        # Calculate count of paths for other
    # cells in bottom-up
    # manner using the recursive solution
    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m - 1][n - 1]


# Driver program to test above function
m = 3
n = 3
print(numberOfPaths(m, n))
