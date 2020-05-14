class fs:
  def read(path, log):
    x = open(path,'r', encoding='utf-8')
    content = x.read()
    if log == True:
      print(content)
    elif log == False:
      return
    else:
      print(log, content)
    x.close()
  def write(content, path, filename):
    import os
    os.chdir(path)
    x = open(filename,'w+',encoding='utf-8')
    x.write(content)
    x.close()

class Player:
  def setusername(username):
    fs.write(username, './Data', 'username.txt')
  def username(shout):
    if shout == False:
      return
    elif shout == True:
      return
    else:
      fs.read('./Data/username.txt', shout)
    
class Game:
  def resume():
    fs.read('./Data/level.txt', 'U are on level')