# 📚 12_Learning_Resources: Master Guides, Cheat Sheets & MCQs

## Overview
This directory is a curated archive of high-value reference documents, comprehensive master guides, interview Q&A compendiums, and multiple-choice question (MCQ) practice sheets. These resources serve as offline companions for deep reading and revision.

---

## 🗂️ Resource Directory

### 1. 📖 Books & Master Reference Guides (`books_and_guides/`)

| Resource | Format | Description |
|:---|:---:|:---|
| 📕 **Python & Data Types Master Guide** | PDF & HTML | Comprehensive illustrated deep dive into Python data types, memory layouts, mutability, and casting. Generated using `generate_guide_pdf.py`. |
| 📘 **OOPs Interview Questions & Answers** | PDF | Curated technical interview Q&A covering classes, inheritance, polymorphism, and abstraction. |
| 📙 **Python Boolean Logic Notes** | PDF | Truthy/falsy evaluation, short-circuit evaluation, logical expressions. |
| 📗 **LeetCode Array & String Roadmap** | PDF | Algorithmic roadmap outlining patterns for arrays and string problems. |
| 📄 **Array Questions** | PDF | 15 targeted coding challenge problems on arrays and matrices. |

---

### 2. 📝 Multiple Choice Question Sheets (`mcqs_and_practice_sheets/`)

MCQs are critical for university examinations, aptitude tests, and screening assessments:

#### 📁 `01_MCQS/` (Foundational Quizzes)
* `Python and its working.pdf` — Bytecode, virtual machines, interpreter mechanics.
* `python_keywords_identifiers_mcqs.pdf` — Naming rules, reserved keywords.
* `Topic_Input&Output.pdf` — `print()` parameters (`sep`, `end`), `input()` parsing.
* `Group5_Operators_MCQ.pdf` — Precedence, associativity, operator behaviors.
* `MCQ of membership and identity operator.pdf` — `in`, `not in`, `is`, `is not`.
* `Control Flow Statement.pdf` — Branching conditions.
* `LOOP MCQ.pdf` — Loop bounds, while/for loops.

#### 📁 `02_MCQS/` & `Practice_Sheets_Answers/` (Data Structures & Syntax Quizzes)
* `(1) Python_Ternary_MatchCase_MCQs(G1).pdf` *(Answered by `02_MCQS_Answers/1.py`)*
* `(2) String questions(2).pdf` *(Answered by `02_MCQS_Answers/2.py`)*
* `(3) String_Iteration_and_Immutability_20MCQs.pdf` *(Answered by `02_MCQS_Answers/3.py`)*
* `(4) python_string_quiz.pdf` *(Answered by `02_MCQS_Answers/4.py`)*
* `(5) Group5_List_Assignment(5).pdf` *(Answered by `02_MCQS_Answers/5.py`)*
* `(6) Python_List_Operations_Quiz_processed (1).pdf` *(Answered by `02_MCQS_Answers/6.py`)*
* `(7) Python_List_Comprehension_Quiz2.pdf` *(Answered by `02_MCQS_Answers/7.py`)*
* `(8) tuple_namedtuple_mcq.pdf` *(Answered by `02_MCQS_Answers/8.py`)*

#### 📁 `String Questions/`
* `Technical_String_151.pdf` & `Technical_String_Practice_150s.pdf` — 150 technical string algorithmic problems with code answers in `Answers/`.

---

## 🛠️ How to Generate PDF Guides

The repository includes a custom PDF compilation script in `books_and_guides/generate_guide_pdf.py` using **WeasyPrint** to render publication-quality PDFs from HTML:

```bash
# Optional: Requires WeasyPrint (pip install weasyprint)
python3 12_learning_resources/books_and_guides/generate_guide_pdf.py
```

---

## Next Step

👉 Explore multi-file software projects in **[13_mini_projects](../13_mini_projects/)**!
