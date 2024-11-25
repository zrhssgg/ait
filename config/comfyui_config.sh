#!/bin/bash

# 基础配置
export WORK_DIR="/workspace"
export PROJECT_NAME="ComfyUI"
export CONDA_ENV_NAME="comfyui_env"
export PYTHON_VERSION="3.12"

# ngrok token
export NGROK_TOKEN=2oksbatronvXqC753wXOMSMFksS_3vtfJnM8YhEYaq896D4uR

# CUDA 和 PyTorch 更新开关
export CUDA_PYTORCH=false

# 模型下载开关
export DOWNLOAD_MODELS=false

# 目录配置
export LOG_DIR="$WORK_DIR/logs"
export MODELS_DIR="$WORK_DIR/$PROJECT_NAME/models"
export TMP_DIR="$WORK_DIR/tmp"
export BACKUP_DIR="$WORK_DIR/backups"

# 日志配置
export LOG_FILE="$LOG_DIR/install.log"
export LOG_LEVEL="INFO"  # DEBUG, INFO, WARNING, ERROR
export MAX_LOG_SIZE="10M"
export LOG_BACKUP_COUNT=5

# 网络配置
export DEFAULT_PORT=8188
export TIMEOUT=30
export MAX_RETRIES=3
export DOWNLOAD_THREADS=4

# 仓库配置
export REPO_URLS=(
    ["comfyui"]="https://openi.pcl.ac.cn/niubi/ComfyUI.git"
    ["manager"]="https://openi.pcl.ac.cn/niubi/comfyui-manager.git"
)

# 模型配置
export MODEL_VERSIONS=(
    ["sd_v15"]="v1-5-pruned-emaonly.safetensors"
    ["vae"]="vae-ft-mse-840000-ema-pruned.safetensors"
    ["controlnet"]="control_v11p_sd15_canny.pth"
)

# 系统要求
export MIN_DISK_SPACE=20  # GB
export MIN_MEMORY=8       # GB
export REQUIRED_CUDA="11.8"

# 功能开关
export ENABLE_AUTO_UPDATE=true
export ENABLE_BACKUP=true
export ENABLE_MONITORING=true 
