# # This file is part of HamsiManager.
# #
## Copyright (c) 2010 - 2013 Murat Demir <mopened@gmail.com>
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


from Core import Universals as uni
from Core.MyObjects import *
import FileUtils as fu
from Databases import sqlite, reFillDatabases, checkDatabases


def getSettings(_settingsFilePath):
    return MQtCore.QSettings(str(_settingsFilePath), MQtCore.QSettings.IniFormat)


def setting():
    return getSettings(fu.joinPath(fu.pathOfSettingsDirectory, uni.fileOfSettings))


def settingForPaths():
    return getSettings(fu.joinPath(fu.pathOfSettingsDirectory, "paths.ini"))


def universalSetting():
    return getSettings(fu.joinPath(fu.userDirectoryPath, ".HamsiApps", "universalSettings.ini"))


def checkSettings():
    if fu.isDir(fu.pathOfSettingsDirectory) == False:
        fu.makeDirs(fu.pathOfSettingsDirectory)
        reFillSettings()
        reFillDatabases()
    else:
        if fu.isFile(fu.joinPath(fu.pathOfSettingsDirectory, "database.sqlite")) == False:
            reFillDatabases()
        if fu.isFile(fu.joinPath(fu.pathOfSettingsDirectory, uni.fileOfSettings)) == False:
            reFillSettings()
        checkDatabases()


def saveUniversalSettings():
    from Core import Execute

    mySetting = universalSetting()
    keysOfUniversalSettings = ["HamsiManagerPath"]
    values = [Execute.findExecutablePath("HamsiManager")]
    for x, keyValue in enumerate(keysOfUniversalSettings):
        if trStr(mySetting.value(keyValue)) != values[x]:
            mySetting.setValue(keyValue, trQVariant(values[x]))


def getUniversalSetting(_key, _defaultValue):
    mySetting = universalSetting()
    value = str(trStr(mySetting.value(_key)))
    if value == "":
        value = _defaultValue
    return value


def setUniversalSetting(_key, _value):
    mySetting = universalSetting()
    mySetting.setValue(_key, trQVariant(_value))


def reFillSettings(_makeBackUp=False):
    if _makeBackUp:
        makeBackUp("Settings")
    mySetting = setting()
    mySetting.clear()


def emendValue(_keyOfSetting, _value, _defaultValue=None, _valueTypesAndValue=None):
    if _valueTypesAndValue == None:
        _valueTypesAndValue = getValueTypesAndValues()[_keyOfSetting]
    if _defaultValue == None:
        _defaultValue = getDefaultValues()[_keyOfSetting]
    if _valueTypesAndValue == "bool":
        try:
            eval(str(_value).title())
        except:
            return _defaultValue
    elif _valueTypesAndValue == "date":
        from datetime import datetime

        try:
            datetime.strptime(str(_value), "%Y %m %d %H %M %S")
        except:
            return _defaultValue
    elif _valueTypesAndValue == "list":
        try:
            value = "['"
            for x, ext in enumerate(uni.getListFromListString(_value)):
                if ext != "":
                    if x != 0:
                        value += "','"
                    value += ext
            value += "']"
            _value = value
        except:
            return _defaultValue
    elif _valueTypesAndValue == "int":
        try:
            int(_value)
        except:
            return _defaultValue
    elif _valueTypesAndValue[0] == "int":
        try:
            if _valueTypesAndValue[1].index(int(_value)) == -1:
                return _defaultValue
        except:
            return _defaultValue
    elif _valueTypesAndValue[0] == "intList":
        try:
            value = "['"
            for x, ext in enumerate(uni.getListFromListString(_value)):
                if ext != "":
                    if _valueTypesAndValue[1].index(int(ext)) != -1:
                        if x != 0:
                            value += "','"
                        value += ext
            value += "']"
            _value = value
        except:
            return _defaultValue
    elif _valueTypesAndValue[0] == "intOptions":
        try:
            if _valueTypesAndValue[1].index(int(_value)) == -1:
                return _defaultValue
        except:
            return _defaultValue
    elif _valueTypesAndValue[0] == "options":
        try:
            if _valueTypesAndValue[1].index(str(_value)) == -1:
                return _defaultValue
        except:
            return _defaultValue
    return _value


def reFillAll(_makeBackUp=False):
    if _makeBackUp:
        makeBackUp("All")
    reFillDatabases()
    reFillSettings()


