""" TESTING CASES """
import unittest
from processor import execute, parse_file
from os import remove as delete_file
import sys

class TestReturnedValue(unittest.TestCase):
    def test_arithmatics(self):
        self.assertEqual(execute("// Arithmatics test"), None)
        self.assertEqual(execute("5 + 5 * 0"), 5)
        self.assertEqual(execute("10 + 20 * 2"), 50)

    def test_exceptions(self):
        self.assertEqual(execute("throw DivideByZeroException"), "DivideByZeroException: You cannot divide numbers with 0")
        self.assertEqual(execute("throw InvalidValue Description"), "InvalidValue: Description")
        self.assertEqual(execute('throw InvalidSyntax "You did something wrong!"'), "InvalidSyntax: You did something wrong!")
        self.assertEqual(execute('throw AlreadyDefined "This person is already defined."'), "AlreadyDefined: This person is already defined.")
        self.assertEqual(execute("throw NotImplementedException This feature is in Alpha. Please add a Alpha tester profile to use this Feature."), "NotImplementedException: This feature is in Alpha. Please add a Alpha tester profile to use this Feature.")
        self.assertEqual(execute("throw DivideByZeroException"), "DivideByZeroException: You cannot divide numbers with 0")
        self.assertEqual(execute("throw InvalidTypeException The input type cannot be an Iterable data."), "InvalidTypeException: The input type cannot be an Iterable data.")

    def test_variable(self):
        self.assertEqual(execute("int a = 10"), None)
        self.assertEqual(execute("print (a)"), "10")
        self.assertEqual(execute("a = 20"), None)
        self.assertEqual(execute("print (a)"), "20")
        self.assertEqual(execute("a += 10"), None)
        self.assertEqual(execute("print (a)"), "30")
        self.assertEqual(execute("a -= 20"), None)
        self.assertEqual(execute("print (a)"), "10")
        self.assertEqual(execute("a *= 10"), None)
        self.assertEqual(execute("print (a)"), "100")
        self.assertEqual(execute("a /= 10"), None)
        self.assertEqual(execute("print (a)"), "10")
        self.assertEqual(execute("a %= 2"), None)
        self.assertEqual(execute("print (a)"), "0")
        self.assertEqual(execute("a = 10"), None)
        self.assertEqual(execute("a %= 3"), None)
        self.assertEqual(execute("print (a)"), "1")
        self.assertEqual(execute("del a"), None)
        self.assertEqual(execute("print (a)"), "NotDefinedException: name 'a' is not defined")

    def test_input(self):
        with open("inputsim.txt", "w") as f:
            f.writelines(["This file is used for Simulating user input.\n"])
        sys.stdin = open("inputsim.txt", "r")
        self.assertEqual(execute("string e = input()"), None)
        self.assertEqual(execute("print (e)"), "This file is used for Simulating user input.")
        sys.stdin.close()
        sys.stdin = sys.__stdin__

    def test_loopfor(self):
        self.assertEqual(execute('loopfor 5 print ("tong") end'), None)

    def test_if_else(self):
        self.assertEqual(execute("int b = 10"), None)
        self.assertEqual(execute("if b == 10 then print (\"b is equal to 10\") end"), None)

    def test_switch_case(self):
        self.assertEqual(execute("float c = 20.0"), None)
        self.assertEqual(execute('switch c case 10.0 print ("The value of c is 10") break case 20.0 print ("The value of c is 20.") break end'), None)

    def test_ternary_operator(self):
        self.assertEqual(execute('int d = 10'), None)
        self.assertEqual(execute('? d >= 10 : print ("a is more than or equal to 10") : print ("a is less than 10") :'), None)

    def test_parse_file(self):
        with open("inputsim.txt", "w") as f:
            f.writelines(["Hello there\n"])
        sys.stdin = open("inputsim.txt", "r")
        try:
            parse_file("main.sts", "inputsim.txt", True), ["40"]
        except SystemExit:
            pass
        self.assertEqual(parse_file("", "inputsim.txt"), None)
        with open("test.sts", "w") as f:
            f.writelines(["var a = 10\n", 'print ("Hello there!")\n'])
        self.assertEqual(parse_file("test.sts", None, True), ["Hello there!"])
        delete_file("test.sts")
        sys.stdin.close()
        sys.stdin = sys.__stdin__

if __name__ == "__main__":
    unittest.main()
