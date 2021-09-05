def uni(n):

    if len(n)>=1 or len(n)<=100000:
            if n==' ':
                return -1 
            else:
                for i in n:
                    if n.count(i)==1:
                        return n.index(i)
                        break

            if len(set(n))!=len(n):
                return -1
    else:
        return -1

print(uni("yyatree"))
