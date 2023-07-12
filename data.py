import json
import csv
import urllib.request

#Part2 values_to_dict
def values_to_dict(keys,llv):
  out=[]
  for data in llv:
    temp={}
    for count in range(len(keys)):
      temp[keys[count]]=data[count]
    out.append(temp)
  return out

#Part2 load_csv
def load_csv(file):
  out=[]
  with open(file) as fp:
    reader=csv.reader(fp)
    header=next(reader)
    for list in reader:
      if(len(list)==len(header)):
        out.append(list)
  return out

#Part2 dict_to_list
def dict_to_list(lod,keys):
  out=[]
  for data in lod:
    temp=[]
    for key in keys:
      temp.append(data[key])
    out.append(temp)
  return out

#Part2 list_to_csv
def list_to_csv(file,llv):
  with open(file,'a') as fp:
    writer=csv.writer(fp)
    for word in llv:
      writer.writerow(word)

#Part 3  fix_date
def fix_date(str):
  out=[]
  str=str.rsplit("/")
  for x in range(len(str)-1):
    out.append(int(str[x]))
  return out

#Part 3  separate_dates
def separate_dates(lod,k):
  for count in range(len(lod)):
    temp=fix_date(lod[count][k])
    lod[count]["month"]=temp[0]
    lod[count]["day"]=temp[1]
  return lod

#Part 3  grab_json
def grab_json(url):
  response=urllib.request.urlopen(url)
  content=response.read().decode()
  return json.loads(content)

#Part 3  parse_numbers
def parse_numbers(lod,keys):
  for count in range(len(lod)):
    for key in keys:
      lod[count][key]=json.loads(lod[count][key])
  return lod

#Part 3  write_csv
def write_csv(lod,fname,keys):
  final=[keys]
  for count in range(len(lod)):
    temp=[]
    for key in keys:
      if(key in lod[count]):
        temp.append(lod[count][key])
    final.append(temp)
  list_to_csv(fname,final)

#Part 3  read_csv
def read_csv(file):
  data=[]
  with open(file) as fp:
    reader=csv.reader(fp)
    header=next(reader)
    for list in reader:
      data.append(list)
    out=values_to_dict(header,data)
  return out