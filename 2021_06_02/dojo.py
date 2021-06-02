def main(s1, s2, s3):
    return fun(0,0,0,s1,s2,s3)

def fun(i1, i2, i3, s1, s2, s3):
    if  i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
        return True

    if i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3] and fun(i1 + 1, i2, i3 + 1, s1, s2, s3):
        return True

    if i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3] and fun(i1, i2 + 1, i3 + 1, s1, s2, s3):
        return True

    return False

# s1: aaca
# i1:     ^
   # s2: aba
# i2:    ^
   #
# s3: aabaaca
# i3:        ^

# 1. vamos andar por todos os índices do S3
#   a. Se não voltou atrás no passo anterior AND o char no apontador do S1
#       avança indice do S1 e do S3
#   b. Se o char no apontador do S2
#       avança indice do S2 e do S3
#   c.
#       volta atrás no S3 e no S1

# def reur(i1,i2,i3)
#     if xxx recur(i1+1, i2, i3+1)
#     elif xxx recur(i1, i2+1, i3+1)
#     else
#       return

