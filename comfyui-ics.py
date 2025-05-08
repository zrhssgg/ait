import marimo

__generated_with = "0.10.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import subprocess
    import os
    import logging
    from datetime import datetime
    return datetime, logging, mo, os, subprocess


@app.cell
def _(mo):
    """UI 组件：工具选择"""
    ai_app = "comfyui"
    aitool_name = mo.ui.dropdown(
        [f"{ai_app}"], 
        value=f"{ai_app}",
        label="选择AI工具"
    )
    return ai_app, aitool_name


@app.cell
def _(aitool_name):
    """虚拟环境所在文件夹、git REPO等常规变量设置"""
    uv_venv_dir = f"ai_{aitool_name.value}"
    git_repo_url = "https://openi.pcl.ac.cn/niubi/ComfyUI.git"
    repo_name = f"{aitool_name.value}"
    app_log = f"{aitool_name.value}.log"
    python_ver = "3.12.8"

    custom_node_1 = "comfyui-manager"
    custom_node_1_repo = "https://openi.pcl.ac.cn/niubi/comfyui-manager.git"
    return (
        app_log,
        custom_node_1,
        custom_node_1_repo,
        git_repo_url,
        python_ver,
        repo_name,
        uv_venv_dir,
    )


@app.cell
def _(custom_node_1, custom_node_1_repo, python_ver):
    """配置类"""
    class Config:
        SYSTEM_DEPS = [
            {
                "name": "系统依赖",
                "cmd": """
                apt-get update
                apt install build-essential libgl1 ffmpeg python3-pip aria2 git git-lfs htop -y
                pip install uv -i https://mirrors.cloud.tencent.com/pypi/simple
                """
            }
        ]

        @staticmethod
        def get_venv_commands(venv_dir):
            return [
                {
                    "name": "虚拟环境设置",
                    "cmd": f"""
                    if [ ! -d "{venv_dir}" ]; then
                        mkdir -p {venv_dir}
                    fi
                    cd {venv_dir}
                    if [ ! -d ".venv" ]; then
                        uv venv --seed -p {python_ver}
                    fi
                    . .venv/bin/activate
                    uv pip install setuptools wheel -i https://mirrors.cloud.tencent.com/pypi/simple
                    uv pip install "numpy<2.0" -i https://mirrors.cloud.tencent.com/pypi/simple
                    uv pip install -U huggingface_hub aria2 insightface -i https://mirrors.cloud.tencent.com/pypi/simple
                    """
                }
            ]

        @staticmethod
        def setup_repo_commands(venv_dir, git_url, repo_name):
            return [
                {
                    "name": f"处理{repo_name}项目仓库",
                    "cmd": f"""
                    cd {venv_dir}
                    . .venv/bin/activate
                    if [ -d "{repo_name}" ]; then
                        echo "更新仓库..."
                        cd {repo_name}
                        git pull
                    else
                        echo "克隆仓库..."
                        git clone {git_url} {repo_name}
                        cd {repo_name}
                    fi
                    uv pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
                    """
                },
                {
                    "name": f"安装{custom_node_1}",
                    "cmd": f"""

                    cd {venv_dir}
                    . .venv/bin/activate
                    cd {repo_name}/custom_nodes
                    if [ -d "{custom_node_1}" ]; then
                        echo "更新仓库..."
                        cd {custom_node_1}
                        git pull
                    else
                        echo "克隆仓库..."
                        git clone {custom_node_1_repo} {custom_node_1}
                        cd {custom_node_1}
                    fi
                    uv pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
                    """
                }
            ]

        @staticmethod
        def get_start_command(venv_dir, repo_name, app_log):
            """获取启动命令"""
            return {
                "name": "启动服务",
                "cmd": f"""
                cd {venv_dir}
                . .venv/bin/activate
                cd {repo_name}
                export HF_ENDPOINT=https://hf-mirror.com
                nohup python main.py > ../../{app_log} 2>&1 &
                """,
                "check_cmd": "ps aux | grep 'python main.py' | grep -v grep"
            }

        @staticmethod
        def get_stop_commands():
            """获取停止命令"""
            return [
                {
                    "name": "停止服务",
                    "cmd": "pkill -f 'python main.py'",
                    "check_cmd": "ps aux | grep 'python main.py' | grep -v grep"
                }
            ]

        @staticmethod
        def download_commands(venv_dir, repo_name):
            return [
                {
                    "name": "模型下载",
                    "cmd": f"""
                    echo "请按需进行模型下载，使用方法请参考视频教程"
                    echo "如有需要，请加群交流 https://fuliai-ai2u.hf.space/"
                    """
                }
            ]

        @staticmethod
        def get_end_show_info(venv_dir, repo_name):
            """获取安装完成后的展示信息"""
            return f"""
            ## 安装完成后的操作说明

            Q&A及资讯:
            - 最新资讯及相关命令请查看 https://fuliai-ai2u.hf.space/
            - 加群交流：https://qr61.cn/oohivs/qRp62U6

            ## 启动程序

            ```bash
            /workspace/apps/ksa/ksa_x64
            cd {venv_dir} && source .venv/bin/activate && cd {repo_name} && export HF_ENDPOINT=https://hf-mirror.com && python main.py
            ```
            之后使用ksa连接，在浏览器中使用 10.0.0.1:8188 来访问ai程序。
            不会用的请查看视频教程：https://www.bilibili.com/video/BV13UBRYVEmX/

            ## 退出程序
            ```bash
            （使用 Ctrl + C）
            ```
            """
    return (Config,)


