import matplotlib.pyplot as plt
import numpy as np
from google.colab import files

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    try:
        # Upload files to Colab
        uploaded = files.upload()

        # Read coefficients from uploaded files
        for filename in uploaded.keys():
            with open(filename, "r") as file:
                lines = file.readlines()
                if len(lines) % 3 != 0:
                    print(f"Error: Number of lines in {filename} should be a multiple of 3.")
                    continue

                time_values = np.linspace(0, 10, 50)
                plt.figure()
                for i in range(0, len(lines), 3):
                    a = float(lines[i].strip())
                    b = float(lines[i + 1].strip())
                    c = float(lines[i + 2].strip())

                    temperature_hardcoded = quadratic_model(time_values, a, b, c)
                    plt.plot(time_values, temperature_hardcoded, label=f'Set {i//3 + 1}: a={a}, b={b}, c={c}')

                plt.xlabel('Time')
                plt.ylabel('Temperature')
                plt.legend()
                plt.title(f'Weather modeling with quadratic equation (File {filename})')
                plt.show()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()