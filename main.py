# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    time = [0] * n
    for i in range(m):
        min_thread = time.index(min(time))
        output.append(min_thread, time[min_thread])
        time[min_thread] += data[i]
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n = map(int, input().split())
    m = map(int, input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for pairs in range(m):
        print(result[pairs][0], result[pairs][1])


if __name__ == "__main__":
    main()
