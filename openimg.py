img=(open('testimg.png', 'rb').read())
print img
for x in img:
    print(str(ord(x)).zfill(3))
