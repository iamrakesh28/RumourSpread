from rumour_spread_model import RumourSpreadModel
from callback import (
    RangeOfInformationSpread,
    OpinionFragmentation,
    AverageInformationEntropy
)

from plot import (
    plot_range_of_info_spread,
    plot_opinion_fragmentation,
    plot_avg_info_entropy
)

def main():

    num_nodes = 3000
    num_bits = 5
    timesteps = 100
    
    rumour_spread = RumourSpreadModel(num_nodes, num_bits, 100, 1, -3)
    result_list = rumour_spread.simulate(
        {0: 0}, timesteps, 
        [RangeOfInformationSpread(
            num_nodes, num_bits, timesteps
        ),
        OpinionFragmentation(
            num_nodes, num_bits, timesteps
        ),
        AverageInformationEntropy(
            num_nodes, timesteps
        )]
    )

    plot_range_of_info_spread(result_list[0])
    plot_opinion_fragmentation(result_list[1])
    plot_avg_info_entropy(result_list[2])

if __name__ == '__main__':
    main()
