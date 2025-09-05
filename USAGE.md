# 网站使用指南

## 🎉 网站已成功配置！

你的学术网站现在已经完全配置好了，所有文件都在 `dist/` 目录中，使用相对路径，可以在任何环境下正常工作。

## 📁 目录结构

```
dist/
├── index.html          # 主页
├── publications.html   # 发表论文页面  
├── projects.html       # 项目展示页面
├── people.html         # 团队成员页面
├── news.html          # 新闻页面
├── join-us.html       # 加入我们页面
├── assets/            # 静态资源
│   ├── css/          # 样式文件
│   ├── js/           # JavaScript文件
│   └── img/          # 图片文件
└── 其他页面...
```

## 🚀 本地预览

### 方法1：Python HTTP服务器（推荐）
```bash
cd dist
python -m http.server 8080
```
然后访问：http://localhost:8080

### 方法2：使用其他HTTP服务器
```bash
# Node.js
npx http-server dist -p 8080

# PHP
cd dist && php -S localhost:8080
```

## 🌐 部署选项

### 1. GitHub Pages
1. 将 `dist/` 目录内容推送到 GitHub 仓库的 `gh-pages` 分支
2. 在仓库设置中启用 GitHub Pages

### 2. Netlify
1. 将 `dist/` 目录拖拽到 Netlify 部署页面
2. 或连接 GitHub 仓库，设置发布目录为 `dist`

### 3. Vercel
1. 导入 GitHub 仓库
2. 设置输出目录为 `dist`

### 4. 传统主机
直接将 `dist/` 目录内容上传到服务器的 web 根目录

## 🔧 更新网站内容

1. **修改内容**：编辑 `_data/`, `_pages/`, `_posts/` 等源文件
2. **重新构建**：运行 `bundle exec jekyll build --config _config_deploy.yml`
3. **测试**：在 `dist/` 目录启动本地服务器测试
4. **部署**：将更新后的 `dist/` 内容部署到你的托管平台

## ✅ 当前状态

- ✅ 网站已构建完成
- ✅ 所有路径已修复为相对路径
- ✅ 可以在任何环境下正常工作
- ✅ 本地服务器测试通过
- ✅ 准备好部署

## 🎯 下一步

你的网站现在已经完全准备好了！你可以：

1. 继续在本地预览和测试
2. 选择一个部署平台并上传 `dist/` 目录
3. 根据需要修改内容并重新构建

祝你的学术网站运行顺利！🚀
