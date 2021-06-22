---
description: StoryScript Quickstart Guide
---

# Quickstart Guide

Welcome to the StoryScript Quickstart guide. This guide is recommended for People who already familiar with Programming in Python or Other similar programming languages.

### Arithmetics

These are all Arithmetics in StoryScript:

| Name | Sign |
| :--- | :--- |
| Add | + |
| Subtract | - |
| Multiply | \* |
| Divide | / |
| Modulo | % |
| Power | \*\* |

### Variables

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

#### Setting symbol

To set a new value to a variable, You will need an equal \(=\) symbol for that. But there's more! Explore what are those here:

| Name | Symbol |
| :--- | :--- |
| Set | = |
| Multiply and set | \*= |
| Add and set | += |
| Subtract and set | -= |
| Divide and set | /= |
| Modulo-ing and set | %= |

#### Variables naming rules

You can't declare a variable with a name with these violations:

1. Using StoryScript keyword
2. Starts with Digits
3. Using Type keyword
4. Function/Variable/Namespace name

StoryScript & Types keywords are:

```csharp
if, else, var, int, bool, float,
list, dictionary, tuple, const, override,
func, end, input, throw, string, typeof,
del, namespace, and, or, then, and "?"
```

And there might be more in the future, And There maybe a Custom type in The future.

### Loops

Currently, In StoryScript, There is only 1 loop. Which is **loopfor loop**. The loopfor loop in StoryScript is a Loop that loops for a specific number of times.  
For example:

```lua
loopfor 10
    print ("ping pong")
end
```

This piece of code, Will print "ping pong" 10 times.

### If statement

the If statement in StoryScript, Is in this format:

```lua
if condition then
    statements
end
```

#### Conditions

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

### Ternary Operator

A Ternary operator is a Short form of If statement. For example:

```lua
int something = 10
if something >= 5 then
    print ("something is more than or equal to 5")
end
```

Can be transformed into this:

```c
int something = 10
? something >= 5 : print ("something is more than or equal to 5") : :
```

Its format is:

```c
? condition : If the condition was true : If the condition was false :
```

And you can use && sign to include multiple commands.  
For example:

```c
int owo = 10
? owo >= 10 : owo *= 20 && print ("owo is now multiplied by 20") : print ("owo value is not changed") :
```

This code, Will multiply owo by 20 and print "owo is now multiplied by 20" when owo is more than or equal to 10. Else will print "owo value is not changed"

### Switch case statement

In StoryScript, the Switch case statement is a Fast way to do simple checks. Its format are:

```csharp
switch variable/data:
    case conditions:
        statements
        break
    case default:
        (default case)
        break
end
```

Here's a little example of Switch case statement:

```csharp
switch a
    case 10:
        print ("The value of a is 10")
        break
    case 20:
        print ("The value of a is 20")
        break
    case default:
        print ("I don't know what's the value of a...")
        break
end
```



