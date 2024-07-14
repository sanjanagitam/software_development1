import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    from google.colab import files

    # Upload files to Colab
    uploaded = files.upload()

    # Read coefficients from uploaded files
    for filename in uploaded.keys():
        with open(filename, "r") as file:
            lines = file.readlines()

            # Check if the file contains at least 3 lines
            if len(lines) < 3:
                print(f"Error: Insufficient lines in {filename}. Expected 3 lines.")
                continue

            try:
                a = float(lines[0].strip())
                b = float(lines[1].strip())
                c = float(lines[2].strip())
            except ValueError:
                print(f"Error: Unable to convert lines in {filename} to floats.")
                continue

            time_values = np.linspace(0, 10, 50)
            temperature_hardcoded = quadratic_model(time_values, a, b, c)

            plt.figure()
            plt.plot(time_values, temperature_hardcoded, label=f'a={a}, b={b}, c={c}')
            plt.xlabel('Time')
            plt.ylabel('Temperature')
            plt.legend()
            plt.title(f'Weather modeling with quadratic equation (File {filename} coefficients)')
            plt.show()

if __name__ == "__main__":
    main()