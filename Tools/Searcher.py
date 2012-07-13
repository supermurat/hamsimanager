## This file is part of HamsiManager.
## 
## Copyright (c) 2010 - 2012 Murat Demir <mopened@gmail.com>      
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


from Core.MyObjects import *
from Core import Universals
from Core import Dialogs
import InputOutputs
import Options
from Options import OptionsForm
from Core import Organizer
import unicodedata

MyDialog, MyDialogType, MyParent = getMyDialog()

class Searcher(MyDialog):
    def __init__(self, _directory):
        MyDialog.__init__(self, MyParent)
        if MyDialogType=="MDialog":
            if Universals.isActivePyKDE4==True:
                self.setButtons(MyDialog.NoDefault)
        elif MyDialogType=="MMainWindow":
            self.setObjectName("Searcher")
            Universals.setMainWindow(self)
        newOrChangedKeys = Universals.newSettingsKeys + Universals.changedDefaultValuesKeys
        wOptionsPanel = OptionsForm.OptionsForm(None, "search", None, newOrChangedKeys)
        self.isMultipleSource = False
        self.sourceToSearch = None
        self.tmrSearchAfter = None
        lblPleaseSelect = MLabel(translate("Searcher", "Directory Or File : "))
        self.pbtnClose = MPushButton(translate("Searcher", "Close"))
        self.lePathToSeach = MLineEdit(trForM(_directory))
        self.pbtnSelectSeachDirectoryPath = MPushButton(translate("Searcher", "Select Directory"))
        self.pbtnSelectSeachFilePath = MPushButton(translate("Searcher", "Select File"))
        self.connect(self.pbtnSelectSeachDirectoryPath,SIGNAL("clicked()"),self.selectSearchDirectoryPath)
        self.connect(self.pbtnSelectSeachFilePath,SIGNAL("clicked()"),self.selectSearchFilePath)
        self.pbtnAddSeachDirectoryPath = MPushButton(translate("Searcher", "Add Directory"))
        self.pbtnAddSeachFilePath = MPushButton(translate("Searcher", "Add File"))
        self.connect(self.pbtnAddSeachDirectoryPath,SIGNAL("clicked()"),self.addSearchDirectoryPath)
        self.connect(self.pbtnAddSeachFilePath,SIGNAL("clicked()"),self.addSearchFilePath)
        self.connect(self.pbtnClose,SIGNAL("clicked()"),self.close)
        self.pbtnReloadSourceToSearch = MPushButton(translate("Searcher", "(Re)Load"))
        self.connect(self.pbtnReloadSourceToSearch,SIGNAL("clicked()"),self.reloadSourceToSearch)
        self.pbtnSearch = MPushButton(translate("Searcher", "Search"))
        self.connect(self.pbtnSearch,SIGNAL("clicked()"),self.search)
        lblSearch = MLabel(translate("Searcher", "Search : "))
        lblSearchList = MLabel(translate("Searcher", "Search List : "))
        self.lblSearchListValues = MLabel(trForM(""))
        self.lblSearchListValues.setWordWrap(True)
        self.leSearch = MLineEdit(trForM(""))
        self.teSearchResult = MTextEdit()
        self.teSearchResult.setText(trForUI(""))
        self.connect(self.leSearch,SIGNAL("textChanged(const QString&)"), self.searchAfter)
        self.cckbIsRegExp = Options.MyCheckBox(self, translate("Searcher", "Regular Expression (RegExp)"), 0, _stateChanged = self.isRegExpChanged)
        self.cckbIsCaseInsensitive = Options.MyCheckBox(self, translate("Searcher", "Case Insensitive"), 2, _stateChanged = self.search)
        self.cckbIsNormalizeUTF8Chars = Options.MyCheckBox(self, translate("Searcher", "Normalize UTF-8 Characters"), 2, _stateChanged = self.search)
        self.cckbIsClearDigits = Options.MyCheckBox(self, translate("Searcher", "Clear Digits"), 2, _stateChanged = self.search)
        self.cckbIsOnlyDigitsAndLetters = Options.MyCheckBox(self, translate("Searcher", "Only Digits And Letters"), 2, _stateChanged = self.search)
        self.cckbIsClearVowels = Options.MyCheckBox(self, translate("Searcher", "Clear Vowels"), 2, _stateChanged = self.search)
        self.cckbIsNormalizeUTF8CharsAndClearVowels = Options.MyCheckBox(self, translate("Searcher", "Normalize UTF-8 Characters And Clear Vowels"), 2, _stateChanged = self.search)
        self.cckbIsLineWrap = Options.MyCheckBox(self, translate("Searcher", "Wrap By Width"), 0, _stateChanged = self.isLineWrap)
        self.pbtnEditValuePathToSeach = MPushButton(translate("Options", "*"))
        self.pbtnEditValuePathToSeach.setObjectName(trForUI(translate("Options", "Edit Values With Advanced Value Editor") + "Path To Seach"))
        self.pbtnEditValuePathToSeach.setToolTip(translate("Options", "Edit values with Advanced Value Editor"))
        self.pbtnEditValuePathToSeach.setFixedWidth(25)
        MObject.connect(self.pbtnEditValuePathToSeach, SIGNAL("clicked()"), self.pbtnEditValuePathToSeachClicked)
        pnlMain = MWidget(self)
        tabwTabs = MTabWidget()
        vblMain = MVBoxLayout(pnlMain)
        pnlMain2 = MWidget(tabwTabs)
        vblMain2 = MVBoxLayout(pnlMain2)
        HBox = MHBoxLayout()
        HBox.addWidget(self.lePathToSeach)
        HBox.addWidget(self.pbtnEditValuePathToSeach)
        HBox1 = MHBoxLayout()
        HBox1.addWidget(self.pbtnReloadSourceToSearch)
        HBox1.addWidget(self.pbtnSelectSeachDirectoryPath)
        HBox1.addWidget(self.pbtnAddSeachDirectoryPath)
        HBox1.addWidget(self.pbtnSelectSeachFilePath)
        HBox1.addWidget(self.pbtnAddSeachFilePath)
        HBox3 = MHBoxLayout()
        HBox3.addWidget(lblSearch, 1)
        HBox3.addWidget(self.leSearch, 20)
        HBox3.addWidget(self.pbtnSearch, 1)
        HBox2 = MHBoxLayout()
        HBox2.addWidget(self.pbtnClose)
        VBox1 = MVBoxLayout()
        HBox4 = MHBoxLayout()
        HBox4.addWidget(self.cckbIsClearDigits)
        HBox4.addWidget(self.cckbIsOnlyDigitsAndLetters)
        HBox5 = MHBoxLayout()
        HBox5.addWidget(self.cckbIsNormalizeUTF8Chars)
        HBox5.addWidget(self.cckbIsClearVowels)
        HBox6 = MHBoxLayout()
        HBox6.addWidget(self.cckbIsNormalizeUTF8CharsAndClearVowels)
        HBox7 = MHBoxLayout()
        HBox7.addWidget(lblSearchList, 1)
        HBox7.addWidget(self.lblSearchListValues, 20)
        HBox8 = MHBoxLayout()
        HBox8.addWidget(self.cckbIsRegExp)
        HBox8.addWidget(self.cckbIsCaseInsensitive)
        VBox1.addLayout(HBox8)
        VBox1.addLayout(HBox4)
        VBox1.addLayout(HBox5)
        VBox1.addLayout(HBox6)
        vblMain2.addWidget(lblPleaseSelect)
        vblMain2.addLayout(HBox)
        vblMain2.addLayout(HBox1)
        vblMain2.addLayout(HBox3)
        vblMain2.addLayout(HBox7)
        gboxFilters = MGroupBox(translate("Searcher", "Filters : "))
        gboxFilters.setLayout(VBox1)
        vblMain2.addWidget(gboxFilters)
        vblMain2.addWidget(self.teSearchResult, 20)
        vblMain2.addWidget(self.cckbIsLineWrap)
        vblMain2.addStretch(1)
        vblMain2.addLayout(HBox2)
        tabwTabs.addTab(pnlMain2, translate("Searcher", "Search"))
        tabwTabs.addTab(wOptionsPanel, translate("Searcher", "Quick Options"))
        vblMain.addWidget(tabwTabs)
        if MyDialogType=="MDialog":
            if Universals.isActivePyKDE4==True:
                self.setMainWidget(pnlMain)
            else:
                self.setLayout(vblMain)
        elif MyDialogType=="MMainWindow":
            self.setCentralWidget(pnlMain)
            moveToCenter(self)
        self.isRegExpChanged(False)
        self.isLineWrap()
        self.setWindowTitle(translate("Searcher", "Searcher"))
        self.setWindowIcon(MIcon("Images:search.png"))
        self.show()
                        
    def closeEvent(self, _event):
        MApplication.setQuitOnLastWindowClosed(True)
    
    def reloadSourceToSearch(self):
        if self.setSourceToSearch():
            self.search()
    
    def setSourceToSearch(self, _isReload=True):
        try:
            if self.sourceToSearch == None or _isReload==True:
                sourceToSearch = ""
                self.isMultipleSource = False
                pathToSearchs = str(self.lePathToSeach.text())
                if InputOutputs.isExist(pathToSearchs)==False and pathToSearchs.find(";")!=-1:
                    self.isMultipleSource = True
                for pathToSearch in Universals.getListFromListString(pathToSearchs, ";"):
                    if InputOutputs.checkSource(pathToSearch):
                        if InputOutputs.isReadableFileOrDir(pathToSearch):
                            if InputOutputs.isFile(pathToSearch):
                                sourceToSearch += InputOutputs.readFromFile(pathToSearch) + "\n"
                            elif InputOutputs.isDir(pathToSearch):
                                sourceToSearch += InputOutputs.getFileTree(pathToSearch, -1, "return", "plainText", "fileList") + "\n"
                self.sourceToSearch = sourceToSearch
                if sourceToSearch!="":
                    return True
                return False
            else:
                return True
        except:
            from Core import ReportBug
            error = ReportBug.ReportBug()
            error.show() 
            
    def getSearchValueList(self):
        searchValue = str(self.leSearch.text())
        if searchValue!="":
            searchValueList = [searchValue]
            if self.cckbIsNormalizeUTF8Chars.checkState() == Mt.Checked or self.cckbIsNormalizeUTF8CharsAndClearVowels.checkState() == Mt.Checked:
                clearedSearchValue = ''.join(c for c in unicodedata.normalize('NFKD', Universals.trUnicode(searchValue)) if unicodedata.category(c) != 'Mn')
                clearedSearchValue = str(Universals.trEncode(clearedSearchValue, "utf-8", "ignore")).replace(Universals.getUtf8Data("little+I"), "i")
            
            if self.cckbIsNormalizeUTF8Chars.checkState() == Mt.Checked:
                if clearedSearchValue not in searchValueList:
                    searchValueList.append(clearedSearchValue)
            
            if self.cckbIsClearDigits.checkState() == Mt.Checked:
                clearedSearchValue1 = ""
                for char in searchValue:
                    if char.isdigit()==False:
                        clearedSearchValue1+=char
                if clearedSearchValue1 not in searchValueList:
                    searchValueList.append(clearedSearchValue1)
            
            if self.cckbIsOnlyDigitsAndLetters.checkState() == Mt.Checked:
                clearedSearchValue2 = ""
                for char in Universals.trUnicode(searchValue):
                    if char.isdigit()==True or char.isalpha()==True:
                        clearedSearchValue2+=char
                if clearedSearchValue2 not in searchValueList:
                    searchValueList.append(clearedSearchValue2)
            
            vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
            if self.cckbIsClearVowels.checkState() == Mt.Checked:
                clearedSearchValue3 = ""
                for char in Universals.trUnicode(searchValue):
                    clearedChar = ''.join(c for c in unicodedata.normalize('NFKD', Universals.trUnicode(char)) if unicodedata.category(c) != 'Mn')
                    clearedChar = str(Universals.trEncode(clearedChar, "utf-8", "ignore")).replace(Universals.getUtf8Data("little+I"), "i")
                    if clearedChar not in vowels:
                        clearedSearchValue3+=char
                if clearedSearchValue3 not in searchValueList:
                    searchValueList.append(clearedSearchValue3)
            
            if self.cckbIsNormalizeUTF8CharsAndClearVowels.checkState() == Mt.Checked:
                clearedSearchValue4 = ""
                for char in clearedSearchValue:
                    if char not in vowels:
                        clearedSearchValue4+=char
                if clearedSearchValue4 not in searchValueList:
                    searchValueList.append(clearedSearchValue4)
            return searchValueList
        else:
            return []
    
    def searchAfter(self, _searchValue=""):
        try:
            if self.cckbIsRegExp.checkState() != Mt.Checked:
                if self.tmrSearchAfter!= None:
                    self.tmrSearchAfter.stop()
                    self.tmrSearchAfter.deleteLater()
                self.tmrSearchAfter = MTimer(self)
                self.tmrSearchAfter.setSingleShot(True)
                self.connect(self.tmrSearchAfter,SIGNAL("timeout()"),self.search)
                self.tmrSearchAfter.start(500)
        except:
            from Core import ReportBug
            error = ReportBug.ReportBug()
            error.show() 
    
    def search(self, _searchValue=""):
        try:
            import re
            if self.setSourceToSearch(False):
                if self.cckbIsRegExp.checkState() == Mt.Checked:
                    searchValueList = [str(self.leSearch.text())]
                else:
                    searchValueList = self.getSearchValueList()
                if len(searchValueList)!=0:
                    searchValueListForToolTip = ""
                    resultOfSearch = ""
                    arrayOfSource = str(self.sourceToSearch).split("\n\r")
                    if len(arrayOfSource)==1: arrayOfSource = str(self.sourceToSearch).split("\n")
                    if len(arrayOfSource)==1: arrayOfSource = str(self.sourceToSearch).split("<br>")
                    if len(arrayOfSource)==1: arrayOfSource = str(self.sourceToSearch).split("<br/>")
                    if len(arrayOfSource)==1: arrayOfSource = str(self.sourceToSearch).split("<br >")
                    if len(arrayOfSource)==1: arrayOfSource = str(self.sourceToSearch).split("<br />")
                    for row in arrayOfSource:
                        for searchVal in searchValueList:
                            if self.cckbIsRegExp.checkState() == Mt.Checked:
                                try:
                                    if self.cckbIsCaseInsensitive.checkState() == Mt.Checked:
                                        pattern = re.compile(Universals.trUnicode(searchVal), re.I | re.U)
                                        if re.search(pattern, Universals.trUnicode(row)) is not None:
                                            resultOfSearch += row + "\n"
                                            break
                                    else:
                                        pattern = re.compile(Universals.trUnicode(searchVal), re.U)
                                        if re.search(pattern, Universals.trUnicode(row)) is not None:
                                            resultOfSearch += row + "\n"
                                            break
                                except:
                                    Dialogs.show(translate("Searcher", "Incorrect Syntax"), translate("Searcher", "Search value is not correct for Regular Expression (RegExp). Please check it and try again."))
                                    return False
                            else:
                                if row.find(searchVal) != -1:
                                    resultOfSearch += row + "\n"
                                    break
                                if self.cckbIsCaseInsensitive.checkState() == Mt.Checked:
                                    pattern = re.compile(re.escape(Universals.trUnicode(searchVal)), re.I | re.U)
                                    if re.search(pattern, Universals.trUnicode(row)) is not None:
                                        resultOfSearch += row + "\n"
                                        break
                                else:
                                    pattern = re.compile(re.escape(Universals.trUnicode(searchVal)), re.U)
                                    if re.search(pattern, Universals.trUnicode(row)) is not None:
                                        resultOfSearch += row + "\n"
                                        break
                    for searchVal in searchValueList:
                        searchValueListForToolTip += "'" + searchVal + "', "
                    self.lblSearchListValues.setText(trForUI(searchValueListForToolTip[0:-2]))
                else:
                    resultOfSearch = str(self.sourceToSearch)
                    self.lblSearchListValues.setText(trForUI(""))
                self.teSearchResult.setText(trForUI(resultOfSearch))
        except:
            from Core import ReportBug
            error = ReportBug.ReportBug()
            error.show() 

    def isRegExpChanged(self, _isSearch=True):
        if self.cckbIsRegExp.checkState() == Mt.Checked:
            self.cckbIsNormalizeUTF8Chars.setEnabled(False)
            self.cckbIsClearDigits.setEnabled(False)
            self.cckbIsOnlyDigitsAndLetters.setEnabled(False)
            self.cckbIsClearVowels.setEnabled(False)
            self.cckbIsNormalizeUTF8CharsAndClearVowels.setEnabled(False)
        else:
            self.cckbIsNormalizeUTF8Chars.setEnabled(True)
            self.cckbIsClearDigits.setEnabled(True)
            self.cckbIsOnlyDigitsAndLetters.setEnabled(True)
            self.cckbIsClearVowels.setEnabled(True)
            self.cckbIsNormalizeUTF8CharsAndClearVowels.setEnabled(True)
        self.lblSearchListValues.setText(trForM(""))
        if _isSearch:
            self.search()
            
    def isLineWrap(self):
        if self.cckbIsLineWrap.checkState() == Mt.Checked:
            self.teSearchResult.setLineWrapMode(MTextEdit.WidgetWidth)
        else:
            self.teSearchResult.setLineWrapMode(MTextEdit.NoWrap)
    
    def selectSearchDirectoryPath(self):
        try:
            SearchPath = QFileDialog.getExistingDirectory(self,
                            translate("Searcher", "Please Select Directory"),self.lePathToSeach.text())
            if SearchPath!="":
                self.lePathToSeach.setText(SearchPath)
                if self.setSourceToSearch(True):
                    self.search()
        except:
            from Core import ReportBug
            error = ReportBug.ReportBug()
            error.show() 
    
    def addSearchDirectoryPath(self):
        try:
            SearchPath = QFileDialog.getExistingDirectory(self,
                            translate("Searcher", "Please Select Directory"),self.lePathToSeach.text())
            if SearchPath!="":
                SearchPaths = Universals.getListFromListString(self.lePathToSeach.text(), ";")
                SearchPaths.append(SearchPath)
                self.lePathToSeach.setText(Universals.getStringFromList(SearchPaths, ";"))
                if self.setSourceToSearch(True):
                    self.search()
        except:
            from Core import ReportBug
            error = ReportBug.ReportBug()
            error.show() 


    def selectSearchFilePath(self):
        try:
            SearchPaths = QFileDialog.getOpenFileNames(self,
                        translate("Searcher", "Please Select A Text File To Search"), self.lePathToSeach.text(),
                        translate("Searcher", "All Files (*.*)"))
                        
            SearchPaths = list(SearchPaths)
            if SearchPaths!=[]:
                self.lePathToSeach.setText(Universals.getStringFromList(SearchPaths, ";"))
                if self.setSourceToSearch(True):
                    self.search()
        except:
            from Core import ReportBug
            error = ReportBug.ReportBug()
            error.show() 

    def addSearchFilePath(self):
        try:
            SearchPaths = QFileDialog.getOpenFileNames(self,
                        translate("Searcher", "Please Select A Text File To Search"), self.lePathToSeach.text(),
                        translate("Searcher", "All Files (*.*)"))
                        
            SearchPaths = list(SearchPaths)
            if SearchPaths!=[]:
                SearchPaths = Universals.getListFromListString(self.lePathToSeach.text(), ";") + SearchPaths
                self.lePathToSeach.setText(Universals.getStringFromList(SearchPaths, ";"))
                if self.setSourceToSearch(True):
                    self.search()
        except:
            from Core import ReportBug
            error = ReportBug.ReportBug()
            error.show() 
    
    def pbtnEditValuePathToSeachClicked(self):
        aved = AdvancedValueEditorDialog(self)
    
