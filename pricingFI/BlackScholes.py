# coding: utf-8
from numpy import log, exp

# Descriptif des payoffs utilisés


class PayOff:
    def __init__(self, strike):
        self._strike = strike

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0}".format(self._strike)

    def _get_strike(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
            à l'attribut 'strike'"""

        print("On accède à l'attribut strike !")
        return self._strike

    def _set_strike(self, strike):
        """Méthode appelée quand on souhaite modifier le strike"""
        self._strike = strike

    # On va dire à Python que notre attribut strike pointe vers une propriété
    strike = property(_get_strike, _set_strike)


# Pricing des options vanilles : call et put européennes

class PayOffCall(PayOff):

    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        return max(spot - self._strike, 0.0)


class PayOffPut(PayOff):

    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        return max(self._strike - spot, 0.0)


# Pricing des options Cash_Or_Nothing


class PayOff_Cash_Or_Nothing_Call(PayOff):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        if spot >= self._strike:
            return 1
        else:
            return 0


class PayOff_Cash_Or_Nothing_Put(PayOff):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        if spot <= self._strike:
            return 1
        else:
            return 0


# Pricing des options Asset_Or_Nothing


class PayOff_Asset_Or_Nothing_Call(PayOff):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        if spot >= self._strike:
            return spot
        else:
            return 0


class PayOff_Asset_Or_Nothing_Put(PayOff):

    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        if spot <= self._strike:
            return spot
        else:
            return 0

# Pricing des options doubles digitales


class PayOffDoubleDigital(PayOff):
    def __init__(self, LowerLevel, UpperLevel):
        self._LowerLevel = LowerLevel
        self._UpperLevel = UpperLevel

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self._LowerLevel, self._UpperLevel)

    def _get_LowerLevel(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
            à l'attribut 'LowerLevel'"""

        print("On accède à l'attribut LowerLevel !")
        return self._LowerLevel

    def _set_LowerLevel(self, LowerLevel):
        """Méthode appelée quand on souhaite modifier le LowerLevel"""
        self._LowerLevel = LowerLevel

    # On va dire à Python que notre attribut strike pointe vers une propriété
    LowerLevel = property(_get_LowerLevel, _set_LowerLevel)

    def _get_UpperLevel(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
            à l'attribut 'UpperLevel'"""

        print("On accède à l'attribut UpperLevel !")
        return self._UpperLevel

    def _set_UpperLevel(self, UpperLevel):
        """Méthode appelée quand on souhaite modifier le UpperLevel"""
        self._UpperLevel = UpperLevel

    # On va dire à Python que notre attribut strike pointe vers une propriété
    UpperLevel = property(_get_UpperLevel, _set_UpperLevel)

    def description_payoff(self, spot):
        if spot <= self._LowerLevel: return 0
        if spot >= self._UpperLevel: return 0
        return 1


# Descriptif des payoffs utilisés


class PayOffExotiques:
    def __init__(self, strike):
        self._strike = strike

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0}".format(self._strike)

    def _get_strike(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
            à l'attribut 'strike'"""

        print("On accède à l'attribut strike !")
        return self._strike

    def _set_strike(self, strike):
        """Méthode appelée quand on souhaite modifier le strike"""
        self._strike = strike

    # On va dire à Python que notre attribut strike pointe vers une propriété
    strike = property(_get_strike, _set_strike)

# Pricing des options asiatiques

# Options asiatiques à cours arithmétique et prix d'exercice fixe


class PayOff_Arithmetric_Average_Call(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        rev = sum(spot)
        avg = rev/len(spot)
        return max(avg - self._strike, 0.0)


class PayOff_Arithmetric_Average_Put(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        rev = sum(spot)
        avg = rev/len(spot)
        return max(self._strike - avg, 0.0)


# Options asiatiques à cours géométrique et prix d'exercice fixe

class PayOff_Geometric_Average_Call(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        log_rev = log(spot[0])
        n = len(spot)
        for i in range(1, n):
            log_rev += log(spot[i])

        avg = exp(log_rev/n)
        return max(avg - self._strike, 0.0)


class PayOff_Geometric_Average_Put(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        log_rev = log(spot[0])
        n = len(spot)
        for i in range(1, n):
            log_rev += log(spot[i])

        avg = exp(log_rev / n)
        return max(self._strike - avg, 0.0)


# Options asiatiques à cours arithmétique et prix d'exercice flottant

class PayOff_Arithmetric_Flottant_Call(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        rev = sum(spot)
        n = len(spot)

        avg = rev/n
        spot_t = spot[n-1]
        return max(spot_t - avg, 0.0)


class PayOff_Arithmetric_Flottant_Put(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        rev = sum(spot)
        n = len(spot)

        avg = rev / n
        spot_t = spot[n - 1]
        return max(avg - spot_t, 0.0)


# Options asiatiques à cours arithmétique et prix d'exercice flottant

class PayOff_Geometric_Flottant_Call(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        log_rev = log(spot[0])
        n = len(spot)
        for i in range(1, n):
            log_rev += log(spot[i])

        avg = exp(log_rev / n)
        spot_t = spot[n - 1]
        return max(spot_t - avg, 0.0)


class PayOff_Geometric_Flottant_Put(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        log_rev = log(spot[0])
        n = len(spot)
        for i in range(1, n):
            log_rev += log(spot[i])

        avg = exp(log_rev / n)
        spot_t = spot[n - 1]
        return max(avg - spot_t, 0.0)

# Options lookback


class PayOff_lookback_Call(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        rev = max(spot)
        n = len(spot)
        spot_t = spot[n - 1]
        return rev - spot_t # toujours positive ou supérieur à zero.


class PayOff_lookback_Put(PayOffExotiques):
    def __init__(self, strike):
        super().__init__(strike)

    def description_payoff(self, spot):
        rev = min(spot)
        n = len(spot)
        spot_t = spot[n - 1]
        return spot_t - rev # toujours positive ou supérieur à zero.


# Descriptif des payoffs utilisés


class PayOffPanier:
    def __init__(self, strike, a, b, vol1, vol2, rho):
        self._strike = strike
        self._a = a
        self._b = b
        self._vol1 = vol1
        self._vol2 = vol2
        self._rho = rho

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1} {2} {3} {4} {5}".format(self._strike, self._a, self._b, self._vol1,
                                self._vol2, self._rho)

    def _get_strike(self):
        return self._strike

    def _set_strike(self, strike):
        self._strike = strike

    strike = property(_get_strike, _set_strike)

    def _get_a(self):
        return self._a

    def _set_a(self, a):
        self._a = a

    a = property(_get_a, _set_a)

    def _get_b(self):
        return self._b

    def _set_b(self, b):
        self._b = b

    b = property(_get_b, _set_b)

    def _get_vol1(self):
        return self._vol1

    def _set_vol1(self, vol1):
        self._vol1 = vol1

    vol1 = property(_get_vol1, _set_vol1)

    def _get_vol2(self):
        return self._vol2

    def _set_vol2(self, vol2):
        self._vol2 = vol2

    vol2 = property(_get_vol2, _set_vol2)

    def _get_rho(self):
        return self._rho

    def _set_rho(self, rho):
        self._rho = rho

    rho = property(_get_rho, _set_rho)


# Options basket

class PayOff_basket_Call(PayOffPanier):
    def __init__(self, strike, a, b, vol1, vol2, rho):
        super().__init__(strike, a, b, vol1, vol2, rho)

    def description_payoff(self, spot1, spot2):
        rev = self._a*spot1 + self._b*spot2
        return max(rev - self._strike, 0.0)


class PayOff_basket_Put(PayOffPanier):
    def __init__(self, strike, a, b, vol1, vol2, rho):
        super().__init__(strike, a, b, vol1, vol2, rho)

    def description_payoff(self, spot1, spot2):
        rev = self._a*spot1 + self._b*spot2
        return max(self._strike - rev, 0.0)


# Options Best-of

class PayOff_BestOf_Call(PayOffPanier):
    def __init__(self, strike, a, b, vol1, vol2, rho):
        super().__init__(strike, a, b, vol1, vol2, rho)

    def description_payoff(self, spot1, spot2):
        return max(max(spot1, spot2) - self._strike, 0.0)


class PayOff_BestOf_Put(PayOffPanier):
    def __init__(self, strike, a, b, vol1, vol2, rho):
        super().__init__(strike, a, b, vol1, vol2, rho)

    def description_payoff(self, spot1, spot2):
        return max(self._strike - max(spot1, spot2), 0.0)


# Options Worst-of

class PayOff_WorstOf_Call(PayOffPanier):
    def __init__(self, strike, a, b, vol1, vol2, rho):
        super().__init__(strike, a, b, vol1, vol2, rho)

    def description_payoff(self, spot1, spot2):
        return max(min(spot1, spot2) - self._strike, 0.0)


class PayOff_WorstOf_Put(PayOffPanier):
    def __init__(self, strike, a, b, vol1, vol2, rho):
        super().__init__(strike, a, b, vol1, vol2, rho)

    def description_payoff(self, spot1, spot2):
        return max(self._strike - min(spot1, spot2), 0.0)

