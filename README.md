# AI For U

在主流免费算力平台上一键安装 AI For U，并支持国内模型的下载。本项目旨在提供一个高效、便捷的 AI For U 安装与配置解决方案。

【获取[强化版一键安装脚本](https://gf.bilibili.com/item/detail/1107198073)】

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

【注意】：强化版一键安装脚本，支持更多功能，请参考 [why_plus.md](docs/why_plus.md)
【获取[强化版一键安装脚本](https://gf.bilibili.com/item/detail/1107198073)】
  

## 快速开始【以上为最小化安装的示范，不包含所有功能及特点】
### 只 ComfyUI 的安装示范
### 包含 ComfyUI + ComfyUI Manager + Ngrok + 国内环境可安装

1. **克隆仓库**：
    ```bash
             git clone https://github.com/aigem/aitools.git
    国内使用：git clone https://openi.pcl.ac.cn/niubi/aitools.git
             git clone https://gitee.com/fuliai/aitools.git
    cd aitools
    ```

2. **运行安装脚本**：
    ```bash
    bash aitools.sh
    ```
    在菜单中选择选项 1 (ComfyUI) 开始自动安装

3. **运行说明**： 

    - 启动ComfyUI服务
    `cd /workspace/ComfyUI/ && python main.py`
    - 启动 Ngrok 隧道服务
    在另一个终端运行 `ngrok http 8188` 运行 Ngrok 隧道服务
