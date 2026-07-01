import sys

def substring_allow_limits(string:str, max_occurrences:dict[ str, int ])->str:
    occurrence_counter : dict[ str, int ] = max_occurrences
    result : str = ""
    current_substring : str = ""
    for char in string:
        if char not in max_occurrences:
            current_substring += char
        elif occurrence_counter[char] != 0:
            current_substring += char
            occurrence_counter[char] -= 1
        else:
            if len(current_substring) > len(result):
                result = current_substring
            current_substring = ""
    if len(current_substring) > len(result):
                result = current_substring
    return result

def ui_input_string()->str:
    result : str = input("\nInserisci una stringa: ")
    return result

def ui_input_limits()->dict[ str, int ]:
    result : dict[ str, int ] = dict()
    while True:
        char = input("\nInserisci un carattere (stringa vuota per terminare): ")
        if char == "":
            break
        if len(char) != 1:
            print("ERRORE: Inseriti troppi caratteri.")
            continue

        while True:
            occurrence_limit = input("\nInserisci un intero positivo: ")
            if occurrence_limit == "":
                print("ERRORE: Il valore dell'intero non può essere vuoto.")
                continue
            try:
                result[char] = int(occurrence_limit)
                if result[char] < 0:
                    print("ERRORE: Il valore inserito non è un intero positivo.")
                    continue
                break
            except:
                print("ERRORE: Il valore inserito non è un intero.")

    return result

def main()->int:
    input_string : str = ui_input_string()
    input_limits : dict[ str, int ] = ui_input_limits()
    max_substring : str = substring_allow_limits(input_string, input_limits)
    print(f"\nStringa originale: '{input_string}'")
    print(f"\nLa porzione di stringa più lunga che soddisfa le condizioni è: '{max_substring}'\n")
    return 0

if __name__ == "__main__":
    sys.exit( main() )