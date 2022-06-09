import re
import pandas as pd

texto = '''Ladrillo Visto 23.5x10.5 Cm
Ladrillo Visto 23.5x10.5 CM
Ladrillo Visto 24.7x11.2x5.6 cm
Tejuela Refractaria 20 mm
Tejuela Refractaria 15 mm
Tierra Refractaria 10 kg
Yeso Blanco El Puntano x  3 Kg
Yeso Blanco Entre Rios X  40 Kgs
Nylon Capa Aisladora 15cm x 50 Mt
Nylon Capa Aisladora 20cm x 50 Mts
Nylon Capa Aisladora 30cm x 50 mts
Manguera Tramontina 1/2" X 15 Mts
Manguera Tramontina 1/2" x 25 Mts
Disco Diamantado Norton Segmentado 110 mm
Disco Diamantado Norton Turbo 110 mm
Disco Diamantado Norton Continuo 110 mm'''

#separar por salto de linea
lista = re.split('\r?\n|\r',texto)

#pasar a minúscula
lista = [i.lower() for i in lista]

#unificar unidades de medida
lista = [re.sub('(cm|Cm|CM)','cm',i) for i in lista]
lista = [re.sub('(mts|Mts|Metros|Metro|Mt)','mt',i) for i in lista]
lista = [re.sub('(kg|Kg|Kgs)','kg',i) for i in lista]
lista = [re.sub('\s(?=x)(?<=\D)|(?<=x)\s(?=\d)','',i) for i in lista]

#separar medida + unidad de medida
lista = [re.split('(?<=\s)(?=\d)|(?<=\s)(?=cm|mm|kg|mt)',i) for i in lista]

#crear listas de materiales, medidas y unidades de medida
materiales = [i[0] for i in lista]
medida = [i[1] for i in lista]
uMedida = [i[-1] for i in lista]

#concatenar todo
df = pd.DataFrame([materiales,uMedida,medida]).T.set_axis(['materiales','unidad de medida','medida'],axis=1)
df