# 小红书UID转iPhone号码API

一个将小红书用户UID转换为对应iPhone号码的RESTful API接口。

## 功能特性

- 🔄 **UID转手机号**: 将小红书用户UID转换为符合中国大陆格式的手机号
- 🌐 **RESTful API**: 提供标准的REST API接口
- 📝 **完整文档**: 内置API文档和示例
- 🛡️ **错误处理**: 完善的参数验证和错误处理机制
- 📊 **日志记录**: 详细的操作日志记录
- ⚡ **高性能**: 基于哈希算法的快速转换
- 🔧 **易于部署**: 简单的Flask应用，易于部署和维护

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动API服务

```bash
python UID2Phone.py
```

服务将在 `http://localhost:5000` 启动

### 3. 测试API

```bash
python test_api.py
```

## API接口文档

### 基础信息

- **服务地址**: `http://localhost:5000`
- **API版本**: 1.0.0
- **数据格式**: JSON

### 接口列表

#### 1. 首页
- **URL**: `/`
- **方法**: `GET`
- **描述**: 获取API基本信息和使用说明

#### 2. 转换UID为手机号 (POST)
- **URL**: `/convert`
- **方法**: `POST`
- **描述**: 通过POST请求转换UID为手机号

**请求参数**:
```json
{
    "uid": "100000000"
}
```

**响应示例**:
```json
{
    "success": true,
    "uid": "100000000",
    "phone": "13800138000",
    "timestamp": "2024-01-01T12:00:00"
}
```

#### 3. 转换UID为手机号 (GET)
- **URL**: `/convert/<uid>`
- **方法**: `GET`
- **描述**: 通过URL参数转换UID为手机号

**示例**: `GET /convert/100000000`

#### 4. 健康检查
- **URL**: `/health`
- **方法**: `GET`
- **描述**: 检查API服务状态

#### 5. API文档
- **URL**: `/docs`
- **方法**: `GET`
- **描述**: 获取完整的API文档

## 使用示例

### Python示例

```python
import requests

# POST方式转换
def convert_uid_post(uid):
    url = "http://localhost:5000/convert"
    data = {"uid": uid}
    response = requests.post(url, json=data)
    return response.json()

# GET方式转换
def convert_uid_get(uid):
    url = f"http://localhost:5000/convert/{uid}"
    response = requests.get(url)
    return response.json()

# 使用示例
result = convert_uid_post("100000000")
print(result)
```

### cURL示例

```bash
# POST方式
curl -X POST http://localhost:5000/convert \
  -H "Content-Type: application/json" \
  -d '{"uid": "100000000"}'

# GET方式
curl http://localhost:5000/convert/100000000
```

### JavaScript示例

```javascript
// POST方式
async function convertUID(uid) {
    const response = await fetch('http://localhost:5000/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({uid: uid})
    });
    return await response.json();
}

// 使用示例
convertUID('100000000').then(result => {
    console.log(result);
});
```

## 转换算法说明

### 核心算法

1. **UID验证**: 检查UID是否为9-12位纯数字
2. **特殊映射**: 检查是否有预定义的特殊映射规则
3. **哈希转换**: 使用MD5哈希算法处理UID
4. **前缀选择**: 根据哈希值选择手机号前缀
5. **后缀生成**: 使用哈希值生成手机号后缀
6. **格式验证**: 确保生成的手机号符合中国大陆格式

### 手机号格式

- **长度**: 11位数字
- **前缀**: 符合中国大陆运营商号段
- **格式**: 1 + 3位运营商代码 + 7位用户号码

### 支持的运营商号段

- **中国移动**: 130-139, 150-159, 180-189, 145, 147, 166, 167, 1703, 1705, 1706, 1349
- **中国联通**: 130-139, 150-159, 180-189, 145, 147, 166, 167, 1704, 1707-1709, 176, 175
- **中国电信**: 133-139, 150-159, 180-189, 145, 147, 166, 167, 1700-1702, 177, 173

## 错误处理

### 常见错误码

- **400**: 请求参数错误
- **404**: 接口不存在
- **500**: 服务器内部错误

### 错误响应格式

```json
{
    "success": false,
    "error": "错误描述",
    "timestamp": "2024-01-01T12:00:00"
}
```

### 常见错误

1. **UID格式错误**: UID必须是9-12位纯数字
2. **UID为空**: 请求中未提供UID参数
3. **转换失败**: 算法无法生成有效手机号

## 日志记录

API会自动记录以下信息：

- 请求日志
- 转换成功/失败记录
- 错误信息
- 性能统计

日志文件: `uid2phone_api.log`

## 性能优化

- 使用哈希算法确保快速转换
- 预定义特殊映射规则
- 备用算法处理异常情况
- 多线程支持

## 部署建议

### 生产环境部署

1. **使用WSGI服务器**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 UID2Phone:app
```

2. **使用Nginx反向代理**:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

3. **使用Docker部署**:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "UID2Phone.py"]
```

## 注意事项

1. **数据安全**: 此API仅用于演示目的，不保证转换结果的准确性
2. **隐私保护**: 请遵守相关法律法规，不要用于非法用途
3. **性能限制**: 建议在生产环境中添加适当的限流和缓存机制
4. **版本兼容**: 确保使用兼容的Python版本（建议3.7+）

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 联系方式

如有问题或建议，请通过GitHub Issues联系。 