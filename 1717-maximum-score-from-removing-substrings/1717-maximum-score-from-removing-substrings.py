class Solution:
 def maximumGain(_,s,x,y,c=0):
  for a,r in[('ab',x),('ba',y)][::-2*(x<y)+1]:
   e=1
   while e:c+=r*(e:=(len(s)-len(s:=s.replace(a,'')))>>1)
  return c