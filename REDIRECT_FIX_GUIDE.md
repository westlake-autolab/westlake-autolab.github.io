# 重定向文件导致的首页样式问题解决方案

## 问题描述
网站首页通过JSP文件重定向到index.html，但由于缓存问题导致首页样式不能正常加载。

## 解决方案

### 方案1：修改服务器上的重定向文件
将服务器上的JSP重定向文件内容替换为：

```html
<html>
<head>
<title>Westlake AutoLab</title>
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<script>
// 添加时间戳强制刷新
var timestamp = new Date().getTime();
window.location.href = "./index.html?v=" + timestamp;
</script>
</head>
<body>
<p>Loading Westlake AutoLab...</p>
</body>
</html>
```

### 方案2：使用缓存清理页面
1. 上传 `clear-cache.html` 到服务器
2. 将重定向指向这个文件
3. 这个文件会强制清理缓存后跳转到index.html

### 方案3：服务器端重定向（推荐）
如果可以修改服务器配置，使用HTTP 301/302重定向而不是JavaScript重定向：

```apache
# Apache .htaccess
RedirectMatch 301 ^/$ /index.html

# 或者
RewriteEngine On
RewriteRule ^$ index.html [R=301,L]
```

```nginx
# Nginx
location = / {
    return 301 /index.html;
}
```

### 方案4：修改index.html缓存策略
已经在index.html中添加了缓存控制头：
```html
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
```

## 部署步骤
1. 上传修改后的index.html
2. 根据服务器类型选择合适的重定向方案
3. 清理浏览器缓存或使用强制刷新（Ctrl+F5）

## 验证方法
1. 访问网站根目录
2. 检查首页样式是否正常加载
3. 使用浏览器开发者工具检查CSS文件是否正确加载
