import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    try:
        # Read coefficients from a file (assuming a file named "coefficients.txt")
        with open("coefficients.txt", "r") as file:
            coefficients = file.read().split()
            a = float(coefficients[0])
            b = float(coefficients[1])
            c = float(coefficients[2])

        time_values = np.linspace(0, 10, 50)
        temperature_hardcoded = quadratic_model(time_values, a, b, c)

        # Plot with file-defined coefficient values in the legend
        plt.plot(time_values, temperature_hardcoded, label=f'File-defined coefficients: a={a}, b={b}, c={c}')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.legend()
        plt.title('Weather modeling with quadratic equation (File-defined coefficients)')
        plt.show()

    except FileNotFoundError:
        print("Error: 'coefficients.txt' file not found. Please create it with the coefficients on separate lines.")
    except IndexError:
        print("Error: 'coefficients.txt' file does not contain enough coefficients. Please ensure it has three lines with the coefficients.")

if __name__ == "__main__":
    main()