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

from TodoList import TodoList
from PySide6.QtWidgets import QApplication
import sys

app = QApplication([])
widget = TodoList()
widget.resize(300, 400)
widget.show()
sys.exit(app.exec_())
