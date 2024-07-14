import numpy as np
import matplotlib.pyplot as plt

def quadratic_model1(time, a1, b1, c1):
    temp1 = a1 * (time**2) + b1 * time + c1
    return temp1

def quadratic_model2(time):
    a2 = 0.1
    b2 = -1
    c2 = 30
    temp2 = a2 * (time**2) + b2 * time + c2
    return temp2

def main():
    time = np.arange(0, 50, 10)
    a1 = float(input('Enter a value: '))
    b1 = float(input('Enter b value: '))
    c1 = float(input('Enter c value: '))
    temp1 = quadratic_model1(time, a1, b1, c1)

    temp2 = quadratic_model2(time)
    plt.plot(time, temp1, label=f'User input coefficients: a={a1}, b={b1}, c={c1}', color='black')
    plt.plot(time, temp2, label='Hard-coded coefficients: a=0.1, b=-1, c=30', color='red')

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation')
    plt.show()

if __name__ == '__main__':
    main()