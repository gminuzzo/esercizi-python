import sys

def __check_input(string:str, max_occurrences:dict[ str, int ])->bool:
    # string deve essere una stringa o un carattere, non un numero.
    if string != str(string):
        return False

    for k,v in max_occurrences.items():
        # Le chiavi di max_occurrences devono essere caratteri, non numeri.
        if k != str(k):
            return False
        # I valori associati alle chiavi di max_occurrences devono essere interi >= 0, non caratteri.
        try:
            if int(v) < 0:
                return False
        except ValueError:
            return False
    return True

def __check_legal_substring(substring:str)->bool:
    return True

def __find_legal_substring(string:str, max_occurrences:dict[ str, int ], start:int)->str:
    result : str = ""
    occurrence_counter : dict[ str, int ] = max_occurrences.copy()
    end : int = start
    while end < len(string):
        print(string[end])
        if string[end] not in max_occurrences:
            result += string[end]
            end += 1
        elif occurrence_counter[ string[end] ] != 0:
            result += string[end]
            end += 1
            occurrence_counter[ string[end] ] -= 1
        else:
            break
    return result

def substring_allow_limits(string:str, max_occurrences:dict[ str, int ])->str:
    assert __check_input(string, max_occurrences)
    result : str = ""
    for start in range(0, len(string)):
        current_substring = __find_legal_substring(string, max_occurrences, start)
        assert __check_legal_substring(current_substring)
        if current_substring > result:
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
            occurrence_limit = input("Inserisci un intero >= 0: ")
            if occurrence_limit == "":
                print("ERRORE: Il valore dell'intero non può essere vuoto.")
                continue
            try:
                result[char] = int(occurrence_limit)
                if result[char] < 0:
                    print("ERRORE: Il valore inserito non può essere negativo.")
                    continue
                break
            except:
                print("ERRORE: Il valore inserito non è un intero.")

    return result

def main()->int:
    #input_string : str = ui_input_string()
    #input_limits : dict[ str, int ] = ui_input_limits()
    max_substring : str = substring_allow_limits("ciao mondo", {"i":0, "o":2})
    #print(f"\nStringa originale: '{input_string}'")
    print(f"\nLa porzione di stringa più lunga che soddisfa le condizioni è: '{max_substring}'\n")
    return 0

if __name__ == "__main__":
    sys.exit( main() )

"""
ciao mondo
----------
c, c > "" --> result = c
i, "" < c --> result = c
ao mond, ao mond > c --> result = ao mond
"""