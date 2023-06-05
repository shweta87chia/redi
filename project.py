responses =["welcome to smart calculator","my name is NIK","Thanks","sorry this is beyond my ability"]
def extract_number_from_text(text):
  l=[]
  for t in text.split(' '):
    try:
      l.append(float(t))
    except ValueError:
      pass