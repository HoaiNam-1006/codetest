import json
from collections import Counter

def def_word_cnt(str):
  counts = Counter(str.split())
  return counts

def write_json(counts, f_name):
  with open(f_name, 'w') as f:
    json.dump(counts, f)
def count(s):
  if s == 0: return 
  f_name=f"result_{s}.json"
  write_json(counts,f_name)
  count(s-1)
if __name__ == "__main__":
  str = input("Nhap vao mot chuoi:")
  counts = def_word_cnt(str)
  count(100)