"""
@Jalexu on discord had an idea for fingerspelling using the whole keyboard, not just one letter at a time, orthospelling was born
Turns out it was actually born 200 years ago for the Michela stenotype, but back then they implemented it by hand, not generatively with a python script called Shrimple
"""

entry_strokes={
    "starter normal"  :['PN'],        #shrimple with normal formatting
    "starter attached":[],            #shrimple with not space at the start
    "starter cap"     :[],            #shrimple but capped the first letter
    "starter acronyms":[],            #shrimple but all caps
    "starter cap attached":[],
    "starter acronyms attached":[]
}





make_starter_letters_have_left_to_right_priority = True
user_definitions={
    "" : "",

    "F": "f",
    "FC": "h",
    "FZ": "j",
    "FP": "t",
    "FN": "gn",
    "FCN": "r",
    "FCP": "b",
    "FCPe": "be", #exception to avoid conflicts with CPe=che
    "FCPi": "bi", #exception to avoid conflicts with CPi=chi
    "FCPue": "be ", #exception to avoid conflicts with CPue=che_
    "FCPui": "bi ",  #exception to avoid conflicts with CPui=chi_
    "FZP": "g",
    "FZPe": "ghe",
    "FZPi": "ghi",
    "FZPue": "ghe ",
    "FZPui": "ghi ",
    "FZPI": "ghi",

    "S": "s",
    "SC": "v",
    "SZ": "z",
    "SP": "c",
    "SN": "gl",
    "SCP": "d",
    "SCPe": "de", #exception to avoid conflicts with CPe=che
    "SCPi": "di", #exception to avoid conflicts with CPi=chi
    "SCPI": "di", #exception to avoid conflicts with CPI=chi
    "SCPue": "di ", #exception to avoid conflicts with CPue=che_
    "SCPui": "di ", #exception to avoid conflicts with CPui=che_
    "SCN": "l",
    "SZP": "m",
    "SZN": "x",
    "SXIUi": "schi",
    "SXIUe": "sche",
    "SXIUui": "schi ",
    "SXIUue": "sche ",

    "C": "sc",
    "CP": "c",
    "CPe": "che",
    "CPi": "chi",
    "CPI": "chi",
    "CPue": "che ",
    "CPui": "chi ",
    "CN": "u",


    "Z": "s",
    "ZIU": "sb",
    "ZRIU": "sd",
    "ZXIU": "sg",
    "ZXIUe": "sghe",
    "ZXIUi": "sghi",
    "ZXIUue": "sghe ",
    "ZXIUui": "sghi ",
    "ZXI": "sv",
    "ZP": "g",
    "ZN": "i",

    "P": "p",

    "N": "n",

    "R": "r",
    "RI": "l",
    "RU": "m",
    "RIU": "t",

    "X": "s",
    "XI": "f",
    "XU": "n",
    "XIU": "c",

    "I": "i",
    "IU": "p",

    "U": "u",

    "u": "u",
    "unc": "ù",
    "ua": "a ", #word ending vowel
    "ue": "e ", #word ending vowel
    "ui": "i ", #word ending vowel
    "uie" :"o ", #word ending vowel
    "uia" :"u ", #word ending vowel

    "i": "i",
    "ia": "è",
    "ianc": "ò",
    "ie": "o",
    "iea": "ì",
    "ie": "o",

    "e": "e",
    "ea": "à",

    "a": "a",

    "n": "n",
    "nz": "i",
    "nc": "u",
    "ns": "gl",
    "nf": "gn",
    "nzs": "x",
    "nzf": "nt",
    "ncs": "l",
    "ncf": "r",

    "p": "p",
    "pc": "c",
    "ps": "c",
    "pf": "t",
    "pzs": "m",
    "pzf": "g",
    "pcs": "d",
    "pcf": "b",

    "z": "s",
    "zs": "z",
    "zf": "j",
 
    "c": "sc",
    "cs": "v",
    "cf": "h",

    "s": "s",

    "f": "f"
}



strokes_you_can_use_to_exit_shrimple_with=[

    "FCf"

]




#dedicated key settings:
dedicated_key = '+'             #Instead of a starter stroke
make_words_done_with_dedicated_key_exit_immediately = True
#joiner_strokes={ #If Shrimple automatically exits, maybe you wanna use KWR to stay in Shrimple
#    "left-hand joiner" : "^SKWR",
#    "right-hand joiner" : "FPL"
#}

































































import re

LONGEST_KEY = 40

