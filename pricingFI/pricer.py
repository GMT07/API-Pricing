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

# # Price of sensibility delta of option
# def gtDeltaOptionVanilla(strike, maturity, spot, volatility, interestRate):
#     pass
#
#
# # Price of sensibility delta of option
# def gtGammaOptionVanilla(strike, maturity, spot, volatility, interestRate):
#     pass
#
#
# # Price of sensibility delta of option
# def gtVegaOptionVanilla(strike, maturity, spot, volatility, interestRate):
#     pass
#
#
# # Simulation
# def gtRhoOptionVanilla(strike, maturity, spot, volatility, interestRate):
#     pass
#
#
# # Price of sensibility delta of option
# def gtThetaOptionVanilla(strike, maturity, spot, volatility, interestRate):
#     pass


# def option_price_monte_carlo(option_type, S, K, T, r, V, nSimulations):
#     """Computes the option price with the Monte Carlo method.
#
#         Returns a option price with the Monte Carlo method
#         :param option_type: option type : call or put
#         :param S: spot or underlying price
#         :param K: exercise price
#         :param r: interest rate
#         :param V: volatility of underlying
#         :param T: time to maturity of option
#         :return: option price
#         """
#
#     drift = (r - (V*V / 2)) * T
#     vSqrdt = V * sqrt(T)
#     running_sum, this_payoff = 0.0, 0.0
#     for i in range(1, nSimulations):
#         gauss = utils.gauss1()
#         this_spot = S*exp(drift + vSqrdt*gauss)
#         if option_type.upper() == "CALL":
#             this_payoff = max(this_spot - K, 0.0)
#         elif option_type.upper() == "PUT":
#             this_payoff = max(K - this_spot, 0.0)
#
#         running_sum += this_payoff
#
#     mean = running_sum / nSimulations
#     mean = mean * exp(-r * T)
#
#     return mean
#
#
# def option_price_black_scholes(option_type, spot, strike, risk_free, sigma, maturity):
#     """Computes the option price with the Black Scholes formula.
#
#     Returns a option price with the Black-Scholes formula
#     :param option_type: option type : call or put
#     :param spot: spot or underlying price
#     :param strike: exercise price
#     :param risk_free: interest rate
#     :param sigma: volatility of underlying
#     :param maturity: time to maturity of option
#     :return: option price
#     """
#
#     time_sqrt = sqrt(maturity)
#     d1 = (log(spot/strike)+risk_free*maturity)/(sigma*time_sqrt)+0.5*sigma*time_sqrt
#     d2 = d1 - (sigma*time_sqrt)
#
#     if option_type.upper() == "CALL":
#         return spot * utils.pgaussred(d1) - strike*exp(-risk_free*maturity) * utils.pgaussred(d2)
#     elif option_type.upper() == "PUT":
#         return strike*exp(-risk_free*maturity) * utils.pgaussred(-d2) - spot * utils.pgaussred(-d1)



