# AI For U

在主流免费算力平台上一键安装 AI For U，并支持国内模型的下载。本项目旨在提供一个高效、便捷的 AI For U 安装与配置解决方案。

## 功能特点

- **自动化安装**：一键安装 ComfyUI等热门Ai应用 及其所有依赖，简化安装流程。
- **一键运行**：一键运行 ComfyUI 及隧道 服务
- **国内镜像源支持**：通过国内镜像源快速下载模型，提升下载速度。
- **自动配置 Conda 环境**：自动创建和配置 Conda 环境，便于管理依赖。
- **断点续传支持**：安装过程中支持断点续传，确保安装过程稳定。
- **友好的命令行界面**：简洁直观的命令行界面，提升用户体验。
- **详细日志记录**：全面记录安装和运行日志，方便问题排查。
- **自动环境检测**：自动检测并配置 CUDA、PyTorch 等依赖环境。
- **模块化设计**：各功能模块独立，便于维护和扩展。

## 支持平台
- [x] 腾讯 Cloud Studio 【免费T4 16G显存】【[视频介绍](https://www.bilibili.com/video/BV1BJmSYFE2a/)】
- [] Google Colab
- [] Kaggle
- [] 启智免费算力平台 【免费A100 40G显存】【[视频介绍](https://www.bilibili.com/video/BV1an4y1X7h5/)】

  

## 快速开始【以上为最小化安装的示范，不包含所有功能及特点】
### 只 ComfyUI 的安装示范
### 包含 ComfyUI + ComfyUI Manager + Ngrok + 国内环境可安装

1. **克隆仓库**：
    ```bash
             git clone https://github.com/aigem/aitools.git
    国内使用：git clone https://openi.pcl.ac.cn/niubi/aitools.git
    cd aitools
    ```

2. **运行安装脚本**：
    ```bash
    bash aitools.sh
    ```

3. **其它说明**：
    - 在菜单中选择选项 1 (ComfyUI) 开始安装
    - 启动服务

## 安装流程详解

安装过程分为以下几个主要阶段：

1. **环境准备**：
   - 创建工作目录结构
   - 复制必要的配置文件和脚本
   - 初始化日志系统

2. **Conda 环境配置**：
   - 创建专用的 conda 环境
   - 安装基础 Python 包
   - 配置环境变量

3. **CUDA 和 PyTorch 设置**：
   - 检测 CUDA 版本
   - 安装匹配的 PyTorch 版本
   - 配置 CUDA 环境变量

4. **ComfyUI 安装**：
   - 克隆 ComfyUI 代码库
   - 安装依赖包
   - 配置运行环境

5. **模型下载**：
   - 支持从国内镜像源下载模型
   - 自动创建模型目录结构
   - 支持断点续传

6. **服务启动**：
   - 配置服务运行参数
   - 启动 ComfyUI 服务
   - 设置自动重启

## 目录结构

```bash
comfyui-cn/
├── aitools.sh              # 主入口脚本
├── scripts/               # 功能脚本目录
│   ├── comfyui_setup.sh   # ComfyUI 安装主脚本
│   ├── conda.sh           # Conda 环境配置脚本
│   ├── cuda-pytorch_update.sh  # CUDA/PyTorch 更新脚本
│   ├── download.sh        # 模型下载脚本
│   └── run.sh            # 服务启动脚本
├── utils/                # 工具脚本目录
│   ├── init.sh           # 初始化脚本
│   ├── log_utils.sh      # 日志工具
│   └── progress.sh       # 进度管理工具
└── config/               # 配置文件目录
    ├── comfyui_config.sh # ComfyUI 配置文件
    └── supervisord.conf  # 服务监控配置
```

## 配置说明

- **工作目录**：默认为 `/workspace`，可在 `config/comfyui_config.sh` 中修改
- **日志目录**：`${WORK_DIR}/logs`，记录所有安装和运行日志
- **模型目录**：`${WORK_DIR}/models`，存放下载的模型文件
- **配置文件**：`${WORK_DIR}/config`，包含所有配置文件

## 常见问题

1. **安装过程中断**
    - 安装程序支持断点续传，重新运行脚本即可从中断处继续
    - 检查 `${WORK_DIR}/logs` 目录下的日志文件以排查问题

2. **conda 命令未找到**
    - 确保已正确安装 Miniconda 或 Anaconda
    - 运行 `source ~/.bashrc` 刷新环境变量

3. **CUDA 相关错误**
    - 确保已安装 NVIDIA 驱动
    - 运行 `nvidia-smi` 检查 GPU 状态
    - 检查 CUDA 版本与 PyTorch 版本是否匹配

4. **模型下载失败**
    - 检查网络连接
    - 尝试使用其他镜像源
    - 使用 `scripts/download.sh` 单独下载模型

5. **服务启动失败**
    - 检查端口是否被占用
    - 查看 `${WORK_DIR}/logs` 下的服务日志
    - 确认 Python 环境和依赖是否正确安装

## 维护和更新

- **更新软件**：
    ```bash
    git pull
    bash aitools.sh
    ```
    选择选项 1 重新安装即可

- **清理安装**：
    ```bash
    bash aitools.sh
    ```
    选择选项 5 进行清理

## 贡献指南

欢迎提交 [Issue](https://github.com/aigem/aitools/issues) 和 [Pull Request](https://github.com/aigem/aitools/pulls)。

在提交之前，请：
1. 检查现有 Issue 是否已报告相同问题
2. 遵循项目的代码风格
3. 提供详细的描述和复现步骤


## 联系方式

- **项目主页**：[GitHub](https://github.com/aigem/aitools)
- **问题反馈**：[Issues](https://github.com/aigem/aitools/issues)