#list creation
laptops = ["acer", "samsung", "apple"]

#list operations
print(len(laptops))

print(laptops.index("acer"))

laptops.append("microsoft")

print(laptops)

laptops.insert(1, "dell")

print(laptops)

#slicing

print(laptops[:2]) #first 2 elements

print(laptops[-1]) #last elemet

print(laptops[::-1]) #reverse

#adding two lists

laptops += ["mac book"]

print(laptops)