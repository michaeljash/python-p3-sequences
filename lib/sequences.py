def print_fibonacci(n):
    fibonacci_sequence = [0, 1]
    
    if n <= 0:
        print([])
        return
    

    if n == 1:
        print([0])
        return
    
    while len(fibonacci_sequence) < n:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    
    print(fibonacci_sequence[:n])

print_fibonacci(9)
