# Naomi Tesla
# https://py.checkio.org/en/mission/conversion-into-camelcase/

def to_camel_case(name: str) -> str:
    if len(name) == 1:
        return name.upper()
    camel = name[0].upper() + name[1::]
    while camel.find('_') > -1:
        sub = camel[camel.index('_'):camel.index('_')+2]
        camel = camel.replace(sub, sub[1::].upper())
    return camel


assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"