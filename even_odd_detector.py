while True:
 x = float(input('Enter integer to detect if it is even or odd x= '))
 a = int(x)
 b = float(x)
 if not a == b:
  print('Neither even nor odd (error: Number must be integar)')
  break
 elif a%2 == 0:
  print('even')
 else:
  print('odd')
  #JR
