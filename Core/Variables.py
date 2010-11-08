# -*- coding: utf-8 -*-
## This file is part of HamsiManager.
## 
## Copyright (c) 2010 Murat Demir <mopened@gmail.com>      
##
## Hamsi Manager is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
## 
## Hamsi Manager is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with HamsiManager; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


import os, sys

class Variables():
    global checkMyObjects, checkStartupVariables, checkEncoding, getAvailablePlayers, getCharSets, getStyles, getScreenSize, getMyObjectsNames, isAvailablePyKDE4, getUserDesktopPath, getDefaultValues, getValueTypesAndValues, getKDE4HomePath, isAvailableKDE4, getSearchEnginesNames, getTaggersNames, getMyPluginsNames, getInstalledThemes, getInstalledLanguagesCodes, getInstalledLanguagesNames, isAvailableSymLink, getHashTypes, isRunableAsRoot, isRunningAsRoot
    global MQtGui, MQtCore, MyObjectName, isQt4Exist, defaultFileSystemEncoding, keysOfSettings, willNotReportSettings, mplayerSoundDevices, imageExtStringOnlyPNGAndJPG, windowModeKeys, tableTypeIcons, iconNameFormatKeys
    global osName, version, intversion, settingVersion, Catalog, aboutOfHamsiManager, HamsiManagerDirectory, executableHamsiManagerPath, userDirectoryPath, fileReNamerTypeNamesKeys, validSentenceStructureKeys, fileExtesionIsKeys, installedLanguagesCodes, installedLanguagesNames, libPath, getLibraryDirectoryPath
    MQtGui, MQtCore, isQt4Exist, MyObjectName = None, None, False, ""
    installedLanguagesCodes, installedLanguagesNames, libPath = None, None, None
    osName = os.name
    Catalog = "HamsiManager" 
    version = "0.9.08"
    intversion = 908
    settingVersion = "908"
    aboutOfHamsiManager = ""
    HamsiManagerDirectory = sys.path[0]
    executableHamsiManagerPath = str(sys.argv[0])
    userDirectoryPath = os.path.expanduser("~")
    defaultFileSystemEncoding = sys.getfilesystemencoding().lower()
    fileReNamerTypeNamesKeys = ["Personal Computer", "Web Server", "Removable Media"]
    validSentenceStructureKeys = ["Title", "All Small", "All Caps", "Sentence", "Don`t Change"]
    fileExtesionIsKeys = ["After The First Point", "After The Last Point"]
    mplayerSoundDevices = ["alsa", "pulse", "oss", "jack", "arts", "esd", "sdl", "nas", "mpegpes", "v4l2", "pcm"]
    imageExtStringOnlyPNGAndJPG = "(*.png *.jpg *.jpeg *.PNG *.JPG *.JPEG)"
    windowModeKeys = ["Normal", "Mini"]
    tableTypeIcons = ["folderTable.png", "fileTable.png", "musicTable.png", "subFolderTable.png", "cover.png"]
    iconNameFormatKeys = ["%Artist%", "%Album%", "%Year%", "%Genre%"]
    keysOfSettings = ["lastDirectory", "isMainWindowMaximized", "isShowAdvancedSelections", 
                  "isShowOldValues", "isRunOnDoubleClick", "isChangeSelected", 
                  "isChangeAll", "isOpenDetailsInNewWindow", "hiddenFolderTableColumns", 
                  "hiddenFileTableColumns", "hiddenMusicTableColumns", "hiddenSubFolderTableColumns", 
                  "hiddenCoverTableColumns", 
                  "isPlayNow", "MainWindowGeometries", "tableType", 
                  "activeTabNoOfSpecialTools", "unneededFiles", "ignoredFiles", 
                  "imageExtensions", "musicExtensions", "priorityIconNames", 
                  "unneededFileExtensions","ignoredFileExtensions", "fileReNamerType", 
                  "validSentenceStructure", 
                  "mplayerPath", "mplayerArgs", "mplayerAudioDevicePointer",
                  "mplayerAudioDevice", "isSaveActions", "fileSystemEncoding", 
                  "applicationStyle", "playerName", "isMinimumWindowMode", 
                  "packagerUnneededFileExtensions", "packagerUnneededFiles", "packagerUnneededDirectories", 
                  "lastUpdateControlDate", "updateInterval", 
                  "NeededObjectsName", "isActivePyKDE4", "isCloseOnCleanAndPackage", 
                  "TableToolsBarButtonStyle", "ToolsBarButtonStyle", "PlayerBarButtonStyle", 
                  "MusicOptionsBarButtonStyle", "SubDirectoryOptionsBarButtonStyle", 
                  "CoverOptionsBarButtonStyle",
                  "language", "isShowQuickMakeWindow", "isChangeExistIcon", 
                  "isClearFirstAndLastSpaceChars", "isEmendIncorrectChars", "validSentenceStructureForFile", 
                  "validSentenceStructureForFileExtension", "isCorrectFileNameWithSearchAndReplaceTable", 
                  "isCorrectDoubleSpaceChars", "fileExtesionIs", "settingsVersion", "subDirectoryDeep", 
                  "isMoveToTrash", "maxRecordFileSize", "themeName", 
                  "unneededDirectories", "ignoredDirectories", 
                  "unneededDirectoriesIfIsEmpty",  
                  "isClearEmptyDirectoriesWhenPath", "isAutoCleanSubFolderWhenPath", 
                  "cleanerUnneededFileExtensions", "cleanerUnneededFiles", "cleanerUnneededDirectories", 
                  "isClearEmptyDirectoriesWhenClear", "isAutoCleanSubFolderWhenClear", 
                  "isClearEmptyDirectoriesWhenSave", "isClearEmptyDirectoriesWhenMoveOrChange", 
                  "isClearEmptyDirectoriesWhenCopyOrChange", "isClearEmptyDirectoriesWhenFileMove", 
                  "isAutoCleanSubFolderWhenSave", "isAutoCleanSubFolderWhenMoveOrChange", 
                  "isAutoCleanSubFolderWhenCopyOrChange", "isAutoCleanSubFolderWhenFileMove", 
                  "isAutoMakeIconToDirectoryWhenSave", "isAutoMakeIconToDirectoryWhenMoveOrChange", 
                  "isAutoMakeIconToDirectoryWhenCopyOrChange", "isAutoMakeIconToDirectoryWhenFileMove", 
                  "isDeleteEmptyDirectories", 
                  "isCleanerDeleteEmptyDirectories", "isPackagerDeleteEmptyDirectories", 
                  "remindMeLaterForUpdate", "remindMeLaterShowDateForUpdate", 
                  "isShowTransactionDetails", "windowMode", "isInstalledKDE4Language", 
                  "isShowWindowModeSuggestion", "isMakeAutoDesign", "isShowReconfigureWizard", 
                  "isAskIfHasManyImagesInAlbumDirectory", "isDeleteOtherImages", 
                  "CoversSubDirectoryDeep", 
                  "amarokDBHost", "amarokDBPort", "amarokDBUser", 
                  "amarokDBPass", "amarokDBDB", "amarokIsUseHost", 
                  "iconNameFormat", "iconFileType", "pathOfMysqldSafe", 
                  "isActiveCompleter", "isShowAllForCompleter", "isActiveClearGeneral"
                  ]
    willNotReportSettings = ["amarokDBHost", "amarokDBPort", "amarokDBUser", 
                  "amarokDBPass", "amarokDBDB"]
    
    def checkMyObjects():
        global MQtGui, MQtCore, isQt4Exist, MyObjectName
        myObjectsNames = getMyObjectsNames()
        if myObjectsNames.count("PySide")>0:
            from PySide import QtCore
            sets = QtCore.QSettings((userDirectoryPath + "/.HamsiApps/HamsiManager/mySettings.ini").decode("utf-8") ,QtCore.QSettings.IniFormat)
            if str(sets.value("NeededObjectsName").toString())=="PySide":
                from PySide import QtGui
                from PySide import QtCore
                MyObjectName = "PySide"
        if MyObjectName=="" and myObjectsNames.count("PyQt4")>0:
            from PyQt4 import QtGui
            from PyQt4 import QtCore
            MyObjectName = "PyQt4"
        if MyObjectName=="":
            isQt4Exist = False
            return False
        MQtGui, MQtCore = QtGui, QtCore
        if MQtGui!=None and MQtCore!=None:
            isQt4Exist=True
            return True
        return False
    
    def checkStartupVariables():
        if checkMyObjects():
            checkEncoding()

    def checkEncoding(_isSetUTF8=False):
        global defaultFileSystemEncoding
        from encodings import aliases
        if [str(v).lower().replace("_", "-") for k, v in aliases.aliases.items()].count(defaultFileSystemEncoding)==0:
            if _isSetUTF8:
                defaultFileSystemEncoding = "utf-8"
            else:
                defaultFileSystemEncoding = sys.getdefaultencoding().lower()
                checkEncoding(True)
        
    def isAvailablePyKDE4():
        try:
            import PyKDE4
            return True
        except:
            return False
                   
    def isAvailableKDE4():
        import InputOutputs
        if InputOutputs.isFile("/usr/bin/kde4"):
            return True
        else:
            return False
            
    def isAvailableSymLink():
        try:
            from os import symlink
            return True
        except:
            return False
        
    def isRunableAsRoot():
        try:
            import InputOutputs
            if InputOutputs.isFile(getLibraryDirectoryPath() + "/kde4/libexec/kdesu"):
                if isRunningAsRoot():
                    return False
                return True
            return False
        except:
            return False
        
    def isRunningAsRoot():
        if userDirectoryPath=="/root":
            return True
        return False

    def getDefaultValues():
        from datetime import datetime
        if getInstalledLanguagesCodes().count(str(MQtCore.QLocale.system().name()))>0:
            insLangCode = str(MQtCore.QLocale.system().name())
        else:
            insLangCode = "en_GB"
        myStyle , PlayerName, myObjectsName = "Plastique", getAvailablePlayers().pop(), getMyObjectsNames()[0]
        for stil in MQtGui.QStyleFactory.keys():
            if stil == "Oxygen":
                myStyle = str(stil)
                break
        return {
                "lastDirectory": str(userDirectoryPath), 
                "isMainWindowMaximized": "False", 
                "isShowAdvancedSelections": "False", 
                "isShowOldValues": "False", 
                "isRunOnDoubleClick": "False", 
                "isChangeSelected": "False", 
                "isChangeAll": "True", 
                "isOpenDetailsInNewWindow": "False", 
                "hiddenFolderTableColumns": str([]), 
                "hiddenFileTableColumns": str([]), 
                "hiddenMusicTableColumns": str([]), 
                "hiddenSubFolderTableColumns": str([]), 
                "hiddenCoverTableColumns": str([]),
                "isPlayNow": "False", 
                "MainWindowGeometries": str([50, 50, 850, 533]), 
                "tableType": "2", 
                "activeTabNoOfSpecialTools": "0", 
                "unneededFiles": str(['Thumbs.db']), 
                "ignoredFiles": str(['.directory']), 
                "imageExtensions": str(['png', 'gif', 'jpeg', 'jpg']), 
                "musicExtensions": str(['mp3', 'ogg']), 
                "priorityIconNames": str(['cover']), 
                "unneededFileExtensions": str([]), 
                "ignoredFileExtensions": str(['m3u']), 
                "fileReNamerType": "Personal Computer", 
                "validSentenceStructure": "Title", 
                "mplayerPath": "mplayer", 
                "mplayerArgs": "-slave -quiet", 
                "mplayerAudioDevicePointer": "-ao",
                "mplayerAudioDevice": mplayerSoundDevices[0], 
                "isSaveActions": "True", 
                "fileSystemEncoding": defaultFileSystemEncoding, 
                "applicationStyle": myStyle, 
                "playerName": PlayerName, 
                "isMinimumWindowMode": "False", 
                "packagerUnneededFileExtensions": str(['pyc', 'py~', 'e4p', 'pro', 'pro.user', 'kdev4', 'kdevelop', 'kdevelop.pcs', 'kdevses', 'ts', 'anjuta']), 
                "packagerUnneededFiles": str(['.directory', '.project', '.bzrignore']), 
                "packagerUnneededDirectories": str(['.eric4project', '.svn', '.git', 'CVS', '.bzr', '.cache', '.settings']), 
                "lastUpdateControlDate": datetime.now().strftime("%Y %m %d %H %M %S"), 
                "updateInterval": "7", 
                "NeededObjectsName": myObjectsName, 
                "isActivePyKDE4": str(isAvailablePyKDE4()), 
                "isCloseOnCleanAndPackage": "True", 
                "TableToolsBarButtonStyle": "0", 
                "ToolsBarButtonStyle": "0", 
                "PlayerBarButtonStyle": "0", 
                "MusicOptionsBarButtonStyle": "0", 
                "SubDirectoryOptionsBarButtonStyle": "0",
                "CoverOptionsBarButtonStyle": "0",
                "language": insLangCode, 
                "isShowQuickMakeWindow": "True", 
                "isChangeExistIcon": "False", 
                "isClearFirstAndLastSpaceChars": "True", 
                "isEmendIncorrectChars": "True", 
                "validSentenceStructureForFile": "Title", 
                "validSentenceStructureForFileExtension": "All Small", 
                "isCorrectFileNameWithSearchAndReplaceTable": "True", 
                "isCorrectDoubleSpaceChars": "True", 
                "fileExtesionIs": "After The Last Point", 
                "settingsVersion": settingVersion,
                "subDirectoryDeep": "-1", 
                "isMoveToTrash": "False", 
                "maxRecordFileSize": "256", 
                "themeName": "Default", 
                "unneededDirectories": str([]),
                "ignoredDirectories": str([]), 
                "unneededDirectoriesIfIsEmpty": str([]), 
                "isClearEmptyDirectoriesWhenPath": "True", 
                "isAutoCleanSubFolderWhenPath": "True", 
                "cleanerUnneededFileExtensions": str(['pyc', 'py~', 'e4p', 'pro', 'pro.user', 'kdev4', 'kdevelop', 'kdevelop.pcs', 'kdevses', 'ts', 'anjuta']),
                "cleanerUnneededFiles": str(['.directory', '.project', '.bzrignore']),
                "cleanerUnneededDirectories": str(['.eric4project', '.svn', '.git', 'CVS', '.bzr', '.cache', '.settings']),
                "isClearEmptyDirectoriesWhenClear": "True",
                "isAutoCleanSubFolderWhenClear": "True", 
                "isClearEmptyDirectoriesWhenSave": "True", 
                "isClearEmptyDirectoriesWhenMoveOrChange": "True", 
                "isClearEmptyDirectoriesWhenCopyOrChange": "True", 
                "isClearEmptyDirectoriesWhenFileMove": "True", 
                "isAutoCleanSubFolderWhenSave": "True", 
                "isAutoCleanSubFolderWhenMoveOrChange": "True", 
                "isAutoCleanSubFolderWhenCopyOrChange": "True", 
                "isAutoCleanSubFolderWhenFileMove": "True", 
                "isAutoMakeIconToDirectoryWhenSave": "True", 
                "isAutoMakeIconToDirectoryWhenMoveOrChange": "True", 
                "isAutoMakeIconToDirectoryWhenCopyOrChange": "True", 
                "isAutoMakeIconToDirectoryWhenFileMove": "True", 
                "isDeleteEmptyDirectories": "True", 
                "isCleanerDeleteEmptyDirectories": "True", 
                "isPackagerDeleteEmptyDirectories": "True", 
                "remindMeLaterForUpdate": "-1", 
                "remindMeLaterShowDateForUpdate": datetime.now().strftime("%Y %m %d %H %M %S"), 
                "isShowTransactionDetails": "False", 
                "windowMode": windowModeKeys[0], 
                "isInstalledKDE4Language": "False", 
                "isShowWindowModeSuggestion": "True", 
                "isMakeAutoDesign": "True", 
                "isShowReconfigureWizard": "True", 
                "isAskIfHasManyImagesInAlbumDirectory": "True", 
                "isDeleteOtherImages": "False", 
                "CoversSubDirectoryDeep": "-1", 
                "amarokDBHost": "localhost", 
                "amarokDBPort": "3306", 
                "amarokDBUser": "amarokuser", 
                "amarokDBPass": "amarokpassword", 
                "amarokDBDB": "amarokdb", 
                "amarokIsUseHost": "False", 
                "iconNameFormat": "%Album%", 
                "iconFileType": "png", 
                "pathOfMysqldSafe": "mysqld_safe", 
                "isActiveCompleter": "True", 
                "isShowAllForCompleter": "True", 
                "isActiveClearGeneral": "False"
                }
                
    def getValueTypesAndValues():
        return {
                "lastDirectory": "str", 
                "isMainWindowMaximized": "bool", 
                "isShowAdvancedSelections": "bool", 
                "isShowOldValues": "bool", 
                "isRunOnDoubleClick": "bool", 
                "isChangeSelected": "bool", 
                "isChangeAll": "bool", 
                "isOpenDetailsInNewWindow": "bool", 
                "hiddenFolderTableColumns": ["intList", range(0, 2)], 
                "hiddenFileTableColumns": ["intList", range(0, 2)], 
                "hiddenMusicTableColumns": ["intList", range(0, 10)], 
                "hiddenSubFolderTableColumns": ["intList", range(0, 2)], 
                "hiddenCoverTableColumns": ["intList", range(0, 2)], 
                "isPlayNow": "bool", 
                "MainWindowGeometries": ["intStaticListLen", 4], 
                "tableType": ["int", range(0, 5)], 
                "activeTabNoOfSpecialTools": ["int", range(0, 5)], 
                "unneededFiles": "list", 
                "ignoredFiles": "list", 
                "imageExtensions": "list", 
                "musicExtensions": "list", 
                "priorityIconNames": "list", 
                "unneededFileExtensions": "list", 
                "ignoredFileExtensions": "list", 
                "fileReNamerType": ["options", fileReNamerTypeNamesKeys], 
                "validSentenceStructure": ["options", validSentenceStructureKeys], 
                "mplayerPath": "str", 
                "mplayerArgs": "str", 
                "mplayerAudioDevicePointer": "str",
                "mplayerAudioDevice": ["options", mplayerSoundDevices], 
                "isSaveActions": "bool", 
                "fileSystemEncoding": ["options", getCharSets()], 
                "applicationStyle": ["options", getStyles()], 
                "playerName": ["options", getAvailablePlayers()], 
                "isMinimumWindowMode": "bool", 
                "packagerUnneededFileExtensions": "list", 
                "packagerUnneededFiles": "list", 
                "packagerUnneededDirectories": "list", 
                "lastUpdateControlDate": "date", 
                "updateInterval": ["int", range(0, 32)], 
                "NeededObjectsName": ["options", getMyObjectsNames()], 
                "isActivePyKDE4": "bool", 
                "isCloseOnCleanAndPackage": "bool", 
                "TableToolsBarButtonStyle": ["int", range(0, 4)], 
                "ToolsBarButtonStyle": ["int", range(0, 4)], 
                "PlayerBarButtonStyle": ["int", range(0, 4)], 
                "MusicOptionsBarButtonStyle": ["int", range(0, 4)], 
                "SubDirectoryOptionsBarButtonStyle": ["int", range(0, 4)], 
                "CoverOptionsBarButtonStyle": ["int", range(0, 4)], 
                "language": ["options", getInstalledLanguagesCodes()], 
                "isShowQuickMakeWindow": "bool", 
                "isChangeExistIcon": "bool", 
                "isClearFirstAndLastSpaceChars": "bool", 
                "isEmendIncorrectChars": "bool", 
                "validSentenceStructureForFile": ["options", validSentenceStructureKeys], 
                "validSentenceStructureForFileExtension": ["options", validSentenceStructureKeys], 
                "isCorrectFileNameWithSearchAndReplaceTable": "bool", 
                "isCorrectDoubleSpaceChars": "bool", 
                "fileExtesionIs": ["options", fileExtesionIsKeys], 
                "settingsVersion": ["options", [settingVersion]],
                "subDirectoryDeep": ["int", range(-1, 10)], 
                "isMoveToTrash": "bool", 
                "maxRecordFileSize": "int", 
                "themeName": ["options", getInstalledThemes()], 
                "unneededDirectories": "list", 
                "ignoredDirectories": "list", 
                "unneededDirectoriesIfIsEmpty": "list", 
                "isClearEmptyDirectoriesWhenPath": "bool", 
                "isAutoCleanSubFolderWhenPath": "bool", 
                "cleanerUnneededFileExtensions": "list",
                "cleanerUnneededFiles": "list",
                "cleanerUnneededDirectories": "list",
                "isClearEmptyDirectoriesWhenClear": "bool",
                "isAutoCleanSubFolderWhenClear": "bool", 
                "isClearEmptyDirectoriesWhenSave": "bool", 
                "isClearEmptyDirectoriesWhenMoveOrChange": "bool", 
                "isClearEmptyDirectoriesWhenCopyOrChange": "bool", 
                "isClearEmptyDirectoriesWhenFileMove": "bool", 
                "isAutoCleanSubFolderWhenSave": "bool", 
                "isAutoCleanSubFolderWhenMoveOrChange": "bool", 
                "isAutoCleanSubFolderWhenCopyOrChange": "bool", 
                "isAutoCleanSubFolderWhenFileMove": "bool", 
                "isAutoMakeIconToDirectoryWhenSave": "bool", 
                "isAutoMakeIconToDirectoryWhenMoveOrChange": "bool", 
                "isAutoMakeIconToDirectoryWhenCopyOrChange": "bool", 
                "isAutoMakeIconToDirectoryWhenFileMove": "bool", 
                "isDeleteEmptyDirectories": "bool", 
                "isCleanerDeleteEmptyDirectories": "bool", 
                "isPackagerDeleteEmptyDirectories": "bool", 
                "remindMeLaterForUpdate": ["int", range(-1, 7)], 
                "remindMeLaterShowDateForUpdate": "date", 
                "isShowTransactionDetails": "bool", 
                "windowMode": ["options", windowModeKeys], 
                "isInstalledKDE4Language": "bool", 
                "isShowWindowModeSuggestion": "bool", 
                "isMakeAutoDesign": "bool", 
                "isShowReconfigureWizard": "bool", 
                "isAskIfHasManyImagesInAlbumDirectory": "bool", 
                "isDeleteOtherImages": "bool", 
                "CoversSubDirectoryDeep": ["int", [ x for x in range(-1, 10) if x!=0 ]], 
                "amarokDBHost": "str", 
                "amarokDBPort": "int", 
                "amarokDBUser": "str", 
                "amarokDBPass": "str", 
                "amarokDBDB": "str", 
                "amarokIsUseHost": "bool", 
                "iconNameFormat": "str", 
                "iconFileType": ["options", ["png", "jpg"]], 
                "pathOfMysqldSafe": "str", 
                "isActiveCompleter": "bool", 
                "isShowAllForCompleter": "bool", 
                "isActiveClearGeneral": "bool"
                }

    def getAvailablePlayers():
        playerNames = ["Mplayer"]
        try:
            import tkSnack
            playerNames.append("tkSnack")
        except:pass
        try:
            from PySide.phonon import Phonon
            playerNames.append("Phonon (PySide)")
        except:pass
        try:
            from PyQt4.phonon import Phonon
            playerNames.append("Phonon")
        except:pass
        return playerNames
       
    def getCharSets():
        from encodings import aliases
        charSets = []
        for k, v in aliases.aliases.items():
            if charSets.count(v.replace("_", "-"))==0:
                charSets.append(v.replace("_", "-"))
        charSets.sort()
        return charSets
        
    def getStyles():
        styles = []
        for stil in MQtGui.QStyleFactory.keys(): 
            styles.append(str(stil))
        return styles
        
    def getScreenSize():
        import Universals
        if Universals.MainWindow!=None:
            return MQtGui.QDesktopWidget().screenGeometry()
        else:
            return None
        
    def getMyObjectsNames():
        myObjectsName = []
        try:
            import PyQt4
            myObjectsName.append("PyQt4")
        except:pass