def makeBackUp(_settingType="All", _backUpDirectory="BackUps", _newFileName="mirror"):
    files = []
    if _settingType == "database" or _settingType == "All":
        files.append("database.sqlite")
    if _settingType == "Settings" or _settingType == "All":
        files.append(uni.fileOfSettings)
    if fu.isDir(fu.joinPath(fu.pathOfSettingsDirectory, _backUpDirectory)) == False:
        fu.makeDirs(fu.joinPath(fu.pathOfSettingsDirectory, _backUpDirectory))
    isReturn = False
    for file in files:
        if _newFileName == "mirror":
            newFileName = file
        elif _newFileName == "random":
            isReturn = True
            import random

            while 1 == 1:
                newFileName = file[:file.find(".")] + "_" + str(random.randrange(0, 100000000)) + file[file.find("."):]
                if fu.isFile(fu.joinPath(fu.pathOfSettingsDirectory, _backUpDirectory, newFileName)) == False:
                    break
        else:
            newFileName = _newFileName
        if fu.isFile(fu.joinPath(fu.pathOfSettingsDirectory, _backUpDirectory, newFileName)):
            fu.removeFile(fu.joinPath(fu.pathOfSettingsDirectory, _backUpDirectory, newFileName))
        try:
            fu.copyFileOrDir(fu.joinPath(fu.pathOfSettingsDirectory, file),
                             fu.joinPath(fu.pathOfSettingsDirectory, _backUpDirectory, newFileName))
            if isReturn:
                return newFileName
        except: pass


def restoreBackUp(_settingType="All", _isMakeBackUp=True):
    files = []
    isSuccessfully = True
    if _settingType == "database" or _settingType == "All":
        files.append("database.sqlite")
    if _settingType == "Settings" or _settingType == "All":
        files.append(uni.fileOfSettings)
    for file in files:
        if _isMakeBackUp:
            oldInfo = fu.readFromFile(fu.joinPath(fu.pathOfSettingsDirectory, file))
        else:
            try:
                fu.removeFile(fu.joinPath(fu.pathOfSettingsDirectory, file))
            except: pass
        try:
            if fu.isFile(fu.joinPath(fu.pathOfSettingsDirectory, "BackUps", file)):
                fu.moveFileOrDir(fu.joinPath(fu.pathOfSettingsDirectory, "BackUps", file),
                                 fu.joinPath(fu.pathOfSettingsDirectory, file))
            else:
                isSuccessfully = False
        except: pass
        if _isMakeBackUp:
            fu.writeToFile(fu.joinPath(fu.pathOfSettingsDirectory, "BackUps", file), oldInfo)
    return isSuccessfully


def saveStateOfSettings(_file):
    from Core import MyConfigure

    newFile = makeBackUp("Settings", "SettingFiles", "random")
    info = MyConfigure.getConfiguredDesktopFileContent()
    newInfo = []
    for row in info.split("\n"):
        if row[:4] == "Exec":
            row = row + " -s SettingFiles" + fu.sep + newFile
        newInfo.append(row)
    info = ""
    for row in newInfo:
        info += row + "\n"
    fu.writeToFile(_file, info)


def openStateOfSettings(_file):
    from Core import Execute

    for rowNo, row in enumerate(fu.readLinesFromFile(_file)):
        if row[:5] == "Exec=":
            t = Execute.executeStringCommand(row[5:])
            getApplication().closeAllWindows()
            break


def updateOldSettings(_oldVersion, _newVersion):
    newSettingsKeys, changedDefaultValuesKeys = [], []
    try:
        oldVersion = int(_oldVersion)
    except:
        oldVersion = _newVersion
    if oldVersion < 1000:
        reFillAll(True)
        return newSettingsKeys, changedDefaultValuesKeys
    if oldVersion < 1081:
        newSettingsKeys = newSettingsKeys + ["isCheckUnSavedValues"]
    if oldVersion < 1082:
        con = sqlite.connect(fu.joinPath(fu.pathOfSettingsDirectory, "database.sqlite"))
        cur = con.cursor()
        cur.execute(str("ALTER TABLE searchAndReplaceTable RENAME TO tmpSearchAndReplaceTable;"))
        cur.execute(str(
            "CREATE TABLE searchAndReplaceTable ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'label' TEXT,'searching' TEXT,'replacing' TEXT,'intIsActive' INTEGER,'intIsCaseSensitive' INTEGER,'intIsRegExp' INTEGER);"))
        cur.execute(str(
            "INSERT INTO searchAndReplaceTable(label,searching,replacing,intIsActive,intIsCaseSensitive,intIsRegExp) SELECT searching,searching,replacing,intIsActive,intIsCaseSensitive,intIsRegExp FROM tmpSearchAndReplaceTable;"))
        cur.execute(str("DROP TABLE tmpSearchAndReplaceTable;"))
        con.commit()
        newSettingsKeys = newSettingsKeys + ["isCorrectValueWithSearchAndReplaceTable"]
    if oldVersion < 1170:
        newSettingsKeys = newSettingsKeys + ["maxDeletedDirectorySize"]
    if oldVersion < 1190:
        changedDefaultValuesKeys = changedDefaultValuesKeys + ["applicationStyle", "windowMode", "fileExtensionIs"]
    if oldVersion < 1371:
        changedDefaultValuesKeys = changedDefaultValuesKeys + ["fileExtensionIs"]
    if oldVersion < 1372:
        changedDefaultValuesKeys = changedDefaultValuesKeys + ["packagerUnneededDirectories",
                                                               "cleanerUnneededDirectories"]

    return newSettingsKeys, changedDefaultValuesKeys