@app.cell
def _(datetime, logging, os):
    """日志处理类"""
    class Logger:
        def __init__(self, name):
            self.logger = self._setup_logger(name)

        def _setup_logger(self, name):
            os.makedirs("logs", exist_ok=True)
            log_file = f'logs/{name}_{datetime.now().strftime("%Y%m%d")}.log'

            logger = logging.getLogger(name)
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler(log_file, encoding="utf-8"),
                    logging.StreamHandler(),
                ],
            )
            return logger

        def info(self, msg): self.logger.info(msg)
        def error(self, msg): self.logger.error(msg)
        def warning(self, msg): self.logger.warning(msg)
    return (Logger,)


@app.cell
def _(mo):
    """UI 组件：功能开关"""
    switches = {
        "system": mo.ui.switch(label="系统依赖安装", value=True),
        "venv": mo.ui.switch(label="虚拟环境设置", value=True),
        "repo": mo.ui.switch(label="程序文件设置", value=True),
        "app": mo.ui.switch(label="启动应用程序", value=True),
        "download": mo.ui.switch(label="文件或模型下载", value=True),
    }
    return (switches,)


@app.cell
def _(Logger, aitool_name):
    """初始化日志记录器"""
    logger = Logger(aitool_name.value)
    return (logger,)


@app.cell
def _(subprocess):
    """命令执行工具类"""
    class CommandRunner:
        @staticmethod
        def run(cmd, logger, check=True, step_name=""):
            try:
                prefix = f"[{step_name}] " if step_name else ""
                logger.info(f"{prefix}正在执行命令...")
                result = subprocess.run(
                    cmd,
                    shell=True,
                    check=check,
                    text=True,
                    capture_output=True
                )
                if result.stdout:
                    logger.info(f"{prefix}输出: {result.stdout.strip()}")
                logger.info(f"{prefix}命令执行成功")
                return True, None
            except subprocess.CalledProcessError as e:
                error_msg = f"{prefix}命令执行失败: {e.stderr if e.stderr else '未知错误'}"
                logger.error(error_msg)
                return False, error_msg
            except KeyboardInterrupt:
                logger.info(f"{prefix}用户中断了命令执行")
                return False, "用户中断了命令执行"
            except Exception as e:
                error_msg = f"{prefix}执行出错: {str(e)}"
                logger.error(error_msg)
                return False, error_msg
    return (CommandRunner,)


@app.cell
def _(aitool_name):
    aitool_name
    return


@app.cell
def _(switches):
    switches
    return


@app.cell
def _(CommandRunner, Config, logger, mo, switches):
    """系统依赖安装"""
    def install_system():
        if not switches["system"].value:
            return mo.md("⚠️ 请先启用系统依赖安装").callout(kind="warn")

        for cmd_info in Config.SYSTEM_DEPS:
            success, error = CommandRunner.run(cmd_info["cmd"], logger, step_name=cmd_info["name"])
            if not success:
                return mo.md(f"❌ {error}").callout(kind="danger")

        return mo.md("✅ 系统依赖安装完成").callout(kind="success")

    install_system()
    return (install_system,)


@app.cell
def _(CommandRunner, Config, logger, mo, os, switches, uv_venv_dir):
    """虚拟环境设置"""
    def setup_venv():
        if not switches["venv"].value:
            return mo.md("⚠️ 请先启用虚拟环境设置").callout(kind="warn")

        os.makedirs(uv_venv_dir, exist_ok=True)

        for cmd_info in Config.get_venv_commands(uv_venv_dir):
            success, error = CommandRunner.run(cmd_info["cmd"], logger, step_name=cmd_info["name"])
            if not success:
                return mo.md(f"❌ {error}").callout(kind="danger")

        return mo.md("✅ 虚拟环境设置完成").callout(kind="success")

    setup_venv()
    return (setup_venv,)


