a = 468340976726457153752543329995929
b = 8259849439295832154416464663433529767284365818089985212729059591436589376622897804486145035259938387227350386062511037821081822522674264342233224751809991132130043304539333112473
c = 599533884777687896776005738659978075404416227379871730343634213152746766776753741738279860246291162932098104341810018762401600714179499797853539653
d = 467801993911057346969253632393329698441821925792111695787002567703451068793258021745557947676079828499403918483241873884718402
e = 62232491515607091882574410635924603070626544377175485625797
f = 11449921622079721154497199899966677907638995896622219388843656194870204440338362332943924986323117322375295462212094869620734133568
g = 12004657173391489668678522013941832147005954727556362660159637892443617
h = 97605290770725966021179803308812675106786783237939047196728424115618
i = 658276182003137496407122225948572028855537578591430853088767389706978810842887148339827707619843413107416738130721399425
j = 5689768398165682472981133878451278523009637608647762675604795738876774718113916506327804992150205611581315356832469416472592015530113139666919895048261416544213718823613767148595520981851577168
k = 23389779576526080530029005130016352147448857309113056992134835347034019051103908490247469955408778428975403650
l = 13598018856492162040239554477268290
m = 10428170087510142513003057669962087616734396610851957661841082666377879726632480951238815619001048548750831415087300271897784233814999629327476879216245414498
n = 189954522487449421655484950204552793156378655991620103560351499621355342751042138555767443588613298932785823641745089405770069301474379286748373195349960130064468846461053536824538649373075643864894720
o = 7531436383873795315009506236096188648036856522778750817396763797198414070984881727501992372613765176393353441442
p = 97492963263563915914862118965031170516265320350495554360202823079704930167534387030768610600709038629529451107411889363545151124179790653827479276545795576577539
def indiceFibo(valor):
  indice = 1
  n1 = 0
  n2 = 1
  res = 0
  while True:
    if valor == 0:
      print(0)
      break
    else:
      indice += 1
      t = n1 + n2
      n2 = t
      n1 = n2 - n1
      if t == valor:
        print(indice)
        break
indiceFibo(a)      
indiceFibo(b)
indiceFibo(c)
indiceFibo(d)
indiceFibo(e)
indiceFibo(f)
indiceFibo(g)      
indiceFibo(h)
indiceFibo(i)
indiceFibo(j)
indiceFibo(k)
indiceFibo(l)
indiceFibo(m)
indiceFibo(n)
indiceFibo(o)
indiceFibo(p)
