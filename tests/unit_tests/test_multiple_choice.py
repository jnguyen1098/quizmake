# !/usr/bin/env python3
# pylint: skip-file

"""
Execute unit tests for the Question object.

Making sure that it parses correctly
"""

from quizmake import parser

CREATION_CASES = "tests/test_data/questions/unit_test_questions"
VALID_QUESTIONS = "tests/test_data/questions/valid_questions"

cases = [
    # fmt: off
    {
        "filename": CREATION_CASES + "/" + "case1.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "This is a question line."
            ],
            "answers": [
                "This is an answer line."
            ],
            "feedback": [
                "This is a feedback line.",
                "So is this."
            ],
        },
    },
    {
        "filename": CREATION_CASES + "/" + "case2.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "  Hello there.\n    This is a question on "
                "multiple lines.\n      hehe....\n\n"
            ],
            "answers": [
                "This is an answer line.",
                "That exists on multiple lines.",
                "Because sometimes we need...",
                "Multiple answers, no?",
            ],
            "feedback": [
                "This is a feedback line.",
                "So is this.",
                "asdf",
                "asdf",
                "asdf",
                "asdf",
                "asdf",
                "asdf",
                "asdf",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0001.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "Why does this program compile with warning(s)?\n"
                "\n#include <stdlib.h>\n\nint main"
                "(void)\n{\n    double {var} = {CUSTOM.random_digit}."
                "{CUSTOM.random_digit}{CUSTOM.random_digit};\n    "
                "printf(\"Hello world!\\n\");\n    return 0;\n}"
            ],
            "answers": [
                "The programmer didn't #include <stdio.h>",
                "The programmer should have used puts() instead",
                "There is nothing wrong with the program",
                "<stdlib.h> is deprecated (obsolete)",
            ],
            "feedback": [
                "Yup, you need this to call printf()",
                "Nope, puts() and printf() accomplish nearly the same thing in this context",
                "There certainly is something wrong with this program. Compile if you give up!",
                "<stdlib.h> is one of the most important libraries!",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0002.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "Trace this code and find the output.\n"
                "\n"
                "#include <stdio.h>\n"
                "#include <stdlib.h>\n"
                "#include <string.h>\n"
                "\n"
                "int main(void)\n"
                "{\n"
                "    char *{var1} = malloc(sizeof(char) * 512);\n"
                "    int {var2} = {digit1};\n"
                "    double {var3} = {digit_non_zero1}{digit_non_zero2}.{digit_non_zero3};\n"
                "\n"
                "    if ((int){var3} > {var2}) {\n"
                "        strcpy({var1}, \"{string1}\");\n"
                "    } else {\n"
                "        strcpy({var1}, \"{string2}\");\n"
                "    }\n"
                "\n"
                "    printf(\"%s\\n\", {var1});\n"
                "\n"
                "    return 0;\n"
                "}"
            ],
            "answers": [
                "{string1}",
                "{string2}",
                "{string}",
                "{string}",
            ],
            "feedback": [
                "Yes. {var3} is bigger than {var2} so \"{string1}\" is copied over.",
                "No. Trace again.",
                "Not even close.",
                "Not even close.",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0003.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "True or False:\n"
                "\n"
                "C uses dynamic type-checking (i.e. types are checked when you run the program, as opposed to when you compile it)"
            ],
            "answers": [
                "False",
                "True",
            ],
            "feedback": [
                "C actually uses static type-checking",
                "Think again.",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0004.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "Why won't this code compile?\n"
                "\n"
                "#include <{include1}>\n"
                "#include <{include2}>\n"
                "#include <{include3}>\n"
                "#include <{include4}>\n"
                "#include <{include5}>\n"
                "\n"
                "int main(void)\n"
                "{\n"
                "    char {var1}[] = \"{string}\";\n"
                "    printf(\"%s\\n\", {var1});\n"
                "    return 0\n"
                "}"
            ],
            "answers": [
                "The programmer forgot to put a semicolon on the return",
                "{var1} is incorrectly initialized",
                "#include <{include3}> is breaking gcc",
                "#include <{include4}> is breaking gcc",
            ],
            "feedback": [
                "Correct.",
                "{var1} is correctly initialized as a string",
                "The {include3} standard library won't break anything even if not used",
                "The {include4} standard library won't break anything even if not used",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0005.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "Say you want to dynamically allocate a 2D array of {type1}. Which would be the correct way to declare it?"
            ],
            "answers": [
                "{type1} **{var1};",
                "{type1} {var1};",
                "{type1} *{var1};",
                "{type1} ***{var1};",
            ],
            "feedback": [
                "Correct; you would need a pointer to a {type1} pointer.",
                "Incorrect. This only declares a single {type1}.",
                "Incorrect. This only creates a 1D array of {type1}.",
                "Incorrect. This creates a whopping 3D array of {type1}.",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0006.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "What will this program output?\n"
                "\n"
                "#include <stdio.h>\n"
                "#include <{include}>\n"
                "#include <{include}>\n"
                "\n"
                "int main(void)\n"
                "{\n"
                "    float {var1} = {digit1}.{digit2}{digit3};\n"
                "    printf(\"%f\\n\", {var1});\n"
                "    return 0;\n"
                "}"
            ],
            "answers": [
                "{digit1}.{digit2}{digit3}0000",
                "This program doesn't compile.",
                "{digit1}.{digit2}{digit3}",
                "{digit1}",
            ],
            "feedback": [
                "By default, the %f print specifier displays 6 significant digits",
                "Yes it does! It doesn't even carry any warnings",
                "Not entirely. Almost there.",
                "Nope; this is a float",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0007.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "Given the following makefile, how would you remove all compiled (not source) files?\n"
                "\n"
                "CC = gcc\n"
                "CFLAGS = -Wall -std=c99\n"
                "\n"
                "run:\n"
                "    ./a.out\n"
                "\n"
                "clean:\n"
                "    rm -rf *.o"
            ],
            "answers": [
                "make clean",
                "make run",
                "make all",
                "make",
            ],
            "feedback": [
                "Yes, 'clean' is customarily the name most people use for cleaning up",
                "No, this is for running the program",
                "No, this recipe doesn't even exist in the makefile. It would usually be used to make all of the program's object files and libraries though",
                "No, this defaults to the first recipe, which is 'run'",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0008.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "This program has a big flaw in it. Would this flaw be discovered at compile-time or run-time?\n"
                "\n"
                "#include <stdio.h>\n"
                "\n"
                "int main(void)\n"
                "{\n"
                "    char {var1}[] = \"{string1}\";\n"
                "    {var1}[{digit_non_zero1}{digit_non_zero2}{digit_non_zero3}] = '4';\n"
                "    printf(\"%s\\n\", {var1});\n"
                "    return 0;\n"
                "}"
            ],
            "answers": [
                "Because it is undefined behaviour, we don't actually know",
                "Run-time",
                "Compile-time",
            ],
            "feedback": [
                "Trick question, sorry. It depends on a few factors. The program may crash on startup, or the compiler might warn you. That's the thing about undefined behaviour: it's unpredictable.",
                "Not always.",
                "Not always.",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0009.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "Find the error in the code.\n"
                "\n"
                "#include <stdio.h>\n"
                "#include <stdlib.h>\n"
                "#include <string.h>\n"
                "\n"
                "int main(void)\n"
                "{\n"
                "    double {var1}[] = \"{string}\";\n"
                "    printf(\"%s\\n\", {var1});\n"
                "    return 0;\n"
                "}"
            ],
            "answers": [
                "double {var1}[] should be declared as char {var1}[] instead",
                "There is nothing wrong with the code",
                "You don't need to #include <stdio.h>",
                "This program should return something other than 0",
            ],
            "feedback": [
                "Yes, because we are initializing a string, we need a char array",
                "There totally is something wrong with this code",
                "You do. You need it to call print()",
                "0 is actually used to successful termination, so it's fine",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0010.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "True or False?\n"
                "\n"
                "A binary tree always has three leaf nodes, hence the name \"binary tree\"."
            ],
            "answers": [
                "False",
                "True",
            ],
            "feedback": [
                "Binary actually means \"two\", so three is indeed incorrect.",
                "Sorry but no.",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0011.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "How many times will \"{string1}\" print?\n"
                "\n"
                "#include <stdio.h>\n"
                "#include <sys/types.h>\n"
                "#include <unistd.h>\n"
                "\n"
                "int main(void)\n"
                "{\n"
                "    fork();\n"
                "    fork();\n"
                "    fork();\n"
                "    puts(\"{string1}\");\n"
                "    return 0;\n"
                "}"
            ],
            "answers": [
                "8 times",
                "3 times",
                "0 times",
                "1 time",
            ],
            "feedback": [
                "Correct; every instance of fork() will cause the next calls to occur twice, and the next ones to occur four times, etc; it's 2^(number of fork() calls)",
                "How many processes are there every time fork() is called?",
                "puts() is just as capable of printing \"{string1}\" as printf() is, so try again",
                "Try again.",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0012.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "Which of the following declarations refers to a pointer to a function that takes in a(n) {type1}, a(n) {type2} and returns a(n) {type3}?"
            ],
            "answers": [
                "{type3} (*{var1})({type2}, {type1});",
                "{type3} {var2}({type1}, {type2});",
                "{type4} {var3}({type1}, {type2});",
                "{type4} (*{var4})({type2}, {type1});",
            ],
            "feedback": [
                "Correct. Because of the asterisk's (*) low precedence, it is important to use parentheses to ensure correct operator precedence for {var1}.",
                "Incorrect. {var2} is just a function, not a function pointer.",
                "Incorrect. {var3} shouldn't return {type4}.",
                "Incorrect. Even though it *IS* a function pointer, it shouldn't return {type4}.",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0013.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": [
                "This program was supposed to sum up all the numbers in the array, but the programmer made a huge mistake. Correct the flawed line if possible.\n"
                "\n"
                "#include <stdio.h>\n"
                "\n"
                "int main(void)\n"
                "{\n"
                "    int {var1}[5] = {{digit_non_zero}{digit_non_zero}, {digit_non_zero}{digit_non_zero}, {digit_non_zero}{digit_non_zero}, {digit_non_zero}{digit_non_zero}, {digit_non_zero}{digit_non_zero}};\n"
                "\n"
                "    int {var3} = 0;\n"
                "\n"
                "    for (int {var2} = 0; {var2} <= sizeof({var1}); {var2}++) {\n"
                "        {var3} = {var3} + {var1}[{var2}];\n"
                "    }\n"
                "\n"
                "    return 0;\n"
                "}"
            ],
            "answers": [
                "for (int {var2} = 0; {var2} < sizeof({var1})/sizeof({var1}[0]); {var2}++)",
                "for (int {var2} = 0; {var2} < sizeof({var1}); {var2}++)",
                "This code runs fine.",
                "for (int {var2} = 0; {var2} < sizeof({var1}); {var2}--)",
            ],
            "feedback": [
                "Correct. sizeof({var1}) merely finds the total memory usage of the array, not the number of elements. By dividing it by the size of a single element, only then can we find the array's length.",
                "Incorrect. sizeof({var1}) on its own will only give you the array's size as a whole, not the number of elements.",
                "Clearly it doesn't.",
                "No, we start at index 0. If we go backwards, it's undefined behaviour."
            ],
        },
    },
    # fmt: on
]

"""
    {
        "filename": VALID_QUESTIONS + "/" + "q0001.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": "",
            "answers": [],
            "feedback": [],
        },
    },
"""

# TODO: move the bare questions in valid_questions/ to a dedicated mc folder
# add replacement cases
def test_mc_question_creation() -> None:
    """Assert the creation and return values of a Question."""
    for test_case in cases:
        question = parser.Question(str(test_case["filename"]))

        assert test_case["filename"] == question.filename
        assert question.type == test_case["question_type"]
        # Add case for checking number of feedback == number of answer

        sections = test_case["sections"]
        for key, value in sections.items():  # type: ignore
            assert question.sections[key] == value
