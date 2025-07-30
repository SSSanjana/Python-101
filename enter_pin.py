print("BANK OF SSS")

pin = int(input("enter your PIN: "))

while pin != 1234:
  pin = int(input("try again."))

if pin == 1234:
  print("PIN accepted.")
