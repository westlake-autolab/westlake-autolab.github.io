#!/usr/bin/env python3
"""
修复子路径部署中的链接问题
将绝对路径链接转换为相对路径链接
"""

import os
import re
import glob

def fix_html_links(file_path):
    """修复HTML文件中的链接"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. 修复导航链接（绝对路径 -> 相对路径）
    # /publications.html -> publications.html
    content = re.sub(r'href="/([^/][^"]*\.html)"', r'href="\1"', content)
    
    # 2. 修复根路径链接
    # href="/" -> href="index.html" (对于非首页)
    if 'index.html' not in file_path:
        content = re.sub(r'href="/"', r'href="index.html"', content)
    
    # 3. 修复 canonical 链接（需要完整URL或相对路径）
    content = re.sub(r'<link rel="canonical" href="/([^"]*)">', 
                    r'<link rel="canonical" href="\1">', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 修复了: {file_path}")
        return True
    else:
        print(f"⏭️  无需修复: {file_path}")
        return False

def main():
    """主函数"""
    print("🔧 开始修复子路径部署的链接问题...")
    
    # 查找所有HTML文件
    html_files = glob.glob("dist/**/*.html", recursive=True)
    
    fixed_count = 0
    for file_path in html_files:
        if fix_html_links(file_path):
            fixed_count += 1
    
    print(f"\n✨ 修复完成！共修复了 {fixed_count} 个文件")
    print("\n📝 修复内容：")
    print("   • 绝对路径链接 -> 相对路径链接")
    print("   • 根路径链接 -> index.html")
    print("   • canonical链接相对化")

if __name__ == "__main__":
    main()
