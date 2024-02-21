def negative_and_positive(sequence):
    negative_sum = 0
    positive_sum = 0

    while sequence:
        number = sequence.pop()
        if number < 0:
            negative_sum += number
        else:
            positive_sum += number

    print(f'{negative_sum}\n{positive_sum}')

    if abs(negative_sum) > positive_sum:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"

sequence = [int(x) for x in input().split()]

print(negative_and_positive(sequence))
