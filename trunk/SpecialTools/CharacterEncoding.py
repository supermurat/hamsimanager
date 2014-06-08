## This file is part of HamsiManager.
## 
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


from Core import Variables
from Core import Organizer
from Core import Universals
from Core.MyObjects import *
import Tables
from Core import Dialogs
import sys
from Core import ReportBug
import Databases

class CharacterEncoding(MWidget):
    def __init__(self, _parent):
        MWidget.__init__(self, _parent)
        self.specialTools = _parent
        self.cckbCorrectText = MCheckBox(translate("SpecialTools", "Character Encoding"))
        lblColumns = MLabel(translate("SpecialTools", "Column: "))
        lblSourceValues = MLabel(translate("SpecialTools", "Source Values : "))
        lblSourceEncoding = MLabel(translate("SpecialTools", "Source Encoding : "))
        lblDestinationEncoding = MLabel(translate("SpecialTools", "Destination Encoding : "))
        self.columns = MComboBox()
        self.cbSourceEncoding = MComboBox()
        self.cbSourceEncoding.addItems(Variables.getCharSets())
        self.cbDestinationEncoding = MComboBox()
        self.cbDestinationEncoding.addItems(Variables.getCharSets())
        self.cbSourceEncoding.setCurrentIndex(self.cbSourceEncoding.findText(Universals.MySettings["fileSystemEncoding"]))
        self.cbDestinationEncoding.setCurrentIndex(self.cbDestinationEncoding.findText(Universals.MySettings["fileSystemEncoding"]))
        self.cbSourceValues = MComboBox()
        self.cbSourceValues.addItems([translate("Options", "Real Values"), 
                            translate("Options", "Table Contents")])
        HBoxs = []
        HBoxs.append(MHBoxLayout())
        HBoxs[0].addWidget(lblColumns)
        HBoxs[0].addWidget(self.columns)
        HBoxs[0].addWidget(lblSourceValues)
        HBoxs[0].addWidget(self.cbSourceValues)
        HBoxs.append(MHBoxLayout())
        HBoxs[1].addWidget(lblSourceEncoding)
        HBoxs[1].addWidget(self.cbSourceEncoding)
        HBoxs[1].addWidget(lblDestinationEncoding)
        HBoxs[1].addWidget(self.cbDestinationEncoding)
        vblCharacterEncoding = MVBoxLayout()
        vblCharacterEncoding.addLayout(HBoxs[0])
        vblCharacterEncoding.addLayout(HBoxs[1])
        self.setLayout(vblCharacterEncoding)
        lblColumns.setFixedWidth(60)
        
    def showAdvancedSelections(self):
        pass
    
    def hideAdvancedSelections(self):
        pass
    
    def checkCompleters(self):
        pass
    
    def reFillCompleters(self):
        pass
            
    def apply(self):
        Universals.MainWindow.Table.isAskShowHiddenColumn = True
        sourceEncoding = str(self.cbSourceEncoding.currentText())
        destinationEncoding = str(self.cbDestinationEncoding.currentText())
        sourceValues = str(self.cbSourceValues.currentText())
        isUseRealValues = (sourceValues == translate("Options", "Real Values"))
        if self.columns.currentIndex()==0:
            columns = list(range(0,Universals.MainWindow.Table.columnCount()))
        else:
            columns = [self.columns.currentIndex()-1]
        for columnNo in columns:
            if Universals.MainWindow.Table.checkHiddenColumn(columnNo,False)==False:
                continue
            for rowNo in range(Universals.MainWindow.Table.rowCount()):
                if Universals.MainWindow.Table.isChangableItem(rowNo, columnNo):
                    if isUseRealValues:
                        newString = Universals.MainWindow.Table.SubTable.getValueByRowAndColumn(rowNo, columnNo)
                    else:
                        newString = str(Universals.MainWindow.Table.item(rowNo,columnNo).text())
                    myString = ""
                    try:myString = Universals.trDecode(newString, sourceEncoding, "ignore")
                    except:pass
                    try:myString = str(Universals.trEncode(newString, destinationEncoding, "ignore"))
                    except:pass
                    Universals.MainWindow.Table.item(rowNo,columnNo).setText(trForUI(myString))
            
