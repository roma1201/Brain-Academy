a = ['python', 'php', 'cpp','pascal']
len(a)
print(len(a))
def main():
    languages=['python', 'cpp', 'pascal', 'php']
strng='python', 'cpp', 'pascal', 'php'
for i in strng:
 print(i)

 
def to_set(lst):
    return set(lst)
lang=['python', 'cpp', 'python','php']
lang_set=set(lang)
res={}
for i in lang_set:
    res[i]=lang.count(i)
print(res)