def getKeysOfSettings():
    return ["lastDirectory", "isMainWindowMaximized", "isShowAdvancedSelections",
            "isRunOnDoubleClick", "isChangeSelected",
            "isChangeAll", "isOpenDetailsInNewWindow", "hiddenFolderTableColumns",
            "hiddenFileTableColumns", "hiddenMusicTableColumns", "hiddenSubFolderTableColumns",
            "hiddenCoverTableColumns", "hiddenAmarokMusicTableColumns", "hiddenAmarokCoverTableColumns",
            "hiddenAmarokArtistTableColumns", "hiddenAmarokCopyTableColumns", "hiddenSubFolderMusicTableColumns",
            "isPlayNow", "MainWindowGeometries", "tableType",
            "activeTabNoOfSpecialTools", "unneededFiles", "ignoredFiles",
            "imageExtensions", "musicExtensions", "priorityIconNames",
            "unneededFileExtensions", "ignoredFileExtensions", "fileReNamerType",
            "validSentenceStructure",
            "mplayerPath", "mplayerArgs", "mplayerAudioDevicePointer",
            "mplayerAudioDevice", "isSaveActions", "fileSystemEncoding",
            "applicationStyle", "playerName", "isMinimumWindowMode",
            "packagerUnneededFileExtensions", "packagerUnneededFiles", "packagerUnneededDirectories",
            "lastUpdateControlDate", "updateInterval",
            "isCloseOnCleanAndPackage",
            "TableToolsBarButtonStyle", "ToolsBarButtonStyle", "PlayerBarButtonStyle",
            "MusicOptionsBarButtonStyle", "SubDirectoryOptionsBarButtonStyle",
            "CoverOptionsBarButtonStyle", "AmarokMusicOptionsBarButtonStyle", "AmarokCopyOptionsBarButtonStyle",
            "language", "isShowQuickMakeWindow", "isChangeExistIcon",
            "isClearFirstAndLastSpaceChars", "isEmendIncorrectChars", "validSentenceStructureForFile",
            "validSentenceStructureForDirectory",
            "validSentenceStructureForFileExtension", "isCorrectFileNameWithSearchAndReplaceTable",
            "isCorrectValueWithSearchAndReplaceTable",
            "isCorrectDoubleSpaceChars", "fileExtensionIs", "settingsVersion", "subDirectoryDeep",
            "maxRecordFileSize", "themeName",
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
            "isActiveCompleter", "isShowAllForCompleter", "isActiveClearGeneral",
            "colorSchemes", "isActiveAutoMakeIconToDirectory",
            "isDontDeleteFileAndDirectory", "pathOfDeletedFilesAndDirectories",
            "isReadOnlyAmarokDB", "isReadOnlyAmarokDBHost", "isResizeTableColumnsToContents",
            "AmarokFilterAmarokCoverTable", "AmarokFilterAmarokCopyTable", "AmarokFilterArtistTable",
            "AmarokFilterAmarokMusicTable",
            "isAppendFileSizeToFileTree", "isAppendLastModifiedToFileTree",
            "isMusicTableValuesChangeInAmarokDB", "isSubFolderTableValuesChangeInAmarokDB",
            "isFileTableValuesChangeInAmarokDB", "isFolderTableValuesChangeInAmarokDB",
            "isSubFolderMusicTableValuesChangeInAmarokDB",
            "isShowHiddensInSubFolderTable", "isShowHiddensInFolderTable", "isShowHiddensInFileTable",
            "isShowHiddensInMusicTable", "isShowHiddensInCoverTable", "isShowHiddensInSubFolderMusicTable",
            "isShowHiddensInFileTree",
            "isDecodeURLStrings", "isCheckUnSavedValues", "isAutoSaveScripts", "maxDeletedDirectorySize"]


