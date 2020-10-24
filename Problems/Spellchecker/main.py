dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

s = input()

incorrect_words = [w for w in s.split() if w not in dictionary]

if len(incorrect_words) == 0:
    print("OK")
else:
    print("\n".join(incorrect_words))
