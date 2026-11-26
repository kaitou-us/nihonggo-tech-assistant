# 30天 AI 软件工程实战训练营

## 学员基本信息

- 求职目标：日本 IT 实习 / 初级软件开发岗位
- 每日学习时间：3小时
- 开发工具：VS Code
- 开发环境：Windows + PowerShell
- 教学模式：理论学习、独立开发、代码审查、运行验收、知识考试

## 主线项目

**Nihongo Tech Assistant — 日语技术文档 AI 学习助手**

本地路径：`D:\nihonggo-tech-assistant`

最终技术栈：Python、FastAPI、Vue 3、SQLite、RAG、Docker、GitHub。

## Day 01：Python 工程基础

状态：已通过

知识考试：81/100

### 已完成成果

- Python 虚拟环境搭建
- 模块化项目结构
- UTF-8 文件读取
- 词频统计与排序
- 重复词汇筛选
- 文本报告生成
- 模块联调与正常数据运行验收

### 当前模块

- `src/file_handler.py`
- `src/analyzer.py`
- `src/reporter.py`
- `src/main.py`
- `data/vocabulary.txt`
- `reports/report.txt`

### 实际运行结果

- 总词汇数：15
- 唯一词汇数：9
- 重复词汇种类：5
- 报告生成成功

### 知识薄弱点

- Path 对象与字符串的区别
- splitlines() 和 strip() 的准确行为
- Python 模块导入与运行机制
- 独立需求拆解
- 独立 Debug 能力

### 遗留技术债务

- 返回值类型注解不准确
- 文件读取失败与空文件的区分
- 相对路径依赖工作目录
- 边界测试尚未确认

计划在 Day 3 进行工程化重构。

---

## Day 02：Git 版本管理与 GitHub 工程实践

状态：学习中

目标版本：v0.1.0

### 学习安排

| 内容 | 时间 |
|---|---:|
| Git 工作原理 | 25分钟 |
| 仓库初始化与 gitignore | 25分钟 |
| 分支管理与冲突处理 | 45分钟 |
| GitHub 与 Pull Request | 30分钟 |
| README 与提交规范 | 30分钟 |
| 版本发布与考试 | 25分钟 |

### 核心知识

- Git 与 GitHub 的区别
- Working Directory
- Staging Area
- Local Repository
- Remote Repository
- git add、commit、push、pull
- git status
- git diff --cached
- git check-ignore
- 功能分支工作流
- Merge Conflict
- Pull Request
- Conventional Commits
- Git Tag

### 实战任务：Issue #001

改善词汇分析报告的可读性。

功能要求：

1. 无重复词汇时显示提示。
2. 改善报告段落排版。
3. 增加报告生成时间。
4. 使用 feature/report-improvement 分支开发。
5. 完成功能测试与代码审查。
6. 模拟并解决一次合并冲突。
7. 合并功能分支并发布版本。

### 当前任务清单

- [ ] 检查 Git 环境
- [ ] 初始化本地仓库
- [ ] 创建 .gitignore
- [ ] 检查暂存区文件
- [ ] 完成首次正式提交
- [ ] 创建功能分支
- [ ] 实现 Issue #001
- [ ] 解决合并冲突
- [ ] 建立 GitHub 远程仓库
- [ ] 完成 Pull Request
- [ ] 编写 README.md
- [ ] 发布 v0.1.0
- [ ] 完成 Day 2 考试

### 当前教学断点

等待学员完成 Git 环境检查、仓库初始化及 .gitignore 创建，并提交以下命令的输出：

```powershell
git --version
git status
git branch
git diff --cached --stat
```

下一步：审查 .gitignore 和仓库状态，指导首次正式提交。

### 技术日语

- バージョン管理：版本管理
- リポジトリ：仓库
- ブランチ：分支
- コミット：提交
- 差分（さぶん）：修改差异
- 競合（きょうごう）：冲突
- マージ：合并
- コードレビュー：代码审查

---

## 课程进度

Day 01：已通过  
Day 02：进行中  
Day 03–30：待学习

已通过课程：1/30

总体课程进度：3.33%
