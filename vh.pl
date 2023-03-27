sintoma(inyectores_sucios, golpeteo_motor).
sintoma(inyectores_sucios, tirones_motor). 

sintoma(inyectores_descalibrados, consumo_excesivo_combustible). 
sintoma(inyectores_descalibrados, humo_negro_escape).

sintoma(problema_electrico, luces_debiles).  
sintoma(problema_electrico, problemas_arranque).

sintoma(problema_sistema_arranque, problemas_arranque).
sintoma(problema_sistema_arranque, ruidos_encendido).

sintoma(problema_sistema_de_refrigeracion, perdida_refrigerante).
sintoma(problema_sistema_de_refrigeracion, humo_blanco).
sintoma(problema_sistema_de_refrigeracion, testigo_temperatura).

sintoma(problema_radiador, ruidos).

sintoma(problema_bomba_de_aceite, testigo_presion_aceite).
sintoma(problema_bomba_de_aceite, ruidos).
sintoma(problema_bomba_de_aceite, perdida_de_potencia).

sintoma(problema_correa_de_distribucion, ruidos).
sintoma(problema_correa_de_distribucion, vibraciones).
sintoma(problema_correa_de_distribucion, problemas_arranque).
sintoma(problema_correa_de_distribucion, perdida_de_potencia).

sintoma(problema_pistones, ruidos).
sintoma(problema_pistones, perdida_de_potencia).
sintoma(problema_pistones, humo_azul).
sintoma(problema_pistones, consumo_de_aceite).

sintoma(problema_anillos, perdida_de_potencia).
sintoma(problema_anillos, ruidos).

sintoma(problema_sensores, parada_motor).
sintoma(problema_sensores, testigos_irregulares).
sintoma(problema_sensores, perdida_de_potencia).
sintoma(problema_sensores, acelaracion_lenta).
sintoma(problema_sensores, consumo_excesivo_combustible).

sintoma(problema_bomba_de_agua, sobrecalentamiento).
sintoma(problema_bomba_de_agua, perdida_de_refrigerante).
sintoma(problema_bomba_de_agua, ruidos).

sintoma(problema_bujias, problemas_arranque).
sintoma(problema_bujias, perdida_de_potencia).
sintoma(problema_bujias, consumo_excesivo_combustible).
sintoma(problema_bujias, humo_excesivo_escape).

posiblesSintomas(X, Y) :- sintoma(X, Y).
