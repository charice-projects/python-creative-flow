#!/usr/bin/env python3
"""
UTF-8文件服务器 - 修复版
解决：1. BytesIO导入问题 2. 端口占用问题
"""
import http.server
import socketserver
import os
import sys
import argparse
import io  # 添加这行！

class UTF8HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """专门处理UTF-8编码的请求处理器"""
    
    def send_head(self):
        """重写send_head以正确处理UTF-8文本文件"""
        path = self.translate_path(self.path)
        
        if os.path.isdir(path):
            return self.list_directory(path)
        
        ctype = self.guess_type(path)
        
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None
        
        try:
            self.send_response(200)
            
            # 对于文本文件，确保指定UTF-8编码
            if ctype.startswith('text/'):
                if 'charset=' not in ctype:
                    ctype = f"{ctype}; charset=utf-8"
            
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs.st_size))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
            return f
        except:
            f.close()
            raise
    
    def list_directory(self, path):
        """生成UTF-8编码的目录列表"""
        try:
            file_list = os.listdir(path)
        except OSError:
            self.send_error(404, "No permission to list directory")
            return None
        
        file_list.sort(key=lambda a: a.lower())
        
        # 构建HTML
        html = ['<!DOCTYPE HTML>']
        html.append('<html>')
        html.append('<head>')
        html.append('<meta charset="utf-8">')
        html.append('<title>目录列表</title>')
        html.append('</head>')
        html.append('<body>')
        html.append(f'<h1>目录列表: {os.path.basename(path)}</h1>')
        html.append('<hr>')
        html.append('<ul>')
        
        # 添加父目录链接
        if path != self.directory:
            parent = os.path.dirname(path)
            html.append(f'<li><a href="{self.get_parent_link(parent)}">../</a></li>')
        
        for name in file_list:
            fullname = os.path.join(path, name)
            displayname = name
            if os.path.isdir(fullname):
                displayname = name + "/"
                name = name + "/"
            
            # 转义HTML特殊字符
            displayname = displayname.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            name = name.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            
            html.append(f'<li><a href="{name}">{displayname}</a></li>')
        
        html.append('</ul>')
        html.append('<hr>')
        html.append('</body></html>')
        
        encoded = '\n'.join(html).encode('utf-8')
        
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        
        # 修复这里：使用 io.BytesIO
        return io.BytesIO(encoded)
    
    def get_parent_link(self, parent):
        """计算父目录链接"""
        rel_path = os.path.relpath(parent, self.directory)
        if rel_path == '.':
            return "/"
        else:
            return "/" + rel_path.replace("\\", "/") + "/"
    
    def guess_type(self, path):
        """猜测文件类型，为文本文件添加UTF-8编码"""
        base, ext = os.path.splitext(path)
        ext = ext.lower()
        
        text_types = {
            '.md': 'text/markdown',
            '.txt': 'text/plain',
            '.html': 'text/html',
            '.htm': 'text/html',
            '.json': 'application/json',
            '.yml': 'text/yaml',
            '.yaml': 'text/yaml',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.csv': 'text/csv',
            '.xml': 'text/xml',
        }
        
        if ext in text_types:
            return f"{text_types[ext]}; charset=utf-8"
        
        return super().guess_type(path)

def try_ports(start_port=8000, max_attempts=5):
    """尝试多个端口，直到找到可用的"""
    for port in range(start_port, start_port + max_attempts):
        try:
            return port, socketserver.TCPServer(("127.0.0.1", port), UTF8HTTPRequestHandler)
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"端口 {port} 被占用，尝试下一个...")
                continue
            raise
    return None, None

def main():
    parser = argparse.ArgumentParser(description='UTF-8文件服务器')
    parser.add_argument('--port', '-p', type=int, default=8000, help='首选端口 (默认: 8000)')
    parser.add_argument('--directory', '-d', default=os.getcwd(), help='服务目录 (默认: 当前目录)')
    
    args = parser.parse_args()
    
    # 切换到目标目录
    os.chdir(args.directory)
    
    print("=" * 60)
    print("UTF-8文件服务器 (修复版)")
    print(f"服务目录: {args.directory}")
    print("=" * 60)
    
    # 尝试启动服务器
    for port in range(args.port, args.port + 10):
        try:
            handler = UTF8HTTPRequestHandler
            # 创建允许地址复用的服务器
            class ReusableTCPServer(socketserver.TCPServer):
                allow_reuse_address = True
            
            server = ReusableTCPServer(("127.0.0.1", port), handler)
            print(f"✓ 服务器启动成功: http://127.0.0.1:{port}")
            print("按 Ctrl+C 停止服务器")
            print("-" * 60)
            print(f"新开一个终端 使用实际启动的端口 启动cloudflared遂穿")
            print(f"cloudflared tunnel --url http://127.0.0.1:{port}")
            print("=" * 60)
            
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print("\n服务器已停止")
                break
                
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"端口 {port} 被占用，尝试端口 {port + 1}...")
                continue
            else:
                print(f"错误: {e}")
                break

if __name__ == "__main__":
    main()