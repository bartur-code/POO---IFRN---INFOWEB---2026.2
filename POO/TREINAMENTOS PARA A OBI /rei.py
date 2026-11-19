dicionario = {
    'a' : 'a', 'b' : 'bac', 'c' : 'cad', 'd' : 'def', 'e' : 'e', 'f' : 'feg', 'g' : 'geh', 'h': 'hij', 'i' : 'i', 'j' : 'jik', 'k' : 'kil', 'l' : 'lim', 'm' : 'mon', 'n' : 'nop', 'o' : 'o', 'p' : 'poq', 'q' : 'qor', 'r' : 'ros', 's' : 'sut', 't' : 'tuv', 'u' : 'u', 'v' : 'vuw', 'w' : 'wux', 'x' : 'xuy', 'y' : 'yuz', 'z' : 'zu'
}
p = input().lower()
for i in p: 
    print(dicionario[i], end = '')