#쓰기모드
f = open('d:\javaedu9\project\python\sample.txt', 'w')
print(f.writable())
f.write('hello~ world~1\n')
f.close()

#추가모드
f = open('d:\javaedu9\project\python\sample.txt', 'a')
f.write('hello~ world~2\n')
f.write('hello~ world~3')
f.close()

#읽기모드
f = open('d:\javaedu9\project\python\sample.txt', 'r')
for line in f.readlines() :
    print(line.strip())
f.close()