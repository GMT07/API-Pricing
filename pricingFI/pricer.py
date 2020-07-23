# coding: utf-8
# Librairies
from utils import utils


#####################################################################################################################

# Price of vanillas options
def MonteCarloOneUnderlying(optionType, strike, maturity, spot, volatility, interestRate, numberOfPaths):
    mean = utils.PricingMonteCarlo(optionType, strike, maturity, spot, volatility, interestRate, numberOfPaths)
    return mean


# Simulation by Monte Carlo of delta
def DeltaOptionVanilla(optionType, strike, maturity, spot, volatility, interestRate, numberOfPaths):
    mean = utils.DeltaOption(optionType, strike, maturity, spot, volatility, interestRate, numberOfPaths)
    return mean


#####################################################################################################################

# Simulation of double digital price
def MonteCarloDoubleDigital(optionType, low, up, maturity, spot, volatility, interestRate, numberOfPaths):
    mean = utils.PricingDoubleDigital(optionType, low, up, maturity, spot, volatility, interestRate, numberOfPaths)
    return mean


# Simulation by Monte Carlo of delta
def DeltaOptionDoubleDigital(optionType, low, up, maturity, spot, volatility, interestRate, numberOfPaths):
    mean = utils.DeltaDoubleDigital(optionType, low, up, maturity, spot, volatility, interestRate, numberOfPaths)

    return mean


#####################################################################################################################

# Price of Asianoptions
def MonteCarloAsianOptions(optionType, strike, maturity, spot, volatility, interestRate, numberOfSteps, numberOfPaths):
    mean = utils.PricingMonteCarloAsiatiques(optionType, strike, maturity, spot, volatility, interestRate,
                                             numberOfSteps, numberOfPaths)
    return mean


# Simulation by Monte Carlo of delta
def DeltaAsianOptions(optionType, strike, maturity, spot, volatility, interestRate, numberOfSteps, numberOfPaths):
    mean = utils.DeltaOptionAsiatiques(optionType, strike, maturity, spot, volatility, interestRate, numberOfSteps,
                                       numberOfPaths)
    return mean


#####################################################################################################################

# Price of lookback
def MonteCarlo_LookBack(optionType, strike, maturity, spot, volatility, interestRate, numberOfSteps, numberOfPaths):
    mean = utils.PricingMonteCarloLookback(optionType, strike, maturity, spot, volatility, interestRate, numberOfSteps,
                                           numberOfPaths)
    return mean


# Simulation by Monte Carlo of delta
def Delta_LookBack(optionType, strike, maturity, spot, volatility, interestRate, numberOfSteps, numberOfPaths):
    mean = utils.DeltaOptionLookback(optionType, strike, maturity, spot, volatility, interestRate, numberOfSteps,
                                     numberOfPaths)
    return mean


#####################################################################################################################

# Price of Basket options
def MonteCarloBasket(optionType, a, b, strike, maturity, spot1, spot2, vol1, vol2, rho, interestRate,
                       numberOfSteps, numberOfPaths):
    mean = utils.PricingMonteCarloBasket(optionType, a, b, strike, maturity, spot1, spot2, vol1, vol2, rho,
                                         interestRate, numberOfSteps, numberOfPaths)
    return mean


# Price of Best of and worst of options
def MonteCarloPerf(optionType, strike, maturity, spot1, spot2, vol1, vol2, rho, interestRate,
                       numberOfSteps, numberOfPaths):
    mean = utils.PricingMonteCarloPerf(optionType, strike, maturity, spot1, spot2, vol1, vol2, rho, interestRate,
                       numberOfSteps, numberOfPaths)
    return mean


#####################################################################################################################
