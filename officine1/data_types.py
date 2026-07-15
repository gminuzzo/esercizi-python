import re

# --- Classi che ereditano dai tipi di base ---

class IntGEZ(int):
	def __new__(cls, num: int):
		if num < 0:
			raise ValueError(f"Errore IntGEZ(): input '{num}' non valido.")
		return super().__new__(cls, num)

class CodiceFiscale(str):
	def __new__(cls, s: str):
		if not re.fullmatch("[A-Za-z]{6}[0-9]{2}[A-Za-z][0-9]{2}[A-Za-z0-9]{5}", s):
			raise ValueError(f"Errore CodiceFiscale(): input '{s}' non valido.")
		return super().__new__(cls, s.upper())

class Telefono(str):
	def __new__(cls, s: str):
		if not re.fullmatch("((00|\+)39)?\s?\d{2,4}\s?\d{4,8}", s):
			raise ValueError(f"Errore CodiceFiscale(): input '{s}' non valido.")
		return super().__new__(cls, s)

class Targa(str):
	def __new__(cls, s: str):
		if not re.fullmatch("", s):
			raise ValueError(f"Errore Targa(): input '{s}' non valido.")
		return super().__new__(cls, s)

# --- Tipi di dato composti ---

class Indirizzo:
	...
