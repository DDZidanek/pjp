def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                output.append(top_token)
                top_token = stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    return output

def evaluate_rpn(rpn):
    stack = []
    
    for token in rpn:
        if token.isdigit():
            stack.append(int(token))
        else:
            try:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    if right == 0:
                        return "ERROR"
                    stack.append(int(left / right))
            except (IndexError, ValueError):
                return "ERROR"
    
    return stack[0] if len(stack) == 1 else "ERROR"

def evaluate_expression(expression):
    try:
        postfix = infix_to_postfix(expression)
        result = evaluate_rpn(postfix)
        return result
    except Exception as e:
        return "ERROR"

adjusted_inputs = [
    "2 * (3 + 5)",
    "15 / (7 - 2 ** 2)",
    "7 + 3 * (10 / (12 / (3 + 1) - 1))",
    "7 + 3 * (10 / ((12 / (3 + 1) - 1))"
]

adjusted_results = [evaluate_expression(expr) for expr in adjusted_inputs]
print(adjusted_results)
