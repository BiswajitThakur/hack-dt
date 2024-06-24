""" Biswajit Thakur """
import re
import sys


def save(dt):
      print('Data has been updated!') if dt.save() else print('Something went wrong!')
      sys.exit()

def exit(*dt):
      sys.exit()

coins = {
      0 : 'DvK5LA7yuSy3KEYityhGIg==',
      1 : 'g0ynEYJMpxEAMDYeATA2Hg==',
      10 : 'qFB8UaJQfFGkyCJRrsgiUQ==',
      100 : 'J0gtdENILXQq0WBgTtFgYA==',
      1000 : 'OFNJE9BQSRO8BZx1VAacdQ==',
      10000 : 'ri9ZN74IWTdHtLIFV5OyBQ==',
      100000 : 'fWAwGd3mMRnRlBUacRIUGg==',
      444000 : 'zYsXc61NEXNVn9tjNVndYw==',
      444444 : 'R1l4UluRflKyAUVMrslDTA==',
      1000000 : 'z4aBYY/EjmHbQ20bmwFiGw==',
      10000000 : 'TMJcBsxUxAZahlFT2hDJUw==',
      100000000 : '3JlBKNx4tC0Ev+UdBF4QGA==',
      999999999 : 'q64NfFRnl0dUnMIzq1VYCA==',
      1000000000 : 'oN+3DKAVLTfNQEQNzYreNg==',
      2000000000 : 'a8oOf2teOwhAFPdSQIDCJQ==',
      2119999999 : 'ardLYpUWFxz9XyoMAv52cg==',
      2147483647 : 'YfIvIp4N0F0XpFxX6FujKA=='
      }

def gold(dt):
      coins_ = [(i,j,coins.get(j)) for i,j in enumerate(coins.keys())]
      for i in coins_:
          print(f'( {i[0]+1} )==> {i[1]}')
      inp_coin = int(input('Select the number of Gold : '))-1
      if inp_coin in range(0,len(coins_)):
          for i in coins_:
              if inp_coin==i[0]:
                   dt.setItem('string', 'payMoney', i[2])
                       
      
def cash(dt):
      coins_ = [(i,j,coins.get(j)) for i,j in enumerate(coins.keys())]
      for i in coins_:
          print(f'( {i[0]+1} )==> {i[1]}')
      inp_coin = int(input('Select the number of Cash : '))-1
      if inp_coin in range(0,len(coins_)):
          for i in coins_:
              if inp_coin==i[0]:
                   dt.setItem('string', 'gameMoney', i[2])
                       
def diamond(dt):
      coins_ = [(i,j,coins.get(j)) for i,j in enumerate(coins.keys())]
      for i in coins_:
          print(f'( {i[0]+1} )==> {i[1]}')
      inp_coin = int(input('Select the number of Diamond : '))-1
      if inp_coin in range(0,len(coins_)):
          for i in coins_:
              if inp_coin==i[0]:
                   dt.setItem('string', 'diamond', i[2])
    

def rank(dt):
     print()
     dt.setRank(int(input('Enter the number of Rank or Level : ')))
     
def grenate(dt):
     print()
     dt.setGrenate(int(input('Enter the number of Grenate : ')))
     
def aidkit(dt):
     print()
     dt.setAidkit(int(input('Enter the number of Aidkit : ')))

def NormalDronePart(dt):
     print()
     dt.setNormalDronePart(int(input('Enter the number of Normal Drone Part : ')))

def SpecialDronePart(dt):
     print()
     dt.setSpecialDronePart(int(input('Enter the number of Special Drone Part : ')))

def RaidBossTicket(dt):
     print()
     dt.setRaidBossTicket(int(input('Enter the number of Raid Boss Ticket : ')))

def GunLevel(dt):
     gunsList = dt.getGunsNameList()
     print()
     print('\033[36m\t\t>> Gun Level hack <<\033[0m')
     for i,j in enumerate(gunsList):
         print(f'( {i+1} )==> {j} ( {dt.getGunLevel(Name=j)} )')
     print('---------------------------------------------------')
     inpGun = int(input('Select a option : '))-1
     lvl = int(input(f'( {gunsList[inpGun]} )==> Enter Level : '))
     dt.setGunLevel(Name=gunsList[inpGun], Level=lvl)

