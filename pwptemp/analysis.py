def param_effect(temp_distribution, well, md_length=1):

    import math
    # Heat Source Terms
    qp = 2 * math.pi * (well.rpm / 60) * well.t + 2 * 0.24 * well.rhol * (well.vp ** 2) * (well.md[-1] /
                (well.ddi * 127.094 * 10 ** 6)) * (1 / 0.24 ** .5)
    qa = 0.05 * (well.wob * (well.rop / 3600) + 2 * math.pi * (well.rpm / 60) * well.tbit) + (well.rhol / 2 * 9.81) * (
                (well.q / 3600) / (0.095 * well.an)) + (2 * 0.3832 * well.md[-1] / ((well.r3 - well.r2) *
                (127.094 * 10 ** 6))) * ((2 * (0.7 + 1) * well.va) / (0.7 * math.pi * (well.r3 + well.r2) *
                (well.r3 - well.r2) ** 2)) ** 0.7


    # Eq coefficients - Inside Drill String
    n_cells = well.zstep - 2
    Tdsi = temp_distribution.tdsi
    Ta = temp_distribution.ta
    Toh = temp_distribution.toh
    c1z = ((well.rhol * well.cl * well.vp) / well.deltaz) / 2  # Vertical component for fluid inside drill string
    c1 = qp / (math.pi * (well.r1 ** 2))  # Heat source term for fluid inside drill string
    c3e = (2 * well.r3 * well.h3 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2  # East component for fluid inside annular
    c3 = qa / (math.pi * ((well.r3 ** 2) - (well.r2 ** 2)))  # Heat source term for fluid inside annular
    cell = round((n_cells * (1 - md_length)) + 1)
    total = (c1z * abs(Tdsi[-cell] - Tdsi[-(cell+1)]) + c1 + c3e * abs(Ta[-cell] - Toh[-cell]) + c3)

    p1 = c1z * abs(Tdsi[-cell] - Tdsi[-(cell+1)]) / total
    p1 = round(p1*100, 2)  # Effect of the mud circulation
    p2 = (c1 + c3) / total
    p2 = round(p2*100, 2)  # Effect of heat source terms
    p3 = c3e * abs(Ta[-cell] - Toh[-cell]) / total  # Effect of the formation
    p3 = round(p3 * 100, 2)

    class ParametersEffect(object):
        def __init__(self):
            self.flow = p1
            self.hs = p2
            self.fm = p3

        def plot(self):
            plot(self, 1)

    return ParametersEffect()


def hs_effect(well):

    import math
    # Heat Source Terms
    qp = 2 * math.pi * (well.rpm / 60) * well.t + 2 * 0.24 * well.rhol * (well.vp ** 2) * (well.md[-1] /
                (well.ddi * 127.094 * 10 ** 6)) * (1 / 0.24 ** .5)
    qa = 0.05 * (well.wob * (well.rop / 3600) + 2 * math.pi * (well.rpm / 60) * well.tbit) + (well.rhol / 2 * 9.81) * (
                (well.q / 3600) / (0.095 * well.an)) + (2 * 0.3832 * well.md[-1] / ((well.r3 - well.r2) *
                (127.094 * 10 ** 6))) * ((2 * (0.7 + 1) * well.va) / (0.7 * math.pi * (well.r3 + well.r2) *
                (well.r3 - well.r2) ** 2)) ** 0.7
    pi = math.pi
    rps = well.rpm / 60
    total = (qp + qa)
    qp = round((qp/total)*100, 2)
    qa = round((qa/total)*100, 2)
    p1 = 2*pi*rps*well.t / total
    p1 = round(p1*100, 2)  # Effect of Drill String Rotation in Heat Source Term Qp
    p2 = qp - p1  # Effect of Friction in Heat Source Term Qp
    p3 = 0.05*(well.wob * well.rop + 2 * pi * rps * well.tbit) / (qp + qa)
    p3 = round(p3 * 100, 2)  # Effect of Drill String Rotation in Heat Source Term Qa
    p4 = qa - p3  # Effect of Friction in Heat Source Term Qa

    class HeatSourceEffect(object):
        def __init__(self):
            self.ds_rot1 = p1
            self.fric1 = p2
            self.ds_rot2 = p3
            self.fric2 = p4
            self.hsr = round(qp/qa, 2)  #Pipe-Annular heat source ratio

        def plot(self):
            plot(self, 2)

    return HeatSourceEffect()


def plot(effect, how):
    import matplotlib.pyplot as plt
    if how == 1:
        labels = ['mud circulation', 'heat source terms', 'formation temperature']
        effects = [effect.flow, effect.hs, effect.fm]
        plt.pie(effects, startangle=90, autopct='%1.1f%%')
        plt.legend(labels, loc=0)
        plt.title('Effect of factors in the temperature calculation')
        plt.show()

    if how == 2:
        labels = ['pipe rotation in Qp', 'friction in Qp', 'pipe rotation in Qa', 'friction in Qa']
        effects = [effect.ds_rot1, effect.fric1, effect.ds_rot2, effect.fric2]
        plt.pie(effects, startangle=90)
        plt.legend(loc=0, labels=['%s, %1.1f %%' % (l, s) for l, s in zip(labels, effects)])
        title = 'Effect of factors in heat source terms. Qp/Qa = %1.2f' % effect.hsr
        plt.title(title)
        plt.show()
