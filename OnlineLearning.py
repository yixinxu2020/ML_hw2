import numpy as np
import math
import matplotlib.pyplot as plt


def readfile(filename):
    outcomes = []
    with open(filename, 'r') as fp:
        for line in fp:
            outcomes.append(line.strip())
    return outcomes


def Combination(N, m):
    return math.factorial(N) / math.factorial(N - m) / math.factorial(m)


def Betafunction(a,b,x):
    return Combination(a+b, a) * x**(a-1) * (1-x)**(b-1)


def Binomial(m, N, p):
    return Combination(N, m) * p ** m * (1 - p) ** (N - m)


def count(outcome):
    zero = 0
    one = 0
    for i in range(len(outcome)):
        if outcome[i] == '1':
            one += 1
        else:
            zero += 1
    return one, zero


if __name__ == '__main__':
    file_dir = './testfile.txt'
    outcomes = readfile(file_dir)

    prior_a = int(input('prior a is: '))
    prior_b = int(input('prior b is: '))

for i in range(len(outcomes)):
    x = np.arange(0, 1, 0.001)
    # prior function
    y1 = Betafunction(prior_a, prior_b, x)

    posterior_a, posterior_b = count(outcomes[i])
    likelihood = Binomial(posterior_a, posterior_a + posterior_b, posterior_a / (posterior_a + posterior_b))

    # likelihood function
    y2 = Binomial(posterior_a, posterior_a + posterior_b, x)

    posterior_a += prior_a
    posterior_b += prior_b

    # posterior function
    y3 = Betafunction(posterior_a, posterior_b, x)

    print("case", i, ":", outcomes[i])
    print("Likelihood:", likelihood)
    print("Beta prior:\ta =", prior_a, "b =", prior_b)
    print("Beta posterior:\ta =", posterior_a, "b =", posterior_b, "\n")

    prior_a = posterior_a
    prior_b = posterior_b

    plt.plot(x, y1, color='green', label='prior')
    plt.plot(x, y2, color='blue', label='likelihood function')
    plt.plot(x, y3, color='red', label='posterior')
    plt.legend()  # 
    plt.xlabel('μ')
    plt.ylabel('likelihood')
    plt.show()
