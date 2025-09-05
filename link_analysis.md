# 链接解析原理分析

## 不同链接类型的行为

### 场景：当前页面在子路径
当前页面：`http://172.16.10.94:9080/system/_owners/yukaicheng_lab/_webprj/index.html`

### 1. 绝对路径链接（会出错）
```html
<a href="/people.html">People</a>
```
**结果：** `http://172.16.10.94:9080/people.html` ❌
**问题：** 丢失了子路径部分，跳转到服务器根目录

### 2. 相对路径链接 - 当前目录（修复前）
```html
<a href="./people.html">People</a>
```
**结果：** `http://172.16.10.94:9080/system/_owners/yukaicheng_lab/_webprj/people.html` ✅
**状态：** 实际上是正确的！

### 3. 相对路径链接 - 同级文件（修复后）
```html
<a href="people.html">People</a>
```
**结果：** `http://172.16.10.94:9080/system/_owners/yukaicheng_lab/_webprj/people.html` ✅
**状态：** 也是正确的！

## 为什么修复有效？

实际上 `./people.html` 和 `people.html` 在这种情况下都应该工作。
修复可能解决的是其他问题：
1. 某些服务器对 `./` 前缀处理不一致
2. 缓存问题
3. 其他HTML结构问题

## 最佳实践
对于子路径部署：
- ✅ 使用相对路径：`people.html`
- ✅ 使用Jekyll的 `{{ site.baseurl }}` 
- ❌ 避免绝对路径：`/people.html`
