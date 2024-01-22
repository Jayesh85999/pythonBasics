f = open('roll', 'r')
print(f.read())
f.close()

print('------')

f = open('roll', 'a')
f.write('Now file has more content!!\n')
f.close()

print('------')
f = open('roll', 'r')
print(f.read())
f.close()