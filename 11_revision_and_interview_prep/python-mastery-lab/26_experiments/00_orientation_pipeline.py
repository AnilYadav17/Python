"""
Experiment 00: Source Code to Execution Pipeline & Runtime Inspection
======================================================================

Question Being Investigated:
----------------------------
What exact transformations occur to Python source code before the CPython
Virtual Machine executes it, and what runtime properties expose this process?

Hypothesis to Test:
-------------------
Python source code is not interpreted directly as text; it is tokenized,
parsed into an Abstract Syntax Tree (AST), compiled into an immutable Code Object
holding bytecode, and executed on a stack-based virtual machine frame.

Instructions to Run:
--------------------
$ python3 26_experiments/00_orientation_pipeline.py
"""

import ast
import dis
import io
import platform
import sys
import tokenize


def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def step_1_runtime_inspection() -> None:
    banner("1. RUNTIME & ENVIRONMENT INSPECTION")
    print(f"Implementation:       {sys.implementation.name}")
    print(f"Version:              {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"Platform:             {platform.platform()}")
    print(f"Byte Order:           {sys.byteorder} endian")
    print(f"Integer Precision:    Arbitrary (bignum)")
    print(f"Virtual Env Active:   {sys.prefix != sys.base_prefix}")
    print(f"sys.prefix:           {sys.prefix}")
    print(f"sys.base_prefix:      {sys.base_prefix}")


def step_2_lexing_and_tokenization(code_snippet: str) -> None:
    banner("2. LEXING & TOKENIZING (Source -> Tokens)")
    print(f"Source Code:\n  {code_snippet.strip()}\n")
    tokens = list(tokenize.tokenize(io.BytesIO(code_snippet.encode("utf-8")).readline))
    print(f"{'TYPE':<6} {'TOKEN NAME':<16} {'STRING VALUE':<20} {'LINE & COL'}")
    print("-" * 65)
    for tok in tokens:
        # Ignore initial encoding and endmarker for brevity
        if tok.type in (tokenize.ENCODING, tokenize.ENDMARKER):
            continue
        print(f"{tok.type:<6} {tokenize.tok_name[tok.type]:<16} {tok.string!r:<20} {tok.start}")


def step_3_ast_parsing(code_snippet: str) -> None:
    banner("3. PARSING (Tokens -> Abstract Syntax Tree)")
    parsed_tree = ast.parse(code_snippet)
    print("Hierarchical AST Dump:")
    print(ast.dump(parsed_tree, indent=2))


def step_4_bytecode_compilation(code_snippet: str) -> None:
    banner("4. COMPILATION (AST -> Code Object & Bytecode)")
    # compile(source, filename, mode) produces a types.CodeType object
    code_obj = compile(code_snippet, filename="<experiment>", mode="exec")

    print(f"Code Object Type:    {type(code_obj).__name__}")
    print(f"Constants (co_consts):    {code_obj.co_consts}")
    print(f"Names (co_names):         {code_obj.co_names}")
    print(f"Local Names (co_varnames):{code_obj.co_varnames}")
    print(f"Raw Bytecode (co_code):   {code_obj.co_code.hex(' ')}")
    print(f"Bytecode Length:          {len(code_obj.co_code)} bytes")


def step_5_bytecode_disassembly(code_snippet: str) -> None:
    banner("5. VIRTUAL MACHINE BYTECODE DISASSEMBLY (dis)")
    code_obj = compile(code_snippet, filename="<experiment>", mode="exec")
    dis.dis(code_obj)


def main() -> None:
    sample_code = "total = price * quantity\n"
    step_1_runtime_inspection()
    step_2_lexing_and_tokenization(sample_code)
    step_3_ast_parsing(sample_code)
    step_4_bytecode_compilation(sample_code)
    step_5_bytecode_disassembly(sample_code)

    banner("OBSERVATIONS & VERDICT")
    print(
        "1. Tokenization stripped white-space and identified 'total', '=', 'price', '*', 'quantity'.\n"
        "2. The AST structured this into an Assign node whose value is a BinOp (Mult).\n"
        "3. The Code Object compiled this into opcodes (LOAD_NAME, BINARY_OP, STORE_NAME).\n"
        "4. The stack VM evaluates this by pushing pointers to price and quantity, calling the\n"
        "   multiplication slot, and storing the pointer to the resulting object under 'total'.\n"
        "Hypothesis Confirmed: Python is a bytecode-compiled language executed via a Virtual Machine."
    )


if __name__ == "__main__":
    main()