def getDefaultValues():
    from datetime import datetime

    if uni.getInstalledLanguagesCodes().count(str(MQtCore.QLocale.system().name())) > 0:
        insLangCode = str(MQtCore.QLocale.system().name())
    else:
        insLangCode = "en_GB"
    myStyle, PlayerName = "", uni.getAvailablePlayers().pop()
    if uni.isWindows: myStyle = "Plastique"
    return {
        "lastDirectory": str(fu.userDirectoryPath),
        "isMainWindowMaximized": "False",
        "isShowAdvancedSelections": "False",
        "isRunOnDoubleClick": "False",
        "isChangeSelected": "False",
        "isChangeAll": "True",
        "isOpenDetailsInNewWindow": "False",
        "hiddenFolderTableColumns": str([]),
        "hiddenFileTableColumns": str([]),
        "hiddenMusicTableColumns": str([]),
        "hiddenSubFolderTableColumns": str([]),
        "hiddenCoverTableColumns": str([]),
        "hiddenAmarokMusicTableColumns": str([]),
        "hiddenAmarokCoverTableColumns": str([]),
        "hiddenAmarokArtistTableColumns": str([]),
        "hiddenAmarokCopyTableColumns": str([]),
        "hiddenSubFolderMusicTableColumns": str([]),
        "isPlayNow": "False",
        "MainWindowGeometries": str([50, 50, 850, 533]),
        "tableType": "1",
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
        "mplayerAudioDevice": uni.mplayerSoundDevices[0],
        "isSaveActions": "True",
        "fileSystemEncoding": fu.defaultFileSystemEncoding,
        "applicationStyle": myStyle,
        "playerName": PlayerName,
        "isMinimumWindowMode": "False",
        "packagerUnneededFileExtensions": str(
            ['pyc', 'py~', 'e4p', 'pro', 'pro.user', 'kdev4', 'kdevelop', 'kdevelop.pcs', 'kdevses', 'ts', 'anjuta']),
        "packagerUnneededFiles": str(['.directory', '.project', '.bzrignore']),
        "packagerUnneededDirectories": str(['.eric4project', '.svn', '.git', 'CVS', '.bzr', '.cache', '.settings',
                                            '.idea']),
        "lastUpdateControlDate": datetime.now().strftime("%Y %m %d %H %M %S"),
        "updateInterval": "14",
        "isCloseOnCleanAndPackage": "True",
        "TableToolsBarButtonStyle": "0",
        "ToolsBarButtonStyle": "0",
        "PlayerBarButtonStyle": "0",
        "MusicOptionsBarButtonStyle": "0",
        "SubDirectoryOptionsBarButtonStyle": "0",
        "CoverOptionsBarButtonStyle": "0",
        "AmarokMusicOptionsBarButtonStyle": "0",
        "AmarokCopyOptionsBarButtonStyle": "0",
        "language": insLangCode,
        "isShowQuickMakeWindow": "True",
        "isChangeExistIcon": "False",
        "isClearFirstAndLastSpaceChars": "True",
        "isEmendIncorrectChars": "True",
        "validSentenceStructureForFile": "Title",
        "validSentenceStructureForDirectory": "Don`t Change",
        "validSentenceStructureForFileExtension": "All Small",
        "isCorrectFileNameWithSearchAndReplaceTable": "True",
        "isCorrectValueWithSearchAndReplaceTable": "True",
        "isCorrectDoubleSpaceChars": "True",
        "fileExtensionIs": "Be Smart",
        "settingsVersion": uni.settingVersion,
        "subDirectoryDeep": "-1",
        "maxRecordFileSize": "256",
        "themeName": "Default",
        "unneededDirectories": str([]),
        "ignoredDirectories": str([]),
        "unneededDirectoriesIfIsEmpty": str([]),
        "isClearEmptyDirectoriesWhenPath": "True",
        "isAutoCleanSubFolderWhenPath": "True",
        "cleanerUnneededFileExtensions": str(
            ['pyc', 'py~', 'e4p', 'pro', 'pro.user', 'kdev4', 'kdevelop', 'kdevelop.pcs', 'kdevses', 'ts', 'anjuta']),
        "cleanerUnneededFiles": str(['.directory', '.project', '.bzrignore']),
        "cleanerUnneededDirectories": str(['.eric4project', '.svn', '.git', 'CVS', '.bzr', '.cache', '.settings',
                                           '.idea']),
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
        "windowMode": uni.windowModeKeys[1],
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
        "isActiveClearGeneral": "False",
        "colorSchemes": "",
        "isActiveAutoMakeIconToDirectory": "True",
        "isDontDeleteFileAndDirectory": "False",
        "pathOfDeletedFilesAndDirectories": fu.joinPath(fu.userDirectoryPath, ".HamsiApps", "HamsiManager", "Deleted"),
        "isReadOnlyAmarokDB": "False",
        "isReadOnlyAmarokDBHost": "False",
        "isResizeTableColumnsToContents": "False",
        "AmarokFilterAmarokCoverTable": "",
        "AmarokFilterAmarokCopyTable": "",
        "AmarokFilterArtistTable": "",
        "AmarokFilterAmarokMusicTable": "",
        "isAppendFileSizeToFileTree": "True",
        "isAppendLastModifiedToFileTree": "False",
        "isMusicTableValuesChangeInAmarokDB": "False",
        "isSubFolderTableValuesChangeInAmarokDB": "False",
        "isFileTableValuesChangeInAmarokDB": "False",
        "isFolderTableValuesChangeInAmarokDB": "False",
        "isSubFolderMusicTableValuesChangeInAmarokDB": "False",
        "isShowHiddensInSubFolderTable": "False",
        "isShowHiddensInFolderTable": "False",
        "isShowHiddensInFileTable": "False",
        "isShowHiddensInMusicTable": "False",
        "isShowHiddensInCoverTable": "False",
        "isShowHiddensInSubFolderMusicTable": "False",
        "isShowHiddensInFileTree": "False",
        "isDecodeURLStrings": "True",
        "isCheckUnSavedValues": "False",
        "isAutoSaveScripts": "True",
        "maxDeletedDirectorySize": "2048"
    }


