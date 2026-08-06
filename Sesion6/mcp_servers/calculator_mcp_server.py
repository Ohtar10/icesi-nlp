from mcp.server.fastmcp import FastMCP
import ast
import operator as op

mcp = FastMCP("CalculadoraMCP", host="localhost", port=8080)

ALLOWED_BIN_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
}
ALLOWED_UNARY_OPS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}

def evaluate_expression(expression: str):
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_BIN_OPS:
            return ALLOWED_BIN_OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_UNARY_OPS:
            return ALLOWED_UNARY_OPS[type(node.op)](_eval(node.operand))
        raise ValueError("La expresión contiene operadores no soportados.")

    return _eval(ast.parse(expression, mode="eval"))

@mcp.tool()
def calculadora(expression: str) -> str:
    """Evalúa una expresión aritmética segura con +, -, *, /, %, ** y paréntesis."""
    result = evaluate_expression(expression)
    return f"Resultado exacto: {result}"

if __name__ == "__main__":
    # Servidor HTTP en el puerto 8080 para compatibilidad con Colab
    mcp.run(transport="streamable-http")
