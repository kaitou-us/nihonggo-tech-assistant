# Nihongo Tech Assistant

日语技术文档学习助手（开发中）。

## 项目简介

这是一个面向日语技术学习者的 Python 项目，计划逐步实现日语技术文档管理、内容检索、词汇解释和 AI 辅助阅读。

## 当前功能

- 读取 UTF-8 编码的日语词汇文件
- 统计词汇总数和唯一词汇数量
- 检测重复词汇
- 按出现次数排序
- 生成文本统计报告

## 技术栈

- Python
- pathlib
- collections.Counter
- Git

## 环境要求

- Python 3.11 或更高版本（实际版本待确认）
- Git

## 运行方法

在项目根目录执行：

```powershell
python -m src.main
```

## 项目结构

```text
nihonggo-tech-assistant/
├── data/
│   └── vocabulary.txt
├── reports/
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── file_handler.py
│   ├── reporter.py
│   └── main.py
├── .gitignore
└── README.md
```

## 开发状态

当前处于 Python CLI 原型阶段。

后续计划：

1. 完善 Python 后端工程结构
2. 增加 SQLite 数据库
3. 开发 FastAPI 接口
4. 开发 Vue 前端
5. 接入大语言模型
6. 实现基于文档的 RAG 问答
