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

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from Item import Item
import json

class TodoList(QWidget):
    
    def __init__(self):
        super().__init__()
        self.items = []
        self.layout = QVBoxLayout()
        self.indent_step = 20
        
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.setWindowTitle("Do it tomorrow !!")
        self.setFocusPolicy(Qt.ClickFocus)
        
        self.load()
        self.refresh()


    def item_finished_slot(self, index):
        del self.items[index]
        self.update_item_index(index)

    def item_commit_slot(self, index):
        self.add_item(index+1, self.items[index].level)
        self.update_item_index(index)
        self.refresh()
        self.items[index].clearFocus()
        self.items[index+1].lineedit.setFocus()
        self.save()

    def item_tab_pressed_slot(self, index):
        if index>0 and self.items[index].level-self.items[index-1].level<1:
            self.items[index].level += 1
            self.items[index].setContentsMargins(self.indent_step*self.items[index].level,0,0,0)

    def load(self):
        try:
            with open('todolist.json','r',encoding='utf-8') as f:
                data = json.load(f)
            i = 0
            for one in data:
                if one['text']:
                    self.add_item(i, one['level'], one['text'])
                    i += 1
        except:
            self.add_item(0)
        self.refresh()

    def save(self):
        data = []
        for item in self.items:
            data.append({'level': item.level, 'text': item.lineedit.text()})
        with open('todolist.json','w',encoding='utf-8') as f:
            json.dump(data,f)
    
    def add_item(self, index, level=0, text=None):
        item = Item(index, level, text)
        item.item_finished_signal.connect(self.item_finished_slot)
        item.item_commit_signal.connect(self.item_commit_slot)
        item.item_tab_pressed_signal.connect(self.item_tab_pressed_slot)
        self.items.insert(index,item)
    
    def update_item_index(self, begin=0):
        for i in range(begin,len(self.items)):
            self.items[i].index = i
    
    def refresh(self):
        for item in self.items:
            self.layout.addWidget(item)
            if item.level:
                item.setContentsMargins(self.indent_step*item.level,0,0,0)

