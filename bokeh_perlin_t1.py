import numpy as np
import matplotlib.pyplot as plt

from perlin_noise import PerlinNoise

from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout
from bokeh.models.widgets import Slider

'''
DOCS: 

Perlin Noise: Its a type of random noise but is coherent noise, which means the changes occour gradually
Amplitude: Y axis
Frequency: X axis
Octaves: Noise maps
Lacunarity: Controls the increase in frequency of octaves
Persistance: Controls the decrease in amplitude
Ease Function: f(x) = 6x^5 - 15x^4 + 10x^3
               amt = 6 * 0.3 ^ 5 - 15 * 0.3 ^ 4 + 10 * 0.3 ^ 3
               amt = 0.16 (interpolation amount)
'''
noiseGenerator = PerlinNoise()


def matplot_draw_static(x_cord_list, y_cord_list, title = "Perlin Noise (From Module)"):

    plt.title(title)
    plt.xlabel("Input value")
    plt.ylabel("Perlin noise Value")
    plt.plot(x_cord_list, y_cord_list)
    plt.show()

# def submerge_octave_layers_interpolate(combined_x, combined_y, interpolate_constant = 0.16):
#     '''
#     Interpolate between the y values of each graph. This involves creating a function that smoothly transitions between the y values of each graph.
#     FORMULA: y_combined = (1 - t) * y1 + t * y2   # where t is a parameter between 0 and 1
#     '''
#     y_combined = [(1 - interpolate_constant) * y1_val + interpolate_constant * y2_val for y1_val, y2_val in zip(y1, y2)]
#     x_combined = [(1 - interpolate_constant) * y1_val + interpolate_constant * y2_val for y1_val, y2_val in zip(y1, y2)]
    
def submerge_octave_layers_average(combined_x, combined_y):

    avg_x = [sum(values)/len(combined_x) for values in zip(*combined_x)]
    avg_y = [sum(values)/len(combined_y) for values in zip(*combined_y)]

    return avg_x, avg_y




def perlin_x_y(frequency_x, amplitude_y, step_size = 0.01, x_range = 500):

    '''
    i is the variable that iterates over the range of values from 0 to 499 (500 values in total). 
    It represents the input values for which you want to generate Perlin noise.
    
    0.01 is the step size or the increment applied to each value of i. In this case, it's used to create a list of x values ranging from 0.00 to 4.99 
    with a step size of 0.01. 
    The purpose of this step size depends on the context of your noise generation. It determines how closely spaced the sampled points are along the x-axis.

    The x list is then used to generate corresponding y values using the noiseGenerator function, likely a Perlin noise generator function. 
    The 0.01 step size is chosen based on the desired resolution or granularity of the noise along the x-axis. 
    Adjusting this value will affect the frequency of the generated noise pattern.
    '''

    x = [x_val * step_size * frequency_x for x_val in range(x_range)]
    y = [noiseGenerator(y_val) * amplitude_y for y_val in x]

    return x, y


def create_noise_map(octaves = 3, persistence = 0.5, lacunarity = 2):
    
    x_cord_list = []
    y_cord_list = []

    for octave_layer in range(0, octaves):

        frequency_x = lacunarity ** octave_layer
        amplitude_y = persistence ** octave_layer

        x_cord, y_cord = perlin_x_y(frequency_x, amplitude_y, step_size = 0.01, x_range = 300)

        x_cord_list.append(x_cord)
        y_cord_list.append(y_cord)

        # matplot_draw_static(x_cord, y_cord, title = "Perlin Noise (From Module)")



    avg_x, avg_y = submerge_octave_layers_average(x_cord_list, y_cord_list)
    
    matplot_draw_static(avg_x, avg_y, title = "Perlin Noise (From Module)")

print(create_noise_map(octaves = 3))



