def param_effect(temp_distribution, well, md_length=1):

    from math import pi
    # Heat Source Terms
    qp = 2 * pi * (well.rpm / 60) * well.t + 2 * 0.24 * well.rhol * (well.vp ** 2) * (well.md[-1] /
                (well.ddi * 127.094 * 10 ** 6)) * (1 / 0.24 ** .5)
    qa = 0.05 * (well.wob * (well.rop / 3600) + 2 * pi * (well.rpm / 60) * well.tbit) + (well.rhol / 2 * 9.81) * (
                (well.q / 3600) / (0.095 * well.an)) + (2 * 0.3832 * well.md[-1] / ((well.r3 - well.r2) *
                (127.094 * 10 ** 6))) * ((2 * (0.7 + 1) * well.va) / (0.7 * pi * (well.r3 + well.r2) *
                (well.r3 - well.r2) ** 2)) ** 0.7

    # Eq coefficients - Inside Drill String
    n_cells = well.zstep - 1
    Tdsi = temp_distribution.tdsi
    Tds = temp_distribution.tds
    Ta = temp_distribution.ta
    Toh = temp_distribution.toh
    Tfm = temp_distribution.tfm
    c1z = ((well.rhol * well.cl * well.vp) / well.deltaz) / 2  # Vertical component for fluid inside drill string
    c1e = (2*well.h1/well.r1) / 2  # East component for fluid inside drill string
    c1t = well.rhol * well.cl / temp_distribution.deltat
    c1 = qp / (pi * (well.r1 ** 2))  # Heat source term for fluid inside drill string
    c2z = (well.lambdal / (well.deltaz ** 2)) / 2
    c3e = (2 * well.r3 * well.h3 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2  # East component for fluid inside annular
    c3 = qa / (pi * ((well.r3 ** 2) - (well.r2 ** 2)))  # Heat source term for fluid inside annular
    cell = round(n_cells * md_length)
    if cell == 0:  # The temperature at the first cell is constant (Tin)
        p1 = 0  # Effect of convection + conduction
        p2 = 0  # Effect of heat source term
    if 0 < cell < well.zstep - 1:
        p1conv = (- c1z * (Tdsi[cell] - Tdsi[cell-1]) - c1z * (Tfm[cell] - Tfm[cell-1])) / c1t
        p1cond = (c1e * (Tds[cell] - Tdsi[cell]) + c1e * (Tfm[cell] - Tfm[cell])) / c1t
        p1 = round(p1conv + p1cond, 2)  # Effect of convection + conduction
        p2 = c1 / c1t  # Effect of heat source term
        p2 = round(p2, 2)
    if cell == well.zstep - 1:
        p1conv = (- c1z * (Tdsi[cell] - Tdsi[cell - 1]) - c1z * (Tfm[cell] - Tfm[cell - 1]) -
                 c2z * (Tds[cell] - Tds[cell - 1]) - c2z * (Tfm[cell] - Tfm[cell - 1])) / c1t
        p1cond = (c1e * (Tds[cell] - Tdsi[cell]) + c1e * (Tfm[cell] - Tfm[cell]) +
                  c3e * (Toh[cell] - Ta[cell]) + c3e * (Tfm[cell] - Tfm[cell])) / c1t
        p1 = round(p1conv + p1cond, 2)  # Effect of convection + conduction
        p2 = (c1 + c3) / c1t  # Effect of heat source term
        p2 = round(p2, 2)

    class ParametersEffect(object):
        def __init__(self):
            self.t1 = round(Tfm[cell], 2)
            self.cc = p1
            self.hs = p2
            self.t2 = round(Tdsi[cell], 2)
            self.time = temp_distribution.time
            self.length = round(md_length * well.md[-1], 1)

        def plot(self):
            plot(self, 1)

    return ParametersEffect()


def hs_effect(well):

    from math import pi
    # Heat Source Terms
    qp = 2 * pi * (well.rpm / 60) * well.t + 2 * 0.24 * well.rhol * (well.vp ** 2) * (well.md[-1] /
                (well.ddi * 127.094 * 10 ** 6)) * (1 / (0.24 ** .5))
    qa = 0.05 * (well.wob * (well.rop / 3600) + 2 * pi * (well.rpm / 60) * well.tbit) + (well.rhol / 2 * 9.81) * (
                (well.q / 3600) / (0.095 * well.an)) + (2 * 0.3832 * well.md[-1] / ((well.r3 - well.r2) *
                (127.094 * 10 ** 6))) * ((2 * (0.7 + 1) * well.va) / (0.7 * pi * (well.r3 + well.r2) *
                (well.r3 - well.r2) ** 2)) ** 0.7
    total = qp + qa
    p1 = (2*pi*(well.rpm/60)*well.t) / total
    p1 = round(p1, 2)  # Effect of Drill String Rotation in Heat Source Term Qp
    p2 = (qp - p1) / total
    p2 = round(p2, 2)  # Effect of Friction in Heat Source Term Qp
    p3 = (0.05*(well.wob * well.rop + 2 * pi * (well.rpm/60) * well.tbit)) / total
    p3 = round(p3, 2)  # Effect of Drill String Rotation in Heat Source Term Qa
    p4 = (qa - p2) / total
    p4 = round(p4, 2)  # Effect of Friction in Heat Source Term Qa

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
        values = [effect.t2, abs(effect.cc), effect.hs, effect.t1]
        bars = ['Tf: %1.2f°C' % effect.t2, 'Convection and Conduction: %1.2f°C' % effect.cc, 'Heat Source Term: %1.2f°C'
                % effect.hs, 'To: %1.2f°C' % effect.t1]
        position = range(4)
        plt.barh(position, values, color=['blue', 'red', 'green', 'blue'])
        if effect.t1 > effect.t2:
            plt.barh(0, abs(effect.cc + effect.hs), color='red', left=effect.t2)
            plt.text(effect.t2, 0, '%1.2f°C' % (effect.cc + effect.hs))
        else:
            plt.barh(0, abs(effect.cc + effect.hs), color='green', left=effect.t1)
            plt.text(effect.t1, 0, '%1.2f°C' % (effect.cc + effect.hs))
        plt.yticks(position, ['Tf', 'CC', 'HS', 'To'])
        plt.title('Temperature contribution of main factors at %1.1fh - %1.1fm' % (effect.time, effect.length),
                  fontweight='bold')
        for i, v in enumerate(values):
            plt.text(v/8, i, bars[i])
        plt.xlabel('Temperature, °C')
        plt.show()

    if how == 2:
        labels = ['pipe rotation in Qp', 'friction in Qp', 'pipe rotation in Qa', 'friction in Qa']
        effects = [effect.ds_rot1, effect.fric1, effect.ds_rot2, effect.fric2]
        plt.pie(effects, startangle=90)
        plt.legend(loc=0, labels=['%s, %1.2f %%' % (l, s) for l, s in zip(labels, effects)])
        title = 'Effect of factors in heat source terms. Qp/Qa = %1.2f' % effect.hsr
        plt.title(title)
        plt.show()
