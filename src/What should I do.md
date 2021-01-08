# 思考思考怎么设计

## Item类

继承自`QtWidgets.QWidget`类

属性：

| 属性名   | 类型                  | 说明           |
| -------- | --------------------- | -------------- |
| level    | int                   | 项目的级别     |
| order    | int                   | 当前项目的序号 |
| layout   | QtWidgets.QHBoxLayout | 布局           |
| checkbox | QtWidgets.QCheckBox   | 左侧的复选框   |
| lineedit | QtWidgets.QLineEdit   | 右侧的输入行   |

方法：

| 方法名与参数           | 返回值类型 | 功能                                       |
| ---------------------- | ---------- | ------------------------------------------ |
| \_\_init\_\_(self)     | None       | 构造函数                                   |
| set_level(self, level) | None       | 设置当前项的级别                           |
| focusNextChild()       | bool       | 移动焦点，但是问题是我自己也不知道移到哪了 |
| deleteLater()          |            | 用于删除这个对象                           |

信号：

| 信号名                     | 说明                                               |
| -------------------------- | -------------------------------------------------- |
| lineedit.returnPressed     | lineedit这个输入框按下了`return`键                 |
| checkbox.stateChanged(int) | checkbox状态改变                                   |
| item_finished_signal       | 点击了复选框，这个对象要被删除了                   |
| item_commit_signal         | 输入框了按了回车，并且输入了东西，要新建个Item项了 |

槽：

| 槽方法名                   | 返回值类型 | 说明                               |
| -------------------------- | ---------- | ---------------------------------- |
| lineedit.returnPressed     |            | lineedit这个输入框按下了`return`键 |
| checkbox.stateChanged(int) | None       | checkbox状态改变                   |
|                            |            |                                    |





## TodoList类

继承自`QtWidgets.QWidget`类

属性：

| 属性名 | 类型                  | 说明             |
| ------ | --------------------- | ---------------- |
| layout | QtWidgets.QVBoxLayout | 布局             |
| items  | list                  | 保存所有item对象 |
|        |                       |                  |
|        |                       |                  |

方法：

| 方法名与参数         | 返回值类型 | 功能                                    |
| -------------------- | ---------- | --------------------------------------- |
| \_\_init\_\_(self)   | None       | 构造函数                                |
| load(self)           |            | 加载文件                                |
| save(self)           |            | 保存到文件中                            |
| add_item(self,index) | None       | 向items中插入新的item项                 |
| refresh(self)        | None       | 将items里面的项目添加到layout布局中显示 |

信号：

| 信号名 | 说明 |
| ------ | ---- |
|        |      |
|        |      |
|        |      |

槽：

| 槽方法名           | 返回值类型 | 说明                                               |
| ------------------ | ---------- | -------------------------------------------------- |
| item_finished_slot | None       | 从items中移除这个对象，并且更改后面item项的序号    |
| item_commit_slot   | None       | 其中一个item项确认后，需要在这个项的下面新建一个项 |
|                    |            |                                                    |