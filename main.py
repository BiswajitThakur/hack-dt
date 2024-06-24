import os
import sys
import time

import dead_target
import _list_

_F_ = r'/data/data/com.vng.g6.a.zombie/shared_prefs/com.vng.g6.a.zombie.v2.playerprefs.xml'
_FilE_ = ''
if os.path.exists(_F_):
     _FilE_ = _F_
else:
     _FilE_ = sys.argv[1]

dt = dead_target.load(_FilE_)

def main():
     while True:
          os.system('clear')
          print()
          print("\033[36m\t\t>> Dead Target hack <<\033[0m")
          print()
          lsts = _list_.all(dt)
          for i,j in enumerate(lsts):
              print(f'( {i+1} )==> {j[1]}')
          inp = int(input('\n >>> Select a option : '))-1
          if inp in range(0,len(lsts)):
              lsts[inp][0](dt)
              time.sleep(1)
          else:
              dt.exit()

if __name__=='__main__':
         main()