@app.cell
def _(
    CommandRunner,
    Config,
    git_repo_url,
    logger,
    mo,
    repo_name,
    switches,
    uv_venv_dir,
):
    """程序文件安装设置"""
    def setup_repo():
        if not switches["repo"].value:
            return mo.md("⚠️ 请先启用文件安装设置").callout(kind="warn")

        for cmd_info in Config.setup_repo_commands(uv_venv_dir, git_repo_url, repo_name):
            success, error = CommandRunner.run(cmd_info["cmd"], logger, step_name=cmd_info["name"])
            if not success:
                return mo.md(f"❌ {error}").callout(kind="danger")

        return mo.md("✅ 程序文件设置完成").callout(kind="success")

    setup_repo()
    return (setup_repo,)


@app.cell
def _(
    CommandRunner,
    Config,
    end_show,
    logger,
    mo,
    post_end_show,
    repo_name,
    switches,
    uv_venv_dir,
):
    """下载：文件或模型"""
    def download_files():
        if not switches["download"].value:
            return mo.md("⚠️ 请先启用下载开关").callout(kind="warn")

        try:
            for cmd_info in Config.download_commands(uv_venv_dir, repo_name):
                success, error = CommandRunner.run(cmd_info["cmd"], logger, step_name=cmd_info["name"])
                if not success:
                    return mo.md(f"❌ {error}").callout(kind="danger")

            # 显示下载完成信息
            download_success = mo.md("✅ 相关下载已经完成").callout(kind="success")
            # 显示安装完成信息
            install_info = end_show()
            post_info = post_end_show()

            return mo.hstack([download_success, install_info, post_info])
        except KeyboardInterrupt:
            logger.info("用户中断了下载过程")
            return mo.md("⚠️ 下载已被用户中断").callout(kind="warn")
        except Exception as e:
            logger.error(f"下载过程出错: {str(e)}")
            return mo.md(f"❌ 下载出错: {str(e)}").callout(kind="danger")

    download_files()
    return (download_files,)


@app.cell
def _(Config, mo, repo_name, uv_venv_dir):
    """主体完成后展示信息内容"""
    def end_show():
        return mo.md(Config.get_end_show_info(uv_venv_dir, repo_name)).callout(kind="success")
    return (end_show,)


@app.cell
def _(Config, mo, ai_app,  uv_venv_dir):
    """将主体完成后展示信息内容写入说明文件"""
    def post_end_show():
        # 获取说明信息内容
        info_content = Config.get_end_show_info(uv_venv_dir, ai_app)

        # 写入说明文件
        try:
            with open(f"{ai_app}说明文件.md", "w", encoding="utf-8") as f:
                f.write(info_content)
            return mo.md(f"✅ 安装成功，使用说明已写入 {ai_app}说明文件.md").callout(kind="success")
        except Exception as e:
            return mo.md(f"❌ 写入说明文件失败: {str(e)}").callout(kind="danger")
    return (post_end_show,)


@app.cell
def _(mo):
    """创建启动和停止按钮"""
    btn = mo.ui.run_button(label="启动服务", kind="info")
    btn1 = mo.ui.run_button(label="停止服务", kind="info")
    return btn, btn1


@app.cell
def _(btn):
    btn
    return


@app.cell
def _(btn1):
    btn1
    return


@app.cell
def _(
    Config,
    app_log,
    btn,
    btn1,
    logger,
    repo_name,
    subprocess,
    switches,
    uv_venv_dir,
):
    """启动/停止应用程序"""
    def handle_app():
        if not switches["app"].value:
            print("⚠️ 请先启用应用程序开关")
            return

        if btn.value:
            # 获取启动配置
            start_config = Config.get_start_command(uv_venv_dir, repo_name, app_log)

            # 检查是否已有进程在运行
            check_result = subprocess.run(start_config["check_cmd"], shell=True)
            if check_result.returncode == 0:
                print("⚠️ 程序已在运行中")
                return

            # 启动服务
            logger.info("[启动服务] 正在启动应用程序...")
            subprocess.run(start_config["cmd"], shell=True)
            print("✅ 程序启动命令已执行")

        elif btn1.value:
            # 获取停止配置
            stop_config = Config.get_stop_commands()[0]

            # 停止服务
            logger.info("[停止服务] 正在停止应用程序...")
            subprocess.run(stop_config["cmd"], shell=True)
            print("✅ 程序停止命令已执行")

    handle_app()
    return (handle_app,)


if __name__ == "__main__":
    app.run()