"""
def construct_every_combination(part_of_the_keyboard):
    #Given a set of options, left or right, up or down.
    #Will return all combinations:
    #left+up, left+down, right+up, right+down, etc.

    path_direction=(part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys())

    every_combination_dictionary={}
    error_rate = {
        'positives': 0,
        'negatives': 0
    }
    every_combination = [[]]  # Initialize with empty list
    for length_of_combination in range(len(path_direction)):
        current_options = path_direction[length_of_combination]
        new_combinations = []  # Temporary list to store updated combinations

        for option in current_options:
            for existing_combination in every_combination:
                new_combination = existing_combination + [option]
                if re.fullmatch(r'(F?S?C?Z?P?N?R?X?I?U?u?i?e?a?n?p?z?c?s?f?)',"".join(new_combination)):
                    error_rate['positives']+=1
                    new_combinations.append(new_combination)
                else:
                    error_rate['negatives']+=1

        every_combination.extend(new_combinations)  # Add new combinations

    print('error rate is: ' + str(error_rate))

    for combination in every_combination:
        the_combination = "".join(combination)

        translation=""
        for chord in combination:
            translation += part_of_the_keyboard[chord]

        #clean up spacing
        if " " in translation:
            translation = translation.replace(" ","")
        else:
            translation = translation + '{^}'

        if not the_combination in every_combination_dictionary:
            every_combination_dictionary[the_combination] = translation


    return every_combination_dictionary


#FSCZPNRXIUuieanpzcsf
generated_definitions = construct_every_combination(user_definitions)

import json
with open("MichelaShrimple.json", "w") as outfile:
    json.dump(generated_definitions, outfile, indent=0)

"""



