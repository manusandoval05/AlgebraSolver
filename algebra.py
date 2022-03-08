import re

class AlgebraicExpression:
    def __init__(self, expression) -> None:
        self.expression = expression
        self.variables = set(re.findall(r"[a-zA-Z]", expression))
        self.tokens = []
        variable_index_map = {
            0: "coefficient",
            1: "variable",
            2: "exponent"
        }
        term_index_map = {
            0: "symbol", 
            1: "variables"
        }
        for term in re.findall(r"([+-])([^+-]+)", "".join(expression.split())): #Find all instances of characters that are separated by + or - (Algebraic term)
            term_dictionary = {
                "symbol": term[0], 
                "variables" : []
            }
            for variable_component in re.findall(r"(\d*)([a-zA-Z]?)\^?(\d*)", term[1])[:-1]: #Loop through variables slicing until the last element, since the regular expressions loops through the last char
                term_dictionary["variables"].append({
                    "coefficient": variable_component[0], 
                    "variable" : variable_component[1],
                    "exponent": variable_component[2]
                })
            self.tokens.append(term_dictionary)
        


#{term_index_map[index]: term if term in ("+", "-") else [{variable_index_map[index]: variable_component for index, variable_component in enumerate(variable_component_list)} for variable_component_list in re.findall(r"(\d*)([a-zA-Z]?)\^?(\d*)", term)] for index, term in enumerate(re.findall(r"([+-])([^+-]+)", "".join(expression.split())))}
