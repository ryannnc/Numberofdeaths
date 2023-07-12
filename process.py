#Part1 get_values
def get_values(lod,k):
  list=[]
  for lists in lod:
    if lists.get(k) not in list:
      list.append(lists.get(k))
  return list

#Part1 sum_death_matches
def sum_death_matches(lod,tgt,k,v):
  list=[]
  for lists in lod:
    if(lists.get(k)==v):
      list.append(int(int(lists.get(tgt))))
  return sum(list)

#Part1 sum_death_matches_specific
def sum_death_matches_specific(lod,tgt,k,v,k2,v2):
  list=[]
  for lists in lod:
    if(lists.get(k)==v and lists.get(k2)==v2):
      list.append(int(int(lists.get(tgt))))
  return sum(list)

#Part1 dict_from_values
def dict_from_values(lod,k):
  out={}
  for lists in lod:
    if(lists.get(k,"none")!="none"):
      out[lists.get(k)]=0
  return out