def getValueTypesAndValues(_isAfterDefineApplication=False):
    myStyleContent = "str"
    if _isAfterDefineApplication:
        myStyleContent = ["options", uni.getStyles()]
    return {
        "lastDirectory": "str",
        "isMainWindowMaximized": "bool",
        "isShowAdvancedSelections": "bool",
        "isRunOnDoubleClick": "bool",
        "isChangeSelected": "bool",
        "isChangeAll": "bool",
        "isOpenDetailsInNewWindow": "bool",
        "hiddenFolderTableColumns": ["intList", list(range(0, 2))],
        "hiddenFileTableColumns": ["intList", list(range(0, 2))],
        "hiddenMusicTableColumns": ["intList", list(range(0, 10))],
        "hiddenSubFolderTableColumns": ["intList", list(range(0, 2))],
        "hiddenCoverTableColumns": ["intList", list(range(0, 2))],
        "hiddenAmarokMusicTableColumns": ["intList", list(range(0, 10))],
        "hiddenAmarokCoverTableColumns": ["intList", list(range(0, 2))],
        "hiddenAmarokArtistTableColumns": ["intList", list(range(0, 2))],
        "hiddenAmarokCopyTableColumns": ["intList", list(range(0, 10))],
        "hiddenSubFolderMusicTableColumns": ["intList", list(range(0, 10))],
        "isPlayNow": "bool",
        "MainWindowGeometries": ["intStaticListLen", 4],
        "tableType": ["options", uni.tableTypesNames.keys()],
        "activeTabNoOfSpecialTools": ["int", list(range(0, 7))],
        "unneededFiles": "list",
        "ignoredFiles": "list",
        "imageExtensions": "list",
        "musicExtensions": "list",
        "priorityIconNames": "list",
        "unneededFileExtensions": "list",
        "ignoredFileExtensions": "list",
        "fileReNamerType": ["options", uni.fileReNamerTypeNamesKeys],
        "validSentenceStructure": ["options", uni.validSentenceStructureKeys],
        "mplayerPath": "str",
        "mplayerArgs": "str",
        "mplayerAudioDevicePointer": "str",
        "mplayerAudioDevice": ["options", uni.mplayerSoundDevices],
        "isSaveActions": "bool",
        "fileSystemEncoding": ["options", uni.getCharSets()],
        "applicationStyle": myStyleContent,
        "playerName": ["options", uni.getAvailablePlayers()],
        "isMinimumWindowMode": "bool",
        "packagerUnneededFileExtensions": "list",
        "packagerUnneededFiles": "list",
        "packagerUnneededDirectories": "list",
        "lastUpdateControlDate": "date",
        "updateInterval": ["int", list(range(0, 32))],
        "isCloseOnCleanAndPackage": "bool",
        "TableToolsBarButtonStyle": ["int", list(range(0, 4))],
        "ToolsBarButtonStyle": ["int", list(range(0, 4))],
        "PlayerBarButtonStyle": ["int", list(range(0, 4))],
        "MusicOptionsBarButtonStyle": ["int", list(range(0, 4))],
        "SubDirectoryOptionsBarButtonStyle": ["int", list(range(0, 4))],
        "CoverOptionsBarButtonStyle": ["int", list(range(0, 4))],
        "AmarokMusicOptionsBarButtonStyle": ["int", list(range(0, 4))],
        "AmarokCopyOptionsBarButtonStyle": ["int", list(range(0, 4))],
        "language": ["options", uni.getInstalledLanguagesCodes()],
        "isShowQuickMakeWindow": "bool",
        "isChangeExistIcon": "bool",
        "isClearFirstAndLastSpaceChars": "bool",
        "isEmendIncorrectChars": "bool",
        "validSentenceStructureForFile": ["options", uni.validSentenceStructureKeys],
        "validSentenceStructureForDirectory": ["options", uni.validSentenceStructureKeys],
        "validSentenceStructureForFileExtension": ["options", uni.validSentenceStructureKeys],
        "isCorrectFileNameWithSearchAndReplaceTable": "bool",
        "isCorrectValueWithSearchAndReplaceTable": "bool",
        "isCorrectDoubleSpaceChars": "bool",
        "fileExtensionIs": ["options", uni.fileExtensionIsKeys],
        "settingsVersion": ["options", [uni.settingVersion]],
        "subDirectoryDeep": ["int", list(range(-1, 10))],
        "maxRecordFileSize": "int",
        "themeName": ["options", uni.getInstalledThemes()],
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
        "remindMeLaterForUpdate": ["int", list(range(-1, 7))],
        "remindMeLaterShowDateForUpdate": "date",
        "isShowTransactionDetails": "bool",
        "windowMode": ["options", uni.windowModeKeys],
        "isInstalledKDE4Language": "bool",
        "isShowWindowModeSuggestion": "bool",
        "isMakeAutoDesign": "bool",
        "isShowReconfigureWizard": "bool",
        "isAskIfHasManyImagesInAlbumDirectory": "bool",
        "isDeleteOtherImages": "bool",
        "CoversSubDirectoryDeep": ["int", [x for x in range(-1, 10) if x != 0]],
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
        "isActiveClearGeneral": "bool",
        "colorSchemes": "Default",
        "isActiveAutoMakeIconToDirectory": "bool",
        "isDontDeleteFileAndDirectory": "bool",
        "pathOfDeletedFilesAndDirectories": "str",
        "isReadOnlyAmarokDB": "bool",
        "isReadOnlyAmarokDBHost": "bool",
        "isResizeTableColumnsToContents": "bool",
        "AmarokFilterAmarokCoverTable": "str",
        "AmarokFilterAmarokCopyTable": "str",
        "AmarokFilterArtistTable": "str",
        "AmarokFilterAmarokMusicTable": "str",
        "isAppendFileSizeToFileTree": "bool",
        "isAppendLastModifiedToFileTree": "bool",
        "isMusicTableValuesChangeInAmarokDB": "bool",
        "isSubFolderTableValuesChangeInAmarokDB": "bool",
        "isFileTableValuesChangeInAmarokDB": "bool",
        "isFolderTableValuesChangeInAmarokDB": "bool",
        "isSubFolderMusicTableValuesChangeInAmarokDB": "bool",
        "isShowHiddensInSubFolderTable": "bool",
        "isShowHiddensInFolderTable": "bool",
        "isShowHiddensInFileTable": "bool",
        "isShowHiddensInMusicTable": "bool",
        "isShowHiddensInCoverTable": "bool",
        "isShowHiddensInSubFolderMusicTable": "bool",
        "isShowHiddensInFileTree": "bool",
        "isDecodeURLStrings": "bool",
        "isCheckUnSavedValues": "bool",
        "isAutoSaveScripts": "bool",
        "maxDeletedDirectorySize": "int"
    }


