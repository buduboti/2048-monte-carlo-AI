from ai import ai

n, m = 10, 10

f = open("test.txt", "r")
t = [[0 for x in range(n)] for y in range(m)]
for i in range(1, n):
    for j in range(1, m):
        t[i][j] = int(f.readline())

f.close()
e = 1

for i in range(1, n):
    for j in range(1, m):
        #print type(t[i][j])
        #print type(ai(i, j))
        t[i][j] = ai(i*10, j*2)
        print str(e) + ' = ' + str(t[i][j])
        e += 1

f = open("test.txt", "w")
f.write(n)
f.write(m)

for i in range(1, n):
    for j in range(1, m):
        f.write(t[i][j])

f.close()