class AdvancedValueEditorDialog(MDialog):
    def __init__(self, _parent):
        MDialog.__init__(self, _parent)
        if Universals.isActivePyKDE4==True:
            self.setButtons(MDialog.NoDefault)
        self.setWindowTitle(translate("AdvancedValueEditorDialog", "Advanced Value Editor"))
        currentValuePathToSeach = str(self.parent().lePathToSeach.text())
        if Universals.isActivePyKDE4==True:
            self.EditorWidgetPathToSeach = MEditListBox(self)
            self.EditorWidgetPathToSeach.setItems([trForUI(x) for x in currentValuePathToSeach.split(";")])
        else:
            self.EditorWidgetPathToSeach = MTextEdit(self)
            self.EditorWidgetPathToSeach.setText(trForUI(currentValuePathToSeach.replace(";", "\n")))
        pnlMain = MWidget(self)
        vblMain = MVBoxLayout(pnlMain)
        pbtnCancel = MPushButton(translate("AdvancedValueEditorDialog", "Cancel"))
        pbtnApply = MPushButton(translate("AdvancedValueEditorDialog", "Apply"))
        MObject.connect(pbtnCancel, SIGNAL("clicked()"), self.close)
        MObject.connect(pbtnApply, SIGNAL("clicked()"), self.apply)
        vblMain.addWidget(MLabel(translate("AdvancedValueEditorDialog", "Search List : ")))
        vblMain.addWidget(self.EditorWidgetPathToSeach)
        hblBox = MHBoxLayout()
        hblBox.addWidget(pbtnApply)
        hblBox.addWidget(pbtnCancel)
        vblMain.addLayout(hblBox)
        if Universals.isActivePyKDE4==True:
            self.setMainWidget(pnlMain)
        else:
            self.setLayout(vblMain)
        self.setMinimumSize(550, 400)
        self.show()
        
    def apply(self):
        valuePathToSeach = ""
        if Universals.isActivePyKDE4==True:
            for y, info in enumerate(self.EditorWidgetPathToSeach.items()):
                if y!=0:
                    valuePathToSeach += ";"
                valuePathToSeach += str(info)
        else:
            valuePathToSeach = str(self.EditorWidgetPathToSeach.toPlainText()).replace("\n", ";")
        self.parent().lePathToSeach.setText(trForUI(valuePathToSeach))
        self.close()
        
        
    
                
