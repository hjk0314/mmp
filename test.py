import maya.OpenMaya as om
import pymel.core as pm
import shutil
import codecs
import filecmp
import subprocess
import os


# pep8: 79 char line ==========================================================
# pep8: 72 docstring or comments line ==================================


class Sync():
    def __init__(self):
        self.main()


    def main(self) -> None:
        fullPath = pm.Env().sceneName()
        chk = self.nameRules(fullPath)
        if not chk:
            pass
        else:
            # dev: "Y:/proj/folder/mdl/dev/file_v0003.ma"
            # pub: "Y:/proj/folder/mdl/pub/file_v0003.ma"
            # v9999: "Y:/proj/folder/mdl/pub/file_v9999.ma"
            # abc: "Y:/proj/folder/mdl/pub/data/abc/file_v0003.abc"
            temp = self.makePath(
                fullPath, 
                dev=True, 
                pub=True, 
                v9999=True, 
                abc=True, 
            )
            dev, pub, v9999, abc = temp
            self.compareFiles(dev, pub, v9999)
            self.saveFiles()
            self.exportAbc(abc)


    def nameRules(self, fullPath: str) -> bool:
        dir = fullPath.split("/")
        name = os.path.splitext(fullPath)[0]
        ver = name.rsplit('_', 1)[-1]
        A = ("dev" or "pub") in dir
        B = ("mdl" or "ldv" or "rig") in dir
        C = len(ver) == 5
        D = ver.startswith('v')
        E = ver[1:].isdigit()
        result = A and B and C and D and E
        return result


    def info(self, fullPath: str, **kwargs: dict) -> list:
        # fullPath: "Y:/proj/folder/mdl/pub/scenes/file_v0011.ma"
        folder = fullPath.split("/")
        dir = os.path.dirname(fullPath)
        scn = os.path.basename(fullPath) 
        # nwe: Name Without Extension
        nwe, ext = os.path.splitext(scn)
        wip = [i for i in ["dev", "pub"] if i in folder][0]
        typ = [i for i in ["mdl", "ldv", "rig"] if i in folder][0]
        ver = nwe.split("_")[-1]
        # nwv: Name Without Version
        nwv = nwe.rsplit("_", 1)[0]
        if wip == 'dev':
            (dev, pub) = (dir, dir.replace("dev", "pub"))
        if wip == 'pub':
            (dev, pub) = (dir.replace("pub", "dev"), dir)
        abc = pub.replace('scenes', 'data/abc')
        # keys
        infoDict = {
            'dir': dir, # dir: "Y:/proj/folder/mdl/pub/scenes"
            'scn': scn, # scn: "file_v0011.ma"
            'nwe': nwe, # nwe: "file_v0011"
            'ext': ext, # ext: ".ma"
            'wip': wip, # wip: "pub"
            'typ': typ, # typ: "mdl"
            'ver': ver, # ver: "v0011"
            'nwv': nwv, # nwv: file_mdl
            'dev': dev, # dev: "Y:/proj/folder/mdl/dev"
            'pub': pub, # pub: "Y:/proj/folder/mdl/pub"
            'abc': abc # abc: "Y:/proj/folder/mdl/pub/data/abc"
        }
        result = [infoDict[i] for i in kwargs if kwargs[i]]
        return result


    def makePath(self):
        pass


    def compareFiles(self):
        pass


    def saveFiles(self):
        pass


    def exportAbc(self):
        pass


    # def openFolder(self):
    #     pass


    # def openText(self):
    #     pass


    # def writeText(self):
    #     pass
