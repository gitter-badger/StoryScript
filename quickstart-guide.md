---
description: StoryScript Quickstart Guide
---

# Quickstart Guide

Welcome to the StoryScript Quickstart guide. This guide is recommended for People who already familiar with Programming in Python or Other similar programming languages.

## Install Guide

To install StoryScript, First, download a Source code from the Main branch. Then, Install [python](https://www.python.org/downloads/release/python-395/). To ensure that everything works, You may need to download Python 3.9.5

## Arithmetic operators

These are all Arithmetic operators in StoryScript:

| Name | Sign |
| :--- | :--- |
| Add | + |
| Subtract | - |
| Multiply | \* |
| Divide | / |
| Modulo \(Find a remainder\) | % |
| Power | \*\* |

## Variables

Unlike Python, Variables are Strictly typed. For example:

```csharp
// Declare an Integer
int a = 10

// This will throws error
a = 3.14
```

These are all types currently available in StoryScript:

| Full Name | Alias used in the Language |
| :--- | :--- |
| Integer | int |
| Floating point number | float |
| Boolean value \(true/false\) | bool |
| List\* | list |
| Dictionary\* | dictionary |
| Tuple\* | tuple |
| Dynamic | dynamic |
| String | string |

\*This type is planned, But not implemented yet

### Setting symbol

To set a new value to a variable, You will need an equal \(=\) symbol for that. But there's more! Explore what are those here:

| Name | Symbol |
| :--- | :--- |
| Set | = |
| Multiply and set | \*= |
| Add and set | += |
| Subtract and set | -= |
| Divide and set | /= |
| Find remainder and set | %= |

### Variables naming rules

You can't declare a variable with a name with these violations:

1. Using StoryScript keyword
2. Starts with Digits
3. Using Type keyword
4. Function/Variable/Namespace name

StoryScript & Types keywords are:

```csharp
if, else, var, int, bool, float, exit
list, dictionary, tuple, const, override,
func, end, input, throw, string, typeof,
del, namespace, and, or, then, and "?"
```

And there might be more in the future, And There maybe a Custom type in The future.

## Loops

Currently, In StoryScript, There is only 1 loop. Which is "**loopfor loop"**. The loopfor loop in StoryScript is a Loop that loops for a specific number of times.  
For example:

```lua
loopfor 10
    print ("ping pong")
end
```

This piece of code, Will print "ping pong" 10 times.

## If statement

the If statement in StoryScript, Is in this format:

```lua
if condition then
    statements
end
```

### Conditions

Currently, In StoryScript, There are 6 Comparison symbol

| Name | Symbol |
| :--- | :--- |
| More than | &gt; |
| Less than | &lt; |
| Equal to | == |
| Not equal to | != |
| More than or Equal to | &gt;= |
| Less than or Equal to | &lt;= |

```lua
var a = 10
if a >= 5 then
    print ("a is more than or equal to 5")
end
```

To include multiple Statements, You'll need to add && sign. For example:

```lua
if a >= 5 then a = 10 && print ("a is more than or equal to 5 and its value is now changed to 10.")end
```

### Multiple Conditions

To use Multiple conditions in StoryScript, There are 2 keywords for you to use.

"and" and "or"

The keyword is pretty self-explanatory. "and" will check if both conditions is true.

And "or" will check if either one condition is true.

For example:

```lua
string userinput = input ()
if userinput == "I hate you" or input == "I don't like you" then
    print (";-;")
end
```

This code will check if the variable "userinput" is equal to "I hate you" **or** "I don't like you" If the condition was true, Print out ";-;"

### Else case

Else case is used to run code when the Condition in the If statement is not true.

For example:

```lua
float a = 3.14
if a == 4.13 then
    print ("a is Equal to 4.13")
else
    print ("a is not Equal to 4.13")
end
```

In this code, there is a variable called "a" which is set to 3.14.

If a is equal to 4.13, Then print "a is Equal to 4.13". Else, print "a is not equal to 4.13"

## Built-in Methods

In StoryScript, There are currently 3 built-in methods. Explore what are they here.

    input \(prompt: string: optional\)  
input\(\) is a method used to receive input through stdin.

    print \(message: any\)  
This will print out the message through stdout.

    exit \(code: any\)  
This will exit the program using the Code specified.

