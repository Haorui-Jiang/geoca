# 版本更新日志

## v0.0.3 - 2024.2.24

**改进**：

- 删除用于初始项目测试的所有代码。

**新功能**：

- 从文件中读取栅格数据，并将数据转换为 Python 列表。
- 根据输入栅格创建栅格模板，并将列表中的数据替换到该栅格模板中。
- 根据栅格数据运行 CA 模型，分析人口或其他资源的迁移情况。

## v0.0.4 - 2024.3.18

**改进**：

- 修改原始代码和注释。
- 添加部分新功能。

**新功能**：

- 从文件夹中批量读取栅格数据（.tif）并将其存储在字典中。
- 对代表多个栅格数据的列表字典进行重构。

## v0.0.5 - 2024.3.29

**改进**：

- 修复导出栅格数据部分的相关代码。

## v0.0.6 - 2024.9.6

**改进**:

- 修改部分函数名称。

**新功能**:

- 通过初始人口数量栅格执行元胞自动机。

## v0.0.7 - 2024.9.11

**改进**:

- 修改部分函数名称。
- 迁移方向由8个降为4个（仅保留东、西、南、北）。

**新功能**:

- 人口可基于栅格像元值大小分散迁移至各个相邻区域。
- 可将一定比例的人口集中迁移到适宜性最强的地区。

## v0.0.8 - 2024.9.12

**改进**:

- 可设置迁移方向的数量（4 或 8）。

## v0.0.9 - 2024.9.17

**新功能**:

- 根据成本路径栅格及环境栅格计算迁移时间。

## v0.0.10 - 2024.9.19

**改进**:

- 修改CA模型输出效果，添加进度条。

## v0.0.11 - 2024.9.20

**改进**:

- 修正部分函数模型算法。