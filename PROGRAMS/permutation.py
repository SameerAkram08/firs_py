from itertools import permutations

def generate_permutations(s):
    # return [''.join(p) for p in permutations(s)]


 input_string = input("Enter string as (abc) = "  )
permutations = generate_permutations(input_string)
print(permutations)