def construct_stroke(target_chord, chord_dictionary):
    """
    Construct a stroke for a target chord using a dictionary of known chord definitions.

    Args:
        target_chord (str): The target chord to construct a stroke for.
        chord_dictionary (dict): A dictionary of known chord definitions.

    Returns:
        str: The constructed stroke for the target chord.
    """

    # When the target chord is in the dictionary
    if target_chord in chord_dictionary:
        return chord_dictionary[target_chord]

    # When the target chord is made of two definitions that are in the dictionary
    for split_location in range(1, len(target_chord)):
        first_half = target_chord[:split_location]
        second_half = target_chord[split_location:]
        if first_half in chord_dictionary and second_half in chord_dictionary:
            return chord_dictionary[first_half] + chord_dictionary[second_half]

    # When the target chord is made of three definitions that are in the dictionary
    for split_location1 in range(1, len(target_chord)):
        for split_location2 in range(split_location1 + 1, len(target_chord)):
            first_half = target_chord[:split_location1]
            middle = target_chord[split_location1:split_location2]
            second_half = target_chord[split_location2:]
            if first_half in chord_dictionary and middle in chord_dictionary and second_half in chord_dictionary:
                return chord_dictionary[first_half] + chord_dictionary[middle] + chord_dictionary[second_half]

    # When the target chord is made of four definitions that are in the dictionary
    for split_location1 in range(1, len(target_chord)):
        for split_location2 in range(split_location1 + 1, len(target_chord)):
            for split_location3 in range(split_location2 + 1, len(target_chord)):
                first_half = target_chord[:split_location1]
                second_half = target_chord[split_location1:split_location2]
                third_half = target_chord[split_location2:split_location3]
                fourth_half = target_chord[split_location3:]
                if (first_half in chord_dictionary and second_half in chord_dictionary and 
                    third_half in chord_dictionary and fourth_half in chord_dictionary):
                    return (chord_dictionary[first_half] + chord_dictionary[second_half] + 
                            chord_dictionary[third_half] + chord_dictionary[fourth_half])

    # When the target chord is made of five definitions that are in the dictionary
    for split_location1 in range(1, len(target_chord)):
        for split_location2 in range(split_location1 + 1, len(target_chord)):
            for split_location3 in range(split_location2 + 1, len(target_chord)):
                for split_location4 in range(split_location3 + 1, len(target_chord)):
                    first_half = target_chord[:split_location1]
                    second_half = target_chord[split_location1:split_location2]
                    third_half = target_chord[split_location2:split_location3]
                    fourth_half = target_chord[split_location3:split_location4]
                    fifth_half = target_chord[split_location4:]
                    if (first_half in chord_dictionary and second_half in chord_dictionary and 
                        third_half in chord_dictionary and fourth_half in chord_dictionary and 
                        fifth_half in chord_dictionary):
                        return (chord_dictionary[first_half] + chord_dictionary[second_half] + 
                                chord_dictionary[third_half] + chord_dictionary[fourth_half] + 
                                chord_dictionary[fifth_half])

    # When the target chord is made of six definitions that are in the dictionary
    for split_location1 in range(1, len(target_chord)):
        for split_location2 in range(split_location1 + 1, len(target_chord)):
            for split_location3 in range(split_location2 + 1, len(target_chord)):
                for split_location4 in range(split_location3 + 1, len(target_chord)):
                    for split_location5 in range(split_location4 + 1, len(target_chord)):
                        first_half = target_chord[:split_location1]
                        second_half = target_chord[split_location1:split_location2]
                        third_half = target_chord[split_location2:split_location3]
                        fourth_half = target_chord[split_location3:split_location4]
                        fifth_half = target_chord[split_location4:split_location5]
                        sixth_half = target_chord[split_location5:]
                        if (first_half in chord_dictionary and second_half in chord_dictionary and 
                            third_half in chord_dictionary and fourth_half in chord_dictionary and 
                            fifth_half in chord_dictionary and sixth_half in chord_dictionary):
                            return (chord_dictionary[first_half] + chord_dictionary[second_half] + 
                                    chord_dictionary[third_half] + chord_dictionary[fourth_half] + 
                                    chord_dictionary[fifth_half] + chord_dictionary[sixth_half])

    # When the target chord is made of seven definitions that are in the dictionary
    for split_location1 in range(1, len(target_chord)):
        for split_location2 in range(split_location1 + 1, len(target_chord)):
            for split_location3 in range(split_location2 + 1, len(target_chord)):
                for split_location4 in range(split_location3 + 1, len(target_chord)):
                    for split_location5 in range(split_location4 + 1, len(target_chord)):
                        for split_location6 in range(split_location5 + 1, len(target_chord)):
                            first_half = target_chord[:split_location1]
                            second_half = target_chord[split_location1:split_location2]
                            third_half = target_chord[split_location2:split_location3]
                            fourth_half = target_chord[split_location3:split_location4]
                            fifth_half = target_chord[split_location4:split_location5]
                            sixth_half = target_chord[split_location5:split_location6]
                            seventh_half = target_chord[split_location6:]
                            if (first_half in chord_dictionary and second_half in chord_dictionary and 
                                third_half in chord_dictionary and fourth_half in chord_dictionary and 
                                fifth_half in chord_dictionary and sixth_half in chord_dictionary and 
                                seventh_half in chord_dictionary):
                                return (chord_dictionary[first_half] + chord_dictionary[second_half] + 
                                        chord_dictionary[third_half] + chord_dictionary[fourth_half] + 
                                        chord_dictionary[fifth_half] + chord_dictionary[sixth_half] + 
                                        chord_dictionary[seventh_half])

    # When the target chord is made of eight definitions that are in the dictionary
    for split_location1 in range(1, len(target_chord)):
        for split_location2 in range(split_location1 + 1, len(target_chord)):
            for split_location3 in range(split_location2 + 1, len(target_chord)):
                for split_location4 in range(split_location3 + 1, len(target_chord)):
                    for split_location5 in range(split_location4 + 1, len(target_chord)):
                        for split_location6 in range(split_location5 + 1, len(target_chord)):
                            for split_location7 in range(split_location6 + 1, len(target_chord)):
                                first_half = target_chord[:split_location1]
                                second_half = target_chord[split_location1:split_location2]
                                third_half = target_chord[split_location2:split_location3]
                                fourth_half = target_chord[split_location3:split_location4]
                                fifth_half = target_chord[split_location4:split_location5]
                                sixth_half = target_chord[split_location5:split_location6]
                                seventh_half = target_chord[split_location6:split_location7]
                                eighth_half = target_chord[split_location7:]
                                if (first_half in chord_dictionary and second_half in chord_dictionary and 
                                    third_half in chord_dictionary and fourth_half in chord_dictionary and 
                                    fifth_half in chord_dictionary and sixth_half in chord_dictionary and 
                                    seventh_half in chord_dictionary and eighth_half in chord_dictionary):
                                    return (chord_dictionary[first_half] + chord_dictionary[second_half] + 
                                            chord_dictionary[third_half] + chord_dictionary[fourth_half] + 
                                            chord_dictionary[fifth_half] + chord_dictionary[sixth_half] + 
                                            chord_dictionary[seventh_half] + chord_dictionary[eighth_half])

    # When the target chord is made of nine definitions that are in the dictionary
    for split_location1 in range(1, len(target_chord)):
        for split_location2 in range(split_location1 + 1, len(target_chord)):
            for split_location3 in range(split_location2 + 1, len(target_chord)):
                for split_location4 in range(split_location3 + 1, len(target_chord)):
                    for split_location5 in range(split_location4 + 1, len(target_chord)):
                        for split_location6 in range(split_location5 + 1, len(target_chord)):
                            for split_location7 in range(split_location6 + 1, len(target_chord)):
                                for split_location8 in range(split_location7 + 1, len(target_chord)):
                                    first_half = target_chord[:split_location1]
                                    second_half = target_chord[split_location1:split_location2]
                                    third_half = target_chord[split_location2:split_location3]
                                    fourth_half = target_chord[split_location3:split_location4]
                                    fifth_half = target_chord[split_location4:split_location5]
                                    sixth_half = target_chord[split_location5:split_location6]
                                    seventh_half = target_chord[split_location6:split_location7]
                                    eighth_half = target_chord[split_location7:split_location8]
                                    ninth_half = target_chord[split_location8:]
                                    if (first_half in chord_dictionary and second_half in chord_dictionary and 
                                        third_half in chord_dictionary and fourth_half in chord_dictionary and 
                                        fifth_half in chord_dictionary and sixth_half in chord_dictionary and 
                                        seventh_half in chord_dictionary and eighth_half in chord_dictionary):
                                        return (chord_dictionary[first_half] + chord_dictionary[second_half] + 
                                                chord_dictionary[third_half] + chord_dictionary[fourth_half] + 
                                                chord_dictionary[fifth_half] + chord_dictionary[sixth_half] + 
                                                chord_dictionary[seventh_half] + chord_dictionary[eighth_half] +
                                                chord_dictionary[ninth_half])






