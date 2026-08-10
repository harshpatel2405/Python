f = open("file4.txt", 'w')

characters =['Iron Man\n', 'Captain America\n', 'Thor\n', 'Hulk\n', 'Black Widow\n', 'Hawkeye\n']
f.writelines(characters)
f.close()

f = open("file4.txt",'r')

ans = f.readlines()

print(ans)

f.close()
