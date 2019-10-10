def param_effect(temp_distribution, well):

    import math
    # Eq coefficients - Inside Drill String
    deltaz = 50
    Tdsi = temp_distribution.tdsi
    Ta = temp_distribution.ta
    Toh = temp_distribution.toh
    c1z = ((well.rhol * well.cl * well.vp) / deltaz) / 2  # Vertical component for fluid inside drill string
    c1 = well.qp / (math.pi * (well.r1 ** 2))  # Heat source term for fluid inside drill string
    c3e = (2 * well.r3 * well.h3 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2  # East component for fluid inside annular
    c3 = well.qa / (math.pi * ((well.r3 ** 2) - (well.r2 ** 2)))  # Heat source term for fluid inside annular

    total = (c1z * abs(Tdsi[-1] - Tdsi[-2]) + c1 + c3e * abs(Ta[-1] - Toh[-1]) + c3)

    p1 = c1z * abs(Tdsi[-1] - Tdsi[-2]) / total
    p1 = round(p1*100, 2)  # Effect of the mud circulation
    p2 = (c1 + c3) / total
    p2 = round(p2*100, 2)  # Effect of heat source terms
    p3 = c3e * abs(Ta[-1] - Toh[-1]) / total  # Effect of the formation
    p3 = round(p3 * 100, 2)

    class ParametersEffect(object):
        def __init__(self):
            self.flow = p1
            self.hs = p2
            self.fm = p3

    return ParametersEffect()


def hs_effect(well):

    import math
    pi = math.pi
    rps = well.rpm / 60
    total = (well.qp + well.qa)
    qp = round((well.qp/total)*100, 2)
    qa = round((well.qa/total)*100, 2)
    p1 = 2*pi*rps*well.t / total
    p1 = round(p1*100, 2)  # Effect of Drill String Rotation in Heat Source Term Qp
    p2 = qp - p1  # Effect of Friction in Heat Source Term Qp
    p3 = 0.05*(well.wob * well.rop + 2 * pi * rps * well.tbit) / (well.qp + well.qa)
    p3 = round(p3 * 100, 2)  # Effect of Drill String Rotation in Heat Source Term Qa
    p4 = qa - p3  # Effect of Friction in Heat Source Term Qa

    class HeatSourceEffect(object):
        def __init__(self):
            self.ds_rot1 = p1
            self.fric1 = p2
            self.ds_rot2 = p3
            self.fric2 = p4
            self.hsr = round(well.qp/well.qa, 2)  #Pipe-Annular heat source ratio

    return HeatSourceEffect()

def plot(effect, how):
    import matplotlib.pyplot as plt
    if how == 1:
        labels = ['mud circulation', 'heat source terms', 'formation temperature']
        effects = [effect.flow, effect.hs, effect.fm]
        plt.pie(effects, startangle=90, autopct='%1.1f%%')
        plt.legend(labels, loc=0)
        plt.title('Effect of the parameters in the temperature calculation')
        plt.show()

    if how == 2:
        labels = ['pipe rotation in Qp', 'friction in Qp', 'pipe rotation in Qa', 'friction in Qa']
        effects = [effect.ds_rot1, effect.fric1, effect.ds_rot2, effect.fric2]
        plt.pie(effects, startangle=90)
        plt.legend(loc=0, labels=['%s, %1.1f %%' % (l, s) for l, s in zip(labels, effects)])
        title = 'Effect of the drill string rotation and friction in heat source terms. Qp/Qa = %1.2f' % effect.hsr
        plt.title(title)
        plt.show()
