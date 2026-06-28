import ast
import operator as op

operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}


def eval_node(node):
    if isinstance(node, ast.BinOp):
        left = eval_node(node.left)
        right = eval_node(node.right)
        operator_func = operators.get(type(node.op))
        if operator_func is None:
            raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        return operator_func(left, right)

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return operators[ast.USub](eval_node(node.operand))

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numeric constants are allowed")

    raise ValueError(f"Unsupported expression element: {type(node).__name__}")


def evaluate_expression(expression):
    parsed = ast.parse(expression, mode="eval")
    return eval_node(parsed.body)


def main():
    print("Simple Python calculator")
    print("Enter arithmetic expressions using +, -, *, /, %, **")
    print("Type 'q' or 'quit' to exit")

    while True:
        expression = input("calc> ").strip()
        if expression.lower() in {"q", "quit", "exit"}:
            break
        if not expression:
            continue

        try:
            result = evaluate_expression(expression)
            print(result)
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
