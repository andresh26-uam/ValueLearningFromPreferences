import numpy as np
import torch



def get_color_gradient(c1, c2, mix):
    """
    Given two hex colors, returns a color gradient corresponding to a given [0,1] value
    """
    c1_rgb = np.array(c1)
    c2_rgb = np.array(c2)
    mix = torch.softmax(torch.tensor(np.array(mix)),dim=0).detach().numpy()
    return (mix[0]*c1_rgb + ((1-mix[0])*c2_rgb))



def pad(array, length):
    new_arr = np.zeros((length,))
    new_arr[0:len(array)] = np.asarray(array)
    if len(new_arr) > len(array):
        new_arr[len(array):] = array[-1]
    return new_arr
