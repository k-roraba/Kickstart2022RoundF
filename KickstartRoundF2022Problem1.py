#CodeJam 2022 Round F Problem 1 - Sort the Fabric

cases = int(input())
output = []

class fabric:
    def __init__(self, c, d, u):
        self.c = c
        self.d = d
        self.u = u 
        self.AdaPos = 0   

for x in range(cases):
    n = int(input())

    unsorted = []
    
    #get input
    for i in range(n):
        [c, d, u] = input().split()
        newFab = fabric(c, int(d), int(u))
        unsorted.append(newFab)

    #sort by Ada (bubblesort)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if unsorted[j].c > unsorted[j+1].c:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            if unsorted[j].c == unsorted[j+1].c:
                if unsorted[j].u > unsorted[j+1].u:
                    unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    #give trackers
    for i in range(n):
        unsorted[i].AdaPos = i
    
    #sort by Charles (bubblesort)
    for i in range(n - 1):
        for j in range(0, n - j - 1):
            if unsorted[j].d > unsorted[j+1].d:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            if unsorted[j].d == unsorted[j+1].d:
                if unsorted[j].u > unsorted[j+1].u:
                    unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
    
    count = 0
    # count matches
    for i in range(n):
        if unsorted[i].AdaPos == i:
            count += 1
    
    string = "Case #" + str(x+1) + ": " + str(count)
    output.append(string)

for x in range(cases):
    print(output[x])