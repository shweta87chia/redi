responses =["welcome to smart calculator","my name is NIK","Thanks","sorry this is beyond my ability"]
def extract_number_from_text(text):
  l=[]
  for t in text.split(' '):
    try:
      l.append(float(t))
    except ValueError:
      pass
      return(l)

def lcm(a,b):
  l=a if a>b else b
  while l<a*b:
      if l%a==0 and l%b==0:
        return l
        l+=1
