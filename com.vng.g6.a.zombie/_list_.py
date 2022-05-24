import dead_target.funcs as dtf

def all(dt):
     return [
         (dtf.exit, '\033[31mExit \033[0m'),
         (dtf.save, '\033[35mSave and Exit \033[0m'),
         (dtf.gold, 'Gold'),
         (dtf.cash, 'Cash'),
         (dtf.diamond, 'diamond'),
         (dtf.rank, f'Rank ( {dt.getRank()} )'),
         (dtf.grenate, f'Grenate ( {dt.getGrenate()} )'),
         (dtf.aidkit, f'Aidkit ( {dt.getAidkit()} )'),
         (dtf.NormalDronePart, f'Normal Drone Part ( {dt.getNormalDronePart()} )'),
         (dtf.SpecialDronePart, f'Special Drone Part ( {dt.getSpecialDronePart()} )'),
         (dtf.RaidBossTicket, f'Raid Boss Ticket ( {dt.getRaidBossTicket()} )'),
         (dtf.GunLevel, 'Gun Level'),
         (dtf.HandSkin, 'Hand Skins'),
         (dtf.GunSkin, 'Gun Skin'),
         (dtf.Mission, f'Mission ( {dt.getItem("curIndexMission")} )'),
         (dtf.Ads, 'Ads')
         
     ]

if __name__=='__main__':
        print('\nplease run one of these following command ...\n')
        print('1) sudo python main.py')
        print('      or           ')
        print('2) python main.py <Location of file of game data>\n')
        

