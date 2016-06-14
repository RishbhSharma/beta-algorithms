#returns the sum of digits
#sod
#example sod(12345)=1+2+3+4+5=15 ; sod(1)=1 ; sod(5)=1 ; sod(12)=1+2
#the num should be of type of string

def sod(num):
  sum=0
  for digit in num:
    sum+=int(digit)
  return int(sum)

# IT CURRENTLY DOESN' WORK!
