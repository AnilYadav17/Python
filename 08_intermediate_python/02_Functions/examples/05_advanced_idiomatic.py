"""
05_advanced_idiomatic.py
Demonstrates advanced functional patterns in Python:
- Partial function application with functools.partial
- Data transformation pipelines using functools.reduce
- Dispatch table pattern using functions as dictionary values
- Inspecting function closure cells
"""

import functools

# 1. Partial Function Application
def base_log(message, level="INFO", channel="syslog"):
    return f"[{channel.upper()}] [{level.upper()}]: {message}"

# Pre-bind arguments to create specialized, reusable functions
info_log = functools.partial(base_log, level="INFO")
error_log = functools.partial(base_log, level="ERROR", channel="alerts")


# 2. Functional Transformation Pipeline via functools.reduce
def compose(*functions):
    """Composes multiple single-argument functions: f(g(h(x)))"""
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


# 3. Dispatch Table Pattern (Replacing complex if-elif chains)
def action_create(payload):
    return f"Created resource: {payload['name']}"

def action_update(payload):
    return f"Updated resource id={payload['id']} with {payload['name']}"

def action_delete(payload):
    return f"Deleted resource id={payload['id']}"

DISPATCH_TABLE = {
    "CREATE": action_create,
    "UPDATE": action_update,
    "DELETE": action_delete,
}

def execute_action(action_type, payload):
    # Lookup handler function from table; fallback to error handler
    handler = DISPATCH_TABLE.get(action_type, lambda p: f"Unknown action: {action_type}")
    return handler(payload)


# 4. Inspecting Closure Cells
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # 'factor' is a free variable captured in closure
    return multiply


def main():
    print("--- 1. Partial Function Application ---")
    print(info_log("Server initialized on port 8000"))
    print(error_log("Database connection lost!"))

    print("\n--- 2. Functional Data Pipeline Composition ---")
    # Pipeline stages: strip -> lowercase -> replace hyphen with space
    pipeline = compose(
        lambda text: text.replace("-", " "),
        lambda text: text.lower(),
        lambda text: text.strip()
    )
    raw_input = "   API-GATEWAY-TIMEOUT-ERROR   "
    print(f"Raw Input: '{raw_input}'")
    print(f"Composed Result: '{pipeline(raw_input)}'")

    print("\n--- 3. Function Dispatch Table ---")
    print(execute_action("CREATE", {"name": "AuditLog"}))
    print(execute_action("UPDATE", {"id": 42, "name": "ArchivedLog"}))
    print(execute_action("PURGE", {"id": 42}))

    print("\n--- 4. Introspecting Closure Internal Cells ---")
    triple = make_multiplier(3)
    print(f"triple(10) = {triple(10)}")
    # Access cell object inside __closure__
    cell = triple.__closure__[0]
    print(f"Closure cell: {cell}, cell_contents: {cell.cell_contents}")

if __name__ == "__main__":
    main()