#        try:
#            import PySide
#            myObjectsName.append("PySide")
#        except:pass
        return myObjectsName
        
    def getUserDesktopPath():
        import InputOutputs
        if isAvailablePyKDE4():
            from PyKDE4.kdeui import KGlobalSettings
            desktopPath = str(KGlobalSettings.desktopPath())
        elif isAvailableKDE4():
            import Execute
            desktopPath = Execute.getCommandResult(["kde4-config", "--userpath", "desktop"])[:-2]
        else:
            desktopNames = [str(MQtGui.QApplication.translate("Variables", "Desktop")), "Desktop"]
            for dirName in desktopNames:
                if InputOutputs.isDir(userDirectoryPath + "/" + dirName):
                    desktopPath = userDirectoryPath + "/" + dirName
                    break
                else:
                    desktopPath = userDirectoryPath
        return desktopPath
    
    def getKDE4HomePath():
        if isAvailableKDE4():
            try:
                if isAvailablePyKDE4():
                    from PyKDE4.kdecore import KStandardDirs
                    kdedirPath = str(KStandardDirs().localkdedir())
                    if kdedirPath[-1]=="/":
                        kdedirPath = kdedirPath[:-1]
                else:
                    import Execute
                    kdedirPath = Execute.getCommandResult(["kde4-config", "--localprefix"])[:-2]
                return kdedirPath
            except:pass
        import InputOutputs
        if InputOutputs.isDir(userDirectoryPath + "/.kde4/share/config"):
            return userDirectoryPath + "/.kde4"
        else:
            return userDirectoryPath + "/.kde"
        
    def getLibraryDirectoryPath():
        global libPath
        if libPath==None:
            if isAvailablePyKDE4():
                from PyKDE4 import pykdeconfig
                libPath = pykdeconfig._pkg_config["kdelibdir"]
            else:
                try:
                    import Execute
                    libPath = Execute.getCommandResult(["kde4-config", "--path", "lib"]).split(":")[1][:-2]
                except:
                    import InputOutputs
                    if InputOutputs.isDir("/usr/lib64"):
                        libPath = "/usr/lib64"
                    else: 
                        libPath = "/usr/lib"
        return libPath
                
    def getSearchEnginesNames():
        import InputOutputs
        engines = []
        for name in InputOutputs.readDirectoryAll(HamsiManagerDirectory+"/SearchEngines"):
            try:
                moduleName = name.split(".")[0]
                moduleNameExt = name.split(".")[1]
                if engines.count(moduleName)==0:
                    if name[:1] != "." and moduleName!="__init__" and ["py", "pyc", "pyd"].count(moduleNameExt)==1 and InputOutputs.isFile(HamsiManagerDirectory+"/SearchEngines/"+name):
                        engines.append(moduleName)
            except:pass
        return engines
    
    def getTaggersNames():
        import InputOutputs
        taggers = []
        for name in InputOutputs.readDirectoryAll(HamsiManagerDirectory+"/Taggers"):
            try:
                moduleName = name.split(".")[0]
                moduleNameExt = name.split(".")[1]
                if taggers.count(moduleName)==0:
                    if name[:1] != "." and moduleName!="__init__" and ["py", "pyc", "pyd"].count(moduleNameExt)==1 and InputOutputs.isFile(HamsiManagerDirectory+"/Taggers/"+name):
                        taggers.append(moduleName)
            except:pass
        return taggers
        
    def getMyPluginsNames():
        import InputOutputs
        plugins = []
        for name in InputOutputs.readDirectoryAll(HamsiManagerDirectory+"/MyPlugins"):
            if name[:1] != "." and InputOutputs.isDir(HamsiManagerDirectory+"/MyPlugins/"+name):
                plugins.append(name)
        return plugins
        
    def getInstalledThemes():
        import InputOutputs
        themes = []
        for name in InputOutputs.readDirectoryAll(HamsiManagerDirectory+"/Themes"):
            if name[:1] != "." and InputOutputs.isDir(HamsiManagerDirectory+"/Themes/"+name):
                themes.append(name)
        return themes
    
    def getInstalledLanguagesCodes():
        global installedLanguagesCodes
        if installedLanguagesCodes==None:
            import InputOutputs
            languages = []
            for name in InputOutputs.readDirectoryAll(HamsiManagerDirectory+"/Languages"):
                if InputOutputs.isFile(HamsiManagerDirectory+"/Languages/"+name) and name[-3:]==".qm":
                    langCode = name[-8:-3]
                    if languages.count(langCode)==0:
                        languages.append(langCode)
            if languages.count("en_GB")==0:
                languages.append("en_GB")
            installedLanguagesNames = languages
        return installedLanguagesNames
        
    def getInstalledLanguagesNames():
        global installedLanguagesNames
        if installedLanguagesNames==None:
            import InputOutputs
            languages = []
            for name in InputOutputs.readDirectoryAll(HamsiManagerDirectory+"/Languages"):
                if InputOutputs.isFile(HamsiManagerDirectory+"/Languages/"+name) and name[-3:]==".qm":
                    langCode = name[-8:-3]
                    if languages.count(str(MQtCore.QLocale.languageToString(MQtCore.QLocale(langCode).language())))==0:
                        languages.append(str(MQtCore.QLocale.languageToString(MQtCore.QLocale(langCode).language())))
            if languages.count("English")==0:
                languages.append("English")
            installedLanguagesNames = languages
        return installedLanguagesNames
        
    def getHashTypes():
        try:
            import hashlib
            return ["MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"]
        except:
            #for x < python 2.5
            hashTypes = []
            try:
                import md5
                hashTypes.append("MD5")
            except:pass
            try:
                import md5
                hashTypes.append("SHA1")
            except:pass
            return hashTypes

    
                
