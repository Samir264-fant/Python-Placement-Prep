#calculating the average of 4 students marks using function
def average(a, b, c, d):
    sum = a + b + c + d
    avg = sum/4
    print(f"The average marks of the students is: {avg}")
    return avg

average(80, 90, 70, 60)