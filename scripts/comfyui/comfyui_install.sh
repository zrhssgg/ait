#!/bin/bash

# 文件名: comfyui_install.sh
# 描述: 安装 ComfyUI 及其管理器
# 作者: ai来事
# 用法:
# bash comfyui_install.sh

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# 导入初始化脚本
source "$ROOT_DIR/utils/init.sh"

# 初始化环境
init_script

# 确保在正确的 conda 环境中
ensure_conda_env

# 检查工作目录
if [ ! -d "$WORK_DIR" ]; then
    log_error "工作目录 $WORK_DIR 不存在"
    exit 1
fi

# 安装ComfyUI
install_comfyui() {
    local repo_url="https://openi.pcl.ac.cn/niubi/ComfyUI.git"
    local target_dir="$WORK_DIR/$PROJECT_NAME"
    
    log_info "开始安装 ComfyUI..."
    
    if [ -d "$target_dir" ]; then
        log_info "更新现有的 ComfyUI 安装..."
        cd "$target_dir"
        git pull
    else
        log_info "克隆 ComfyUI 仓库..."
        git clone "$repo_url" "$target_dir"
        cd "$target_dir"
    fi
    
    log_info "安装 ComfyUI 依赖..."
    pip install -r requirements.txt
    pip install aria2
    
    if [ $? -eq 0 ]; then
        log_info "ComfyUI 安装成功"
    else
        log_error "ComfyUI 依赖安装失败"
        return 1
    fi
}

# 安装 comfyui-manager
install_manager() {
    local repo_url="https://openi.pcl.ac.cn/niubi/comfyui-manager.git"
    local target_dir="$WORK_DIR/$PROJECT_NAME/custom_nodes/comfyui-manager"
    
    log_info "开始安装 ComfyUI Manager..."
    
    mkdir -p "$(dirname "$target_dir")"
    
    if [ -d "$target_dir" ]; then
        log_info "更新现有的 ComfyUI Manager..."
        cd "$target_dir"
        git pull
    else
        log_info "克隆 ComfyUI Manager 仓库..."
        git clone "$repo_url" "$target_dir"
        cd "$target_dir"
    fi
    
    log_info "安装 ComfyUI Manager 依赖..."
    pip install -r requirements.txt
    
    if [ $? -eq 0 ]; then
        log_info "ComfyUI Manager 安装成功"
    else
        log_error "ComfyUI Manager 依赖安装失败"
        return 1
    fi
}

# 主函数
main() {
    log_info "=== 开始 ComfyUI 安装流程 ==="
    
    # 更新系统包
    log_info "更新系统包..."
    apt update && apt upgrade -y
    
    # 安装 ComfyUI
    install_comfyui || exit 1
    
    # 安装 ComfyUI Manager
    install_manager || exit 1
    
    # 显示安装信息
    log_info "=== ComfyUI 安装完成 ==="
    echo -e "${GREEN}安装位置: $WORK_DIR/$PROJECT_NAME${NC}"
    echo -e "${BLUE}启动命令: python $WORK_DIR/$PROJECT_NAME/main.py${NC}"
}

# 运行主程序
main
