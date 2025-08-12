#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书UID转iPhone号码API启动脚本
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 7):
        print("❌ 错误: 需要Python 3.7或更高版本")
        print(f"当前版本: {sys.version}")
        return False
    print(f"✅ Python版本检查通过: {sys.version}")
    return True

def install_requirements():
    """安装依赖包"""
    print("📦 检查并安装依赖包...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 依赖包安装完成")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 依赖包安装失败: {e}")
        return False

def check_files():
    """检查必要文件是否存在"""
    required_files = ["UID2Phone.py", "requirements.txt"]
    missing_files = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ 缺少必要文件: {', '.join(missing_files)}")
        return False
    
    print("✅ 文件检查通过")
    return True

def start_server():
    """启动API服务器"""
    print("🚀 启动小红书UID转iPhone号码API服务...")
    print("📍 服务地址: http://localhost:5000")
    print("📖 API文档: http://localhost:5000/docs")
    print("💚 健康检查: http://localhost:5000/health")
    print("=" * 50)
    print("按 Ctrl+C 停止服务")
    print("=" * 50)
    
    try:
        # 导入并运行主应用
        from UID2Phone import app
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\n🛑 服务已停止")
    except Exception as e:
        print(f"❌ 启动服务失败: {e}")
        return False
    
    return True

def main():
    """主函数"""
    print("=" * 50)
    print("小红书UID转iPhone号码API启动器")
    print("=" * 50)
    
    # 检查Python版本
    if not check_python_version():
        sys.exit(1)
    
    # 检查文件
    if not check_files():
        sys.exit(1)
    
    # 安装依赖
    if not install_requirements():
        sys.exit(1)
    
    # 启动服务器
    start_server()

if __name__ == "__main__":
    main() 