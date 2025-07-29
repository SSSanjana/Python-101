H = int(input("enter height: "))
C = int(input("enter credits: "))

if H>=137 and C>=10:
  print("Enjoy the ride!")
elif H<137 and C>=10:
  print("You are not tall enough to ride.")
elif H>=137 and C<10:
  print("You don't have enough credits.")
else:
  print("not met either requirement")
