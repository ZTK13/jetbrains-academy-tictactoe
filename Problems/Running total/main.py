input_list = list(input())

input_int_list = [int(n) for n in input_list]

output_list = [sum(input_int_list[: i + 1]) for i in range(len(input_int_list))]

print(output_list)
