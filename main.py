#Quratul Ain
#July 2022
#list of colours

colours=["red","blue","green","black","white","pink","grey","purple","yellow","brown"]#list of 10 colours
for i in colours:
  print(i)
start=int(input("enter a starting number (0-4): "))
end=int(input("enter a number (5-9): "))
print(colours[start:end])