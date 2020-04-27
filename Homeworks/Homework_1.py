from ast import literal_eval

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

with open("/home/lawih/zaine_academy/Homeworks/lista1") as file: 
  lines = file.readlines() 
  for line in lines: 
        print("{} {}".format(get_type(line),line)) 