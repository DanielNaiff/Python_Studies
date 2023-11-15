def notas(*n, sit=False):
  r = dict()
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['media'] = sum(n)/len(n)
  if sit:
    if r['media'] >= 7:
      r['situação'] = 'Boa'
    elif r['media'] >= 5:
      r['situação'] = 'Razoável'
    else:
      r['situação'] = 'Ruim'
  return r