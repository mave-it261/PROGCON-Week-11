def computeAverage(numbers):
    total = 0
    count = 0
    index = 0
    while True:    #This simulates a Do Loop
        num = numbers[index]
        if num != 0:
            total = total + num
            count = count + 1
        index = index + 1
        if index >= 4: break
    average = float(total) / count
    
    return average

# Main
numbers = [0] * (4)

numbers[0] = int(input())
numbers[1] = int(input())
numbers[2] = int(input())
numbers[3] = int(input())
print(computeAverage(numbers))
