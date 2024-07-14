import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    # Define your coefficients
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    time_values = np.linspace(0, 20, 50)
    temperature_user_defined = quadratic_model(time_values, a, b, c)

    # Plot with user-defined coefficient values in the legend
    plt.plot(time_values, temperature_user_defined, label=f'User-defined coefficients: a={a}, b={b}, c={c}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather modeling with quadratic equation (User-defined coefficients)')
    plt.show()

if __name__ == "__main__":
    main()
