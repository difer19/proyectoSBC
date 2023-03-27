from pyswip import Prolog


class SistemaExpertoMecanica:
    def __init__(this):
        this.prolog = Prolog()
        this.prolog.consult("vh.pl")
    
    def diagnostico(this, sintomas):
        print(procesarSintoma(sintomas))
        return list(this.prolog.query(procesarSintoma(sintomas)))
    
    def diagnostico2(this, problema):
        return list(this.prolog.query(problema))

def procesarSintoma(sintomas):
    cad = ""
    for sintoma in sintomas:
        cad += "sintoma(X, " + str(sintoma) + "),"
    return cad[:-1]


# sbc = SistemaExpertoMecanica()
# print(sbc.diagnostico2("sintoma(X, golpeteo_motor),sintoma(X, humo_negro_escape)"))