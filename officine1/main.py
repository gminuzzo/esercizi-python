import sys
from data_types import IntGEZ
from data_types import CodiceFiscale
from data_types import Telefono

def main()->int:
	print("\n--- Test dei tipi di dato ---")

	print("\n--- Test IntGEZ() ---")
	try:
		num = 1
		print(f"IntGEZ({num}) ==> {IntGEZ(num)}: {type(IntGEZ(num))}")
		num = 0
		print(f"IntGEZ({num}) ==> {IntGEZ(num)}: {type(IntGEZ(num))}")
		num = 3.14
		print(f"IntGEZ({num}) ==> {IntGEZ(num)}: {type(IntGEZ(num))}")
		num = -1
		print(f"IntGEZ({num}) ==> {IntGEZ(num)}: {type(IntGEZ(num))}")
	except ValueError as e:
		print(e)

	print("\n--- Test CodiceFiscale() ---")
	try:
		cf = CodiceFiscale("MNZGDN94T10H501L")
		print(f"CodiceFiscale({cf}): {type(cf)}")

		cf = CodiceFiscale("mnzgdn94t10h501l")
		print(f"CodiceFiscale({cf.lower()}): {type(cf)}")
		
		cf = CodiceFiscale("NZGDN94T10H501L")
		print(f"CodiceFiscale({cf}): {type(cf)}")
	except ValueError as e:
		print(e)

	print("\n--- Test Telefono() ---")
	try:
		tel = Telefono("+39 351 8205356")
		print(f"Telefono({tel}): {type(tel)}")
		tel = Telefono("0039 351 8205356")
		print(f"Telefono({tel}): {type(tel)}")
		tel = Telefono("351 8205356")
		print(f"Telefono({tel}): {type(tel)}")
		tel = Telefono("351 82 05356")
		print(f"Telefono({tel}): {type(tel)}")
	except ValueError as e:
		print(e)

	print()

if __name__ == "__main__":
	sys.exit( main() )