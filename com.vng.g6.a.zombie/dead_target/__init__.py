""" Biswajit Thakur """
import re
import urllib.parse
import xml.etree.ElementTree as ET

#___________________________________________________________
class load:
    #########################################################
    def __init__(self,pth):
          self.path = pth
          self.dead_target_tree = ET.parse(pth)
          self.dead_target_root = self.dead_target_tree.getroot()
    #########################################################
    def save(self):
        try:
           self.dead_target_tree.write(self.path)
           return True
        except:
           return False
    #########################################################
    def exit(self):
        import sys
        sys.exit()
    #########################################################
    def setItem(self,__taG,__attribVal,__datA):
       """ args setItem(self,__taG,__attribVal,__datA) """
       try:
          if 'string' == __taG:
               for data_ in self.dead_target_root.iter(__taG):
                     if __attribVal == data_.attrib.get('name'):
                          data_.text = urllib.parse.quote(str(__datA))
                          break
               else:
                    el = ET.Element(__taG)
                    el.set('name',__attribVal)
                    el.text = urllib.parse.quote(str(__datA))
                    self.dead_target_root.append(el)
          elif 'int' == __taG or 'float' == __taG:
                for data_ in self.dead_target_root.iter(__taG):
                     if __attribVal == data_.attrib.get('name'):
                           data_.set('value',str(__datA))
                           break
                     else:
                          el = ET.Element(__taG)
                          el.set('name',__attribVal)
                          el.set('value',str(__datA))
                          self.dead_target_root.append(el)
          return True
       except:
          return False
    #########################################################
    def getItem(self,__attribVal):
        """ args getItem(attrivute_value) """
        for d in self.dead_target_root.iter('string'):
            if __attribVal == d.attrib.get('name'):
                 return urllib.parse.unquote(d.text)
        for d_ in self.dead_target_root.iter('int'):
            if __attribVal==d_.attrib.get('name'):
                 return d_.attrib.get('value')
        for d_ in self.dead_target_root.iter('float'):
            if __attribVal==d_.attrib.get('name'):
                 return d_.attrib.get('value')
    #########################################################
    def getGunsNameList(self):
        """ return ['gunName_1','gunName_2',....,'gunName_n'] """
        return [ i[0] for i in re.findall(r'([\w\s]+)\|(\d+)\;\d+\;(.*?)\|',self.getItem('gunSkinData')) ]
    #########################################################
    def getGunsList(self):
        """ return [('gunName','code','skin'),(...),(...),....(...)] """
        return re.findall(r'([\w\s]+)\|(\d+)\;\d+\;(.*?)\|',self.getItem('gunSkinData'))
    #########################################################
    def getGunInfo(self,**NameOrCode):
       """ args Name=** or Code = ** 
       return type {'Name':str,'Code':int,'Skin':str} """
       for i in self.getGunsList():
           if (i[0]==NameOrCode.get('Name')) or (i[1]==str(NameOrCode.get('Code'))):
              return { 'Name' : i[0],'Code' : int(i[1]),'Skin' : i[2] }
    #########################################################
    def getInventoryInfo(self,**NameOrCode):
       """
       if args Name=str or Code=int
           return {'Name':str,'Code':int,'Skin':str,'Level':int}
       else
           return [{'Name':str,'Code':int,'Skin':str,'Level':int},{...},...]
       """
       gnLst = []
       for i in re.findall(r'(\d+)\|(\d+)\|',self.getItem('inventory')):
           k = self.getGunInfo(Code=int(i[0]))
           if(k.get('Code')==int(i[0])):
               k.update({'Level' : int(i[1])})
               gnLst.append(k)
       if NameOrCode.get('Code') or NameOrCode.get('Name'):
            for i in gnLst:
                if NameOrCode.get('Code') == i.get('Code') or NameOrCode.get('Name') == i.get('Name'):
                     return i
       else:
            return gnLst
    #########################################################
    def getGunLevel(self,**NameOrCode):
        """ args Name=str or Code=int
            return int or None
        """
        try:
            return self.getInventoryInfo(**NameOrCode).get('Level')
        except:
            return None
    #########################################################
    def getHandSkinsList(self):
        """ return hand skins set >>> {int, int, ...} """
        return { int(i) for i in re.findall(r'(\d+)\|',self.getItem('listHandSkin')) }
    #########################################################
    def setHandSkins(self,sknCode, *arg):
        """ args setHandSkins(sknCode) or setHandSkins(sknCode1,sknCode2,sknCode3,...) """
        hndSknLst = self.getHandSkinsList()
        if isinstance(sknCode, int):
             hndSknLst.add(int(sknCode))
        for i in arg:
            hndSknLst.add(int(i))
        d = ''
        for i in hndSknLst:
            d = f"{d}{i}|"
        return self.setItem('string', 'listHandSkin', d)
    #########################################################
    def setGunLevel(self,**NameOrCodeAndLevel):
         """ args Code=int or Name=str and Level=int """
         GunCode=self.getGunInfo(Name=NameOrCodeAndLevel.get('Name'),Code=NameOrCodeAndLevel.get('Code')).get('Code')
         gnLst = [ (int(i[0]), int(i[1])) for i in re.findall(r'(\d+)\|(\d+)\|',self.getItem('inventory'))]
         for i,j in enumerate(gnLst):
             if j[0] == GunCode:
                gnLst[i]=(j[0],NameOrCodeAndLevel.get('Level'))
                break
         else:
             gnLst.append((GunCode,NameOrCodeAndLevel.get('Level')))
         d=''
         for i in gnLst:
             d = f"{d}{i[0]}|{i[1]}|"
         return self.setItem('string','inventory',d)
    #########################################################
    def setGunSkin(self,**NameOrCodeAndSkin):
        """ args Name=str or Code=int and Skin=list """
        GunInf=self.getGunInfo(Name=NameOrCodeAndSkin.get('Name'),Code=NameOrCodeAndSkin.get('Code'))
        skns = { 1:{1:10},2:{1:5},3:{2:100},
                 4:{1:50},5:{5:400},7:{2:21},
                 8:{5:1500},9:{1:20},10:{4:250},
                11:{1:800},12:{7:5000},13:{6:10000},
                14:{2:1000},15:{1:600},16:{7:10000},
                18:{1:1857460}
                }
        skn2 = skns.get(GunInf.get('Code'),{})
        _skn_ = {int(i):int(j) for i,j in re.findall(r'(\d+):(\d+):',GunInf.get('Skin'))}
        for i in NameOrCodeAndSkin.get('Skin'):
            _skn_.update({i:skn2.get(i,1)})
        d=''
        for i in _skn_.items():
            d=f"{d}{i[0]}:{i[1]}:"
        dd=self.getGunsList()
        for i,j in enumerate(dd):
            if int(j[1])== GunInf.get('Code'):
                dd[i]=(GunInf.get('Name'),GunInf.get('Code'),d)
        ddd=''
        for i in dd:
            ddd=f"{ddd}{i[0]}|{i[1]};0;{i[2]}|"
        return self.setItem('string', 'gunSkinData', ddd)
    #########################################################
    def setRank(self,rnk):
        return self.setItem('int','levelQuestMission',int(rnk)) and self.setItem('int','level',int(rnk))
    #########################################################
    def getRank(self):
        return self.getItem('levelQuestMission')
    #########################################################
    def setLevel(self,rnk):
        return self.setRank(rnk)
    #########################################################
    def getLevel(self):
        return self.getRank()
    #########################################################
    def setGrenate(self,val):
        return self.setItem('int','grenadesCount',int(val))
    #########################################################
    def getGrenate(self):
        return self.getItem('grenadesCount')
    #########################################################
    def setAidkit(self,val):
        return self.setItem('int','aidKitCount',int(val))
    #########################################################
    def getAidkit(self):
        return self.getItem('aidKitCount')
    #########################################################
    def setNormalDronePart(self,val):
        return self.setItem('int','normalDronePart',int(val))
    #########################################################
    def getNormalDronePart(self):
        return self.getItem('normalDronePart')
    #########################################################
    def setSpecialDronePart(self,val):
        return self.setItem('int','specialDronePart',int(val))
    #########################################################
    def getSpecialDronePart(self):
        return self.getItem('specialDronePart')
    #########################################################
    def setRaidBossTicket(self,val):
        return self.setItem('int','raidbossPaidTicketCount',int(val))
    #########################################################
    def getRaidBossTicket(self):
        return self.getItem('raidbossPaidTicketCount')
    #########################################################
    
    #########################################################
    
    #########################################################
    
    