import inspect
from sample_class import TaskManager

# Create object
task = TaskManager("Finish Lab", "Irene")

print("=== BASIC INFORMATION ===")
print("Class Name:", task.__class__.__name__)
print("Type:", type(task))

print("\n=== AVAILABLE MEMBERS ===")
members = dir(task)
for m in members:
    print(m)

print("\n=== CHECK METHOD EXISTENCE ===")
method_name = input("Enter method name to check: ")

if hasattr(task, method_name):
    print(f"{method_name} exists!")
    
    attr = getattr(task, method_name)
    
    if callable(attr):
        print(f"{method_name} is callable!")
        
        try:
            # Try calling method
            if method_name == "set_priority":
                result = attr("High")
            else:
                result = attr()
            print("Result:", result)
        except TypeError:
            print("Error: Method requires parameters.")
    else:
        print(f"{method_name} is NOT callable.")
else:
    print(f"{method_name} does NOT exist.")

print("\n=== SIGNATURE DETAILS ===")
try:
    sig = inspect.signature(task.display)
    print("display() signature:", sig)
except Exception as e:
    print("Could not get signature:", e)

print("\n=== SOURCE CODE ===")
try:
    source = inspect.getsource(TaskManager.display)
    print(source)
except:
    print("Source code not available.")