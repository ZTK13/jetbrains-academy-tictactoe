prime_numbers = [num for num in range(2, 1000)
                 if all(num % factor != 0 for factor in range(2, num))]
