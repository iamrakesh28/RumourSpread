import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import seaborn as sns
from rumour_spread_model import RumourSpreadModel
from callback import (
    OpinionFragmentation,
    Adversary
)

NUM_NODES = 1000
NUM_BITS = 5
NODE_CAPACITY = 100
INIT_NUM_NODES = 15
NUM_EDGES_PER_STEP = 10
TIMESTEPS = 1000

def plot_opinion_fragmentation(bit_counts, title):
    num_bit_strings = len(bit_counts[0])
    num_bits = int(math.log2(num_bit_strings))
    bit_string_list = [None] * num_bit_strings

    for i in range(num_bit_strings):
        bit_string_list[i] = f'{i:0{num_bits}b}'

    bit_count_df = pd.DataFrame(
        data=np.array(bit_counts).T, index=bit_string_list
    )

    sns.heatmap(bit_count_df, cmap='viridis')
    plt.title(title)
    plt.xlabel('Timestep')
    plt.ylabel('Binary String')
    plt.show()

def main():
    while True:
        inp_string = input('Enter: ')

        if inp_string == 'done':
            break
        
        conservation_factor, confidence_factor, adversary_nodes = map(float, inp_string.split())

        rumour_spread = RumourSpreadModel(
            NUM_NODES, NUM_BITS, NODE_CAPACITY,
            conservation_factor, confidence_factor,
            INIT_NUM_NODES, NUM_EDGES_PER_STEP
        )

        _, opinion_freq = rumour_spread.simulate({0: 0}, TIMESTEPS, [
            Adversary(0, int(adversary_nodes), 500),
            OpinionFragmentation(
                NUM_NODES, NUM_BITS, TIMESTEPS
            )]
        )

        plot_opinion_fragmentation(
            opinion_freq, 
            f'K = {conservation_factor}, β = {confidence_factor}'
        )

if __name__ == '__main__':
    main()

