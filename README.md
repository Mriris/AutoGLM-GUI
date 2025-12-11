# AutoGLM-GUI

AutoGLM 手机助手的现代化 Web 图形界面 - 让 AI 自动化操作 Android 设备变得简单

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)

## ✨ 特性

- **对话式任务管理** - 通过聊天界面控制 Android 设备
- **实时屏幕预览** - 随时查看设备正在执行的操作
- **零配置部署** - 支持任何 OpenAI 兼容的 LLM API
- **ADB 深度集成** - 通过 Android Debug Bridge 直接控制设备

## 📸 界面预览

### 任务开始
![任务开始](https://github.com/user-attachments/assets/b8cb6fbc-ca5b-452c-bcf4-7d5863d4577a)

### 任务执行完成
![任务结束](https://github.com/user-attachments/assets/b32f2e46-5340-42f5-a0db-0033729e1605)

## 🚀 快速开始

### 前置要求

- Python 3.10+
- 已开启 USB 调试的 Android 设备
- 已安装 ADB 并添加到系统 PATH
- 一个 OpenAI 兼容的 API 端点

### 快捷运行（推荐）

**无需安装，直接运行：**

```bash
# 使用 uvx 一键启动（无需提前安装包）
uvx autoglm-gui --base-url http://localhost:8080/v1
```

需要提前安装 uv，[安装教程](https://docs.astral.sh/uv/getting-started/installation/)。

### 传统安装


```bash
# 方式 1: 通过 pip 安装
pip install autoglm-gui
autoglm-gui --base-url http://localhost:8080/v1

# 方式 2: 从源码安装
git clone https://github.com/your-repo/AutoGLM-GUI.git
cd AutoGLM-GUI
uv sync

# 构建前端（必须）
uv run python scripts/build.py

# 启动服务
uv run autoglm-gui --base-url http://localhost:8080/v1
```

启动后，在浏览器中打开 http://localhost:8000 即可开始使用！

## 📖 使用说明

1. **连接设备** - 启用 USB 调试并通过 ADB 连接设备
2. **对话** - 描述你想要做什么（例如："去美团点一杯霸王茶姬的伯牙绝弦"）
3. **观察** - Agent 会逐步执行操作

## 🛠️ 开发指南

```bash
# 后端开发（自动重载）
uv run autoglm-gui --base-url http://localhost:8080/v1 --reload

# 前端开发服务器
cd frontend && pnpm dev

# 构建完整包
uv run python scripts/build.py --pack
```

## 📝 开源协议

Apache License 2.0

## 🙏 致谢

本项目基于 [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) 构建，感谢 zai-org 团队在 AutoGLM 上的卓越工作。