def lookup(strokes):
    output_string=""

    for stroke_number, stroke in enumerate(strokes):

        if stroke_number == 0:
            if not dedicated_key in stroke:
                stroke_valid = False
                for entry_stroke_category in entry_strokes.values():
                    if stroke in entry_stroke_category or strokes in entry_stroke_category:
                        stroke_valid = True
                if not stroke_valid:
                    raise KeyError
                if len(strokes)==1:
                    return '{Entered Shrimple}'
        else:
            if not dedicated_key in stroke:
                stroke_valid = False
                for entry_stroke_category in entry_strokes.values():
                    if stroke in entry_stroke_category:
                        stroke_valid = True
                if stroke_valid:
                    raise KeyError
        
        if stroke==dedicated_key:
            raise KeyError


        if stroke in strokes_you_can_use_to_exit_shrimple_with:
            raise KeyError



        if make_words_done_with_dedicated_key_exit_immediately and dedicated_key in strokes[0]:
            match = re.fullmatch(r'(F?S?C?Z?P?N?R?X?I?U?u?i?e?a?n?p?z?c?s?f?)', stroke.replace(dedicated_key,""))
            if stroke_number == 0 and not dedicated_key in stroke:
                raise KeyError
            elif not stroke_number == 0:
                raise KeyError
            
        #output_string+="hi "


    if (len(strokes)) == 1 and dedicated_key not in strokes[0]:
        if strokes[0]==entry_strokes['starterattached']:
            return ("{^}")
        else:
            return("{^ ^}")
        
        

    for stroke_number, stroke in enumerate(strokes):

        if ((not stroke_number == 0 and stroke in entry_strokes.values())
             or dedicated_key in stroke):
            raise KeyError
        
        match= re.fullmatch(
            r'(F?S?C?Z?P?N?R?X?I?U?u?i?e?a?n?p?z?c?s?f?)',

            #this string:
            stroke.replace(dedicated_key,""))

        if not match:
            raise KeyError
        
        stroke_output=construct_stroke(match[1], user_definitions)

        #do whatever checks you want here

        if ' ' in stroke_output:
            stroke_output = stroke_output.replace(" ","") + " "


        if not stroke_number==0 or (dedicated_key in strokes[0]):
            output_string+=stroke_output


    if strokes[0] in entry_strokes['starter cap']:
        return output_string.capitalize()
    if strokes[0] in entry_strokes["starter acronyms"]:
        return output_string.upper()
    if strokes[0] in entry_strokes['starter attached']:
        return "{^^}"+output_string
    if strokes[0] in entry_strokes['starter cap attached']:
        return "{^^}"+output_string.capitalize()
    if strokes[0] in entry_strokes['starter acronyms attached']:
        return "{^^}"+output_string.upper()
    return output_string




print(lookup(("PN", "PNen")))
print(lookup(("PN", "FCNRIUuiapcf")))
