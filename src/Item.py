# Copyright 2021 Dingzx97
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLineEdit
from PySide6.QtCore import Qt, Signal, QEvent


class Item(QWidget):
    
    item_finished_signal = Signal(int)
    item_commit_signal = Signal(int)
    item_tab_pressed_signal = Signal(int)
    
    
    def __init__(self, index, level=0, text=None):
        super().__init__()
        self.index = index
        self.level = level
        
        self.layout = QHBoxLayout()
        self.checkbox = QCheckBox()
        self.lineedit = QLineEdit()
        
        self.checkbox.setFocusPolicy(Qt.NoFocus)
        self.lineedit.setFocusPolicy(Qt.ClickFocus)
        self.lineedit.setText(text)
        self.lineedit.installEventFilter(self)
        
        
        self.layout.addWidget(self.checkbox)
        self.layout.addWidget(self.lineedit)
        self.setLayout(self.layout)

        self.checkbox.stateChanged.connect(self.checked_slot)
        self.lineedit.returnPressed.connect(self.return_slot)


    def checked_slot(self):
        self.item_finished_signal.emit(self.index)
        self.deleteLater()

    def return_slot(self):
        if self.lineedit.text():
            self.item_commit_signal.emit(self.index)

    def eventFilter(self, obj, event):
        if obj == self.lineedit:
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Tab:
                    self.item_tab_pressed_signal.emit(self.index)
                    return True
        return QWidget.eventFilter(self, obj, event)