def HandSkin(dt):
     print()
     print('\033[36m\t\t>> Hand Skins hack <<\033[0m')
     print()
     print('+---------------------------------------------+')
     print('|    5         --> [ 5 ]                      |')
     print('| 3, 7, 8, 9   --> [ 3, 7, 8, 9 ]             |')
     print('| 3 ~ 8        --> [ 3, 4, 5, 6, 7, 8 ]       |')
     print('| 2, 4 ~ 7, 9  --> [ 2, 4, 5, 6, 7, 9 ]       |')
     print('+---------------------------------------------+')
     inpSkns = input('Enter the numbers of Hand Skins : ')
     r1= r'(\d+)\s*[\~\-\_]\s*(\d+)'
     while(re.search(r1,inpSkns)):
          a = re.search(r1,inpSkns)
          rx = f'({a.group(1)}\s*[\~\-\_]\s*({a.group(2)}))'
          b = list(range(int(a.group(1)),int(a.group(2))+1))
          c = ''
          for i in b:
              c = f'{c}{i},'
          inpSkns=re.sub(rx,c,inpSkns)
     k = [int(i) for i in re.findall(r'\d+',inpSkns)]
     dt.setHandSkins(*k)
     
def GunSkin(dt):
     print()
     print('\033[36m\t\t>> Gun Skins hack <<\033[0m')
     print()
     gunsList = dt.getGunsNameList()
     for i,j in enumerate(gunsList):
          print(f'( {i+1} )==> {j} ( {dt.getGunLevel(Name=j)} )')
     print('---------------------------------------------')
     inpGun = int(input('Select a option : '))-1
     print('+-------------------------------------------+')
     print('|    5         --> [ 5 ]                    |')
     print('| 3, 7, 8, 9   --> [ 3, 7, 8, 9 ]           |')
     print('| 3 ~ 8        --> [ 3, 4, 5, 6, 7, 8 ]     |')
     print('| 2, 4 ~ 7, 9  --> [ 2, 4, 5, 6, 7, 9 ]     |')
     print('+-------------------------------------------+')
     inpSkns = input(f'( {gunsList[inpGun]} )==> Enter Skins numbers : ')
     inpGun = gunsList[inpGun]
     r1= r'(\d+)\s*[\~\-\_]\s*(\d+)'
     while(re.search(r1,inpSkns)):
          a = re.search(r1,inpSkns)
          rx = f'({a.group(1)}\s*[\~\-\_]\s*({a.group(2)}))'
          b = list(range(int(a.group(1)),int(a.group(2))+1))
          c = ''
          for i in b:
              c = f'{c}{i},'
          inpSkns=re.sub(rx,c,inpSkns)
     k = [int(i) for i in re.findall(r'\d+',inpSkns)]
     dt.setGunSkin(Name=inpGun,Skin=k)
     
def Mission(dt):
     print()
     print('\033[36m\t\t>> Mission hack <<\033[0m')
     print()
     print(f' Current Mission : {dt.getItem("curIndexMission")}')
     print()
     i=int(input(' Enter the number of Mission : '))
     dt.setItem('int', 'curIndexMission', i)
     dt.setItem('string', 'dicMissionV2', f'15%7C{i}%7C2%7C15%7C')

def Ads(dt):
     print()
     print('\033[36m\t\t>> Ads hack <<\033[0m')
     print()
     print('( 1 )==> Remove Ads ')
     print('( 2 )==> Don\'t Remove Ads')
     i=int(input('Select a option : '))
     if i==1:
        print()
        print('Your selected option : 1')
        if re.search(r'\s*\'?\"?\s*(y|Y)\s*\'?\"?\s*',input('Enter \'y\' to continue... : ')):
           dt.setItem('float', 'purchasedMoney', '97.0')
     elif i==2:
        print()
        print('Your selected option : 2')
        if re.search(r'\s*\'?\"?\s*(y|Y)\s*\'?\"?\s*',input('Enter \'y\' to continue... : ')):
           dt.setItem('float', 'purchasedMoney', '0.0')
     ###


