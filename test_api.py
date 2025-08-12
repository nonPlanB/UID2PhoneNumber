#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书UID转iPhone号码API测试脚本
"""

import requests
import json
import time

# API基础URL
BASE_URL = "http://localhost:5000"

def test_api_endpoints():
    """测试所有API端点"""
    print("=" * 50)
    print("小红书UID转iPhone号码API测试")
    print("=" * 50)
    
    # 测试1: 首页
    print("\n1. 测试首页...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"状态码: {response.status_code}")
        print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试2: 健康检查
    print("\n2. 测试健康检查...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"状态码: {response.status_code}")
        print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试3: API文档
    print("\n3. 测试API文档...")
    try:
        response = requests.get(f"{BASE_URL}/docs")
        print(f"状态码: {response.status_code}")
        print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试4: POST方式转换UID
    print("\n4. 测试POST方式转换UID...")
    test_uids = [
        "100000000",  # 特殊映射
        "123456789",  # 普通UID
        "987654321",  # 普通UID
        "555666777",  # 普通UID
    ]
    
    for uid in test_uids:
        try:
            data = {"uid": uid}
            response = requests.post(f"{BASE_URL}/convert", json=data)
            print(f"\nUID: {uid}")
            print(f"状态码: {response.status_code}")
            print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        except Exception as e:
            print(f"错误: {e}")
    
    # 测试5: GET方式转换UID
    print("\n5. 测试GET方式转换UID...")
    for uid in test_uids:
        try:
            response = requests.get(f"{BASE_URL}/convert/{uid}")
            print(f"\nUID: {uid}")
            print(f"状态码: {response.status_code}")
            print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        except Exception as e:
            print(f"错误: {e}")
    
    # 测试6: 错误情况测试
    print("\n6. 测试错误情况...")
    
    # 测试无效UID
    invalid_uids = [
        "",  # 空UID
        "abc123",  # 包含字母
        "123",  # 太短
        "12345678901234567890",  # 太长
    ]
    
    for uid in invalid_uids:
        try:
            data = {"uid": uid}
            response = requests.post(f"{BASE_URL}/convert", json=data)
            print(f"\n无效UID: '{uid}'")
            print(f"状态码: {response.status_code}")
            print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        except Exception as e:
            print(f"错误: {e}")
    
    # 测试空请求体
    try:
        response = requests.post(f"{BASE_URL}/convert", json={})
        print(f"\n空请求体")
        print(f"状态码: {response.status_code}")
        print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试不存在的端点
    try:
        response = requests.get(f"{BASE_URL}/nonexistent")
        print(f"\n不存在的端点")
        print(f"状态码: {response.status_code}")
        print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"错误: {e}")

def test_performance():
    """测试API性能"""
    print("\n" + "=" * 50)
    print("性能测试")
    print("=" * 50)
    
    # 测试批量转换性能
    test_uids = [str(i) for i in range(100000000, 100000010)]
    
    start_time = time.time()
    success_count = 0
    error_count = 0
    
    for uid in test_uids:
        try:
            data = {"uid": uid}
            response = requests.post(f"{BASE_URL}/convert", json=data)
            if response.status_code == 200:
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            error_count += 1
            print(f"请求失败: {e}")
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"总请求数: {len(test_uids)}")
    print(f"成功请求: {success_count}")
    print(f"失败请求: {error_count}")
    print(f"总耗时: {total_time:.2f}秒")
    print(f"平均响应时间: {total_time/len(test_uids)*1000:.2f}毫秒")

if __name__ == "__main__":
    print("开始测试小红书UID转iPhone号码API...")
    print("请确保API服务已启动在 http://localhost:5000")
    
    # 等待用户确认
    input("按回车键开始测试...")
    
    # 运行测试
    test_api_endpoints()
    test_performance()
    
    print("\n" + "=" * 50)
    print("测试完成！")
    print("=" * 50) 