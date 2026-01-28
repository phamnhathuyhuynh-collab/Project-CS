def square_root_bisection(square_target, tolerance=1e-7, max_iterations = 100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        root = None
        low = 0
        high = max(1, square_target)
        for _ in range(max_iterations):
            mid = (low + high ) / 2
            square_mid = mid**2
            if abs(square_mid- square_target) < tolerance:
                root = mid
                break
            elif(square_mid > square_target):
                high = mid 
            else:
                low = mid
        if root == None:
            print(f"Failed to converge within {max_iterations} iterations.")
        else:
            print(f'The square root of {square_target} is approximately {root}')
    return root
