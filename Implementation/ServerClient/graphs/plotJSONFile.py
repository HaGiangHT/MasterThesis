import matplotlib.pyplot as plt

# Manually define data
data = {
    'person':       [0.1,   0.1,   0.1,   0.1,  0.1,   0.125,  0.125,   0.1, 0.1    , 0.125,],
    'bicycle':      [0.225, 0.225, 0.225, 0.225,0.225, 0.175,  0.225,   0.25, 0.2   , 0.25,],
    'car':          [0.1,   0.1,   0.1,   0.1,  0.1,   0.15,   0.175,   0.175, 0.175, 0.175,],
    'motorcycle':   [0.225, 0.225, 0.225, 0.225,0.225, 0.225,  0.2,     0.2, 0.25   , 0.225,  ],
    'bus':          [0.225, 0.225, 0.225, 0.225,0.225, 0.2,    0.15,    0.2, 0.2    , 0.15, ],
    'truck':        [0.125, 0.125, 0.125, 0.125,0.125, 0.125,  0.125,   0.075, 0.075, 0.075,]
}

def plot_graph(data):
    iterations = range(1, len(next(iter(data.values()))) + 1)  # assuming all keys have the same number of iterations

    for key, values in data.items():
        plt.plot(iterations, values, marker='o', label=key)

    #plt.title('Value Changes Over Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('Values')
    plt.xticks(iterations)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, fancybox=True, shadow=True)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../graphs/NoneF_Json.png')

def main():
    plot_graph(data)

if __name__ == "__main__":
    main()
