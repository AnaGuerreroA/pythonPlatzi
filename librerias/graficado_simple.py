from bokeh.plotting import figure, output_file, show
import random

if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = 20 #valores a graficar
    x_vals = list(range(total_vals))

    y_vals = []

    for i in x_vals: 
        val = random.randint(0,100)#pregunta valor Y
        print(val)
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)