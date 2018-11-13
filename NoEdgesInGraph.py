# Function to find the total
# number of edges in a complete
# graph with N vertices

def totalEdge(n):
    result = (n * (n - 1)) // 2
    return result


# Driver code
if __name__ == '__main__':
    n = 5
    print("Total number of Edges: ", totalEdge(n))
