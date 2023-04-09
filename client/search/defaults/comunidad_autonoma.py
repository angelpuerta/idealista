from enum import Enum

class Andalucia(Enum):
    ALMERIA = "Almería"
    CADIZ = "Cádiz"
    CORDOBA = "Córdoba"
    GRANADA = "Granada"
    HUELVA = "Huelva"
    JAEN = "Jaén"
    MALAGA = "Málaga"
    SEVILLA = "Sevilla"

class Aragon(Enum):
    HUESCA = "Huesca"
    TERUEL = "Teruel"
    ZARAGOZA = "Zaragoza"

class Asturias(Enum):
    ASTURIAS = "Asturias"

class Baleares(Enum):
    BALEARES = "Illes Balears"

class Canarias(Enum):
    LAS_PALMAS = "Las Palmas"
    SANTA_CRUZ_DE_TENERIFE = "Santa Cruz de Tenerife"

class Cantabria(Enum):
    CANTABRIA = "Cantabria"

class CastillaLaMancha(Enum):
    ALBACETE = "Albacete"
    CIUDAD_REAL = "Ciudad Real"
    CUENCA = "Cuenca"
    GUADALAJARA = "Guadalajara"
    TOLEDO = "Toledo"

class CastillaLeon(Enum):
    AVILA = "Ávila"
    BURGOS = "Burgos"
    LEON = "León"
    PALENCIA = "Palencia"
    SALAMANCA = "Salamanca"
    SEGOVIA = "Segovia"
    SORIA = "Soria"
    VALLADOLID = "Valladolid"
    ZAMORA = "Zamora"

class Catalunya(Enum):
    BARCELONA = "Barcelona"
    GIRONA = "Girona"
    LLEIDA = "Lleida"
    TARRAGONA = "Tarragona"

class Ceuta(Enum):
    CEUTA = "Ceuta"

class ComunidadValenciana(Enum):
    ALICANTE = ""
    CASTELLON = 2
    VALENCIA = 3

class Extremadura(Enum):
    BADAJOZ = "Badajoz"
    CACERES = "Cáceres"

class Galicia(Enum):
    A_CORUNA = "A Coruña"
    LUGO = "Lugo"
    OURENSE = "Ourense"
    PONTEVEDRA = "Pontevedra"

class LaRioja(Enum):
    LA_RIOJA = "La Rioja"

class Madrid(Enum):
    MADRID = "Madrid"

class Melilla(Enum):
    MELILLA = "Melilla"

class Murcia(Enum):
    MURCIA = "Murcia"

class Navarra(Enum):
    NAVARRA = "Navarra"

class PaisVasco(Enum):
    ALAVA = "Álava"
    GUIPUZCOA = "Guipúzcoa"
    VIZCAYA = "Vizcaya"

class ComunidadAutonoma(Enum):
    ANDALUCIA = Andalucia
    ARAGON = Aragon
    ASTURIAS = Asturias
    BALEARES = Baleares
    CANARIAS = Canarias
    CANTABRIA = Cantabria
    CASTILLA_LA_MANCHA = CastillaLaMancha
    CASTILLA_LEON = CastillaLeon
    CATALUÑA = Catalunya
    CEUTA = Ceuta
    COMUNIDAD_VALENCIANA = ComunidadValenciana
    EXTREMADURA = Extremadura
    GALICIA = Galicia
    LA_RIOJA = LaRioja
    MADRID = Madrid
    MELILLA = Melilla
    MURCIA = Murcia
    NAVARRA = Navarra
    PAIS_VASCO = PaisVasco