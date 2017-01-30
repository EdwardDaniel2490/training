a = ["4", "fizyuemlpwitpuv"]
b = ["4", "plowpceuctoiwuuqtynyeew"]
c = ["3", "jgybyimniupcyswhq"]
d = ["-3", "eofkokhfwzlaadbylom"]
e = ["-7", "mepcmyqhmnwsxfeyltywuyzv"]
f = ["-4", "eopbouqiaqoieoyq"]
g = ["3", "spalgudykofpyuyaptr"]
h = ["3", "ouiwopjauuqehwr"]
i = ["-1", "gomfplgiyymtzhpyilhildeu"]
j = ["6", "swipueocuhisgaizagjte"]
k = ["3", "airuyupstycpuirqfad"]
l = ["4", "fvioinddaeclbci"]
m = ["-8", "iykfwuwuwzirooheeqsaunfx"]
def girarString(entrada):
  texto1 = ""
  c = int(entrada[0])
  b = str(entrada[1])
  texto2 = ""
  if c > 1:
    for i in range(c, len(b)):
      texto1 += b[i]
    if texto1 in b:
      texto2 = b.replace(texto1, "")
    print(texto1 + texto2)
  elif c < 1:
    inicia = len(b) - abs(c)
    for i in range(inicia, len(b)):
      texto1 += b[i]
    if texto1 in b:
      texto2 = b.replace(texto1, "")
    print(texto1 + texto2)
girarString(a)
girarString(b)
girarString(c)
girarString(d)
girarString(e)
girarString(f)
girarString(g)
girarString(h)
girarString(i)
girarString(j)
girarString(k)
girarString(l)
girarString(m)
