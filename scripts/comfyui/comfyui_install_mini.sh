#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_ROOT_DIR=$(dirname "$ROOT_DIR")"

# 导入初始化脚本
source "$ROOT_ROOT_DIR/utils/init.sh"

# 初始化环境
init_script

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
    log_info "ComfyUI 安装成功"
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
    log_info "ComfyUI Manager 安装成功"
}

# 主函数
main() {
    log_info "=== 开始 ComfyUI 安装流程 ==="
    
    # 更新系统包
    log_info "更新系统包..."
    apt update
    
    # 安装 ComfyUI
    install_comfyui || return 1
    
    # 安装 ComfyUI Manager
    install_manager || return 1
    
    # 显示安装信息
    log_info "=== ComfyUI 安装完成 ==="
    echo -e "${GREEN}安装位置: $WORK_DIR/$PROJECT_NAME${NC}"
    echo -e "${BLUE}启动命令: python $WORK_DIR/$PROJECT_NAME/main.py${NC}"
    echo -e "${BLUE}使用 ngrok 暴露端口: ngrok http $DEFAULT_PORT ${NC}"
    echo -e "${PURPLE}更详细说明:  https://1pages.nbid.bid ${NC}"
}

# 运行主程序
main
