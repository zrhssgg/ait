#!/bin/bash

# 设置颜色变量
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 清屏函数
clear_screen() {
    clear
}

# 显示标题
show_title() {
    echo -e "${CYAN}"
    echo '    _    ___ _____ ___   ___  ____    _   _ '
    echo '   / \  |_ _|  ___/ _ \ | _ \|  _ \  | | | |'
    echo '  / _ \  | || |_ | | | ||   /| |_) | | | | |'
    echo ' / ___ \ | ||  _|| |_| || |\\ |  _ <  | |_| |'
    echo '/_/   \_\___|_|   \___/ |_| \_|_| \_\  \___/ '
    echo -e "${NC}"
    echo -e "${PURPLE}欢迎使用 AI For U 安装助手${NC}"
    echo "----------------------------------------"
}

# 显示菜单
show_menu() {
    echo -e "\n${GREEN}请选择要安装的 AI 工具：${NC}"
    echo "1) ComfyUI - AI工作流神器"
    echo "2) Chat TTS - AI 语音合成"
    echo "3) Open WebUI - 最强AI对话客户端"
    echo "4) 退出"
}

# 执行选择的操作
execute_choice() {
    case $1 in
        1)
            echo -e "\n${BLUE}正在启动 ComfyUI 安装程序...${NC}"
            if [ -f "./comfyui_setup.sh" ]; then
                bash ./comfyui_setup.sh
            else
                echo -e "${RED}未找到【 comfyui 】安装脚本${NC}"
                echo -e "${BLUE}获取脚本：https://gf.bilibili.com/item/detail/1107198073{NC}"
            fi
            ;;
        2)
            echo -e "\n${BLUE}正在启动 Chat TTS 安装程序...${NC}"
            echo -e "${PURPLE}此功能正在开发中...${NC}"
            ;;
        3)
            echo -e "\n${BLUE}正在启动 Open WebUI 安装程序...${NC}"
            if [ -f "./open-webui_setup.sh" ]; then
                bash ./open-webui_setup.sh
            else
                echo -e "${RED}未找到【 open-webui 】安装脚本${NC}"
                echo -e "${BLUE}获取脚本：https://gf.bilibili.com/item/detail/1107198073{NC}"
            fi
            ;;
        4)
            echo -e "\n${GREEN}感谢使用 ai来事|aitools 安装助手！${NC}"
            exit 0
            ;;
        *)
            echo -e "\n${GREEN}感谢使用 ai来事|aitools 安装助手！${NC}"
            echo -e "${RED}无效的选择，请重试${NC}"
            echo -e "${BLUE}详情请查看：https://gf.bilibili.com/item/detail/1107198073${NC}"
            ;;
    esac
}

# 主程序循环
main() {
    while true; do
        clear_screen
        show_title
        show_menu
        
        echo -e "\n${GREEN}请输入选项编号：${NC}"
        read choice
        
        execute_choice $choice
        
        echo -e "\n${BLUE}按回车键继续...${NC}"
        read
    done
}

# 运行主程序
main
