import maya.cmds as cmds
import maya.mel as mel
import check
import tools
import update


# 79 char line ================================================================
# 72 docstring or comments line ========================================


cmds.evalDeferred('createMenuBar()')
def createMenuBar():
    # Main menu #
    # gMW = pm.language.melGlobals["gMainWindow"]
    gMW = mel.eval("$tmpVar=$gMainWindow")
    menu_id = "hjk0314"
    menu_lbl = "mmp"
    if cmds.menu(menu_id, l=menu_lbl, exists=True, p=gMW):
        cmds.deleteUI(cmds.menu(menu_id, e=True, dai=True))
    mainMenu = cmds.menu(menu_id, l=menu_lbl, p=gMW, to=True)
    # Main menu end #
    #
    # Sub menu start #
    # Check
    cmds.menuItem(l="Check", subMenu=True, parent=mainMenu, tearOff=True)
    cmds.menuItem(l="Same Names", c=lambda x: check.sameName())
    cmds.menuItem(l="Bad Names", c=lambda x: check.badName())
    cmds.setParent("..", menu=True)
    # Tools
    cmds.menuItem(l="Tools", subMenu=True, p=mainMenu, to=True)
    cmds.menuItem(l="Export Shader to Json", c=lambda x: tools.abc())
    cmds.menuItem(l="Speed", c=lambda x: tools.speed())
    cmds.menuItem(l="Delete Vaccine", c=lambda x: tools.vaccine())
    cmds.menuItem(l="Bundangmain", c=lambda x: tools.bundangmain())
    cmds.menuItem(l="Unknown Plugins", c=lambda x: tools.delPlugin())
    cmds.setParent("..", menu=True)
    # Update
    cmds.menuItem(l="Update", subMenu=True, p=mainMenu, to=True)
    cmds.menuItem(l="Sync", c=lambda x: update.sync())
    cmds.setParent("..", menu=True)
    # Sub menu end #


# pep8: 79 char line ==========================================================
# pep8: 72 docstring or comments line ==================================

