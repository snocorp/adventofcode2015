import re

binary_pattern = r'([\da-z]+) ([A-Z]+) ([\da-z]+) -> ([a-z]+)'
unary_pattern = r'([A-Z]+) ([\da-z]+) -> ([a-z]+)'
direct_pattern = r'([\da-z]+) -> ([a-z]+)'

binary = re.compile(binary_pattern)
unary = re.compile(unary_pattern)
direct = re.compile(direct_pattern)

ops = {
    'AND': '&',
    'OR': '|',
    'NOT': '~',
    'LSHIFT': '<<',
    'RSHIFT': '>>'
}

reserved = {
    'as': 'as1',
    'if': 'if1',
    'in': 'in1',
    'is': 'is1'
}

output_wire = 'a'

out = open('output.py', 'w')

out.write("""
memo = {}
"""
)

def get_operand(operand_name):
    operand_name = reserved.get(operand_name, operand_name)
    try:
        operand = int(operand_name)
    except ValueError:
        operand = operand_name + '()'
    
    return operand

try:
    with open('input.txt', 'r') as f:
        for line in f:
            m = binary.match(line)
            if m:
                function_name = m.group(4)
                operator_name = m.group(2)
                left_operand_name = m.group(1)
                right_operand_name = m.group(3)
                
                function_name = reserved.get(function_name, function_name)
                
                operator = ops[operator_name]
                if not operator:
                    print 'Unknown operator: ' + operator_name
                    break
                
                left_operand = get_operand(left_operand_name)
                right_operand = get_operand(right_operand_name)
                
                out.write("""
def %s():
    if '%s' in memo:
        return memo['%s']
    val = %s %s %s
    memo['%s'] = val
    return val

""" % (function_name, function_name, function_name, left_operand, operator, right_operand, function_name)
                )
                continue
            
            m = unary.match(line)
            if m:
                function_name = m.group(3)
                operator_name = m.group(1)
                operand_name = m.group(2)
                
                function_name = reserved.get(function_name, function_name)
                
                operator = ops[operator_name]
                if not operator:
                    print 'Unknown operator: ' + operator_name
                    break
                
                operand = get_operand(operand_name)
                
                out.write("""
def %s():
    if '%s' in memo:
        return memo['%s']
    val = %s %s
    memo['%s'] = val
    return val

""" % (function_name, function_name, function_name, operator, operand, function_name)
                )
                continue
            
            m = direct.match(line)
            if m:
                function_name = m.group(2)
                operand_name = m.group(1)
                
                function_name = reserved.get(function_name, function_name)
                
                operand = get_operand(operand_name)
                
                out.write("""
def %s():
    if '%s' in memo:
        return memo['%s']
    val = %s
    memo['%s'] = val
    return val
""" % (function_name, function_name, function_name, operand, function_name)
                )
                continue
            
            print 'No match for line: ' + line

    out.write('\nprint str(%s())' % output_wire)

finally:
    out.close()