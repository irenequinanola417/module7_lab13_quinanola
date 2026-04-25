# Lab 13: Reflection and Introspection Utility

## Description
This project is a Python inspection tool that analyzes a custom class called TaskManager. It uses reflection and introspection to examine attributes and methods at runtime.

## Inspection Techniques Used
- type()
- dir()
- hasattr()
- getattr()
- callable()
- inspect.signature()
- inspect.getsource()

## Dynamic Behavior
The program asks the user to input a method name. If the method exists and is callable, it runs the method dynamically using getattr().

## Reflection
Introspection helped the program discover and use object methods dynamically instead of hardcoding them. This can be useful in debugging tools, frameworks, and plugin systems. The most challenging part was handling methods with parameters when calling them dynamically.