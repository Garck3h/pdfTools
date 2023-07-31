import base64
import os
import argparse
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


def extract_pages(input_path, output_path, start_page=0, end_page=None):
    # 创建输出目录
    os.makedirs(output_path, exist_ok=True)

    # 遍历输入目录中的所有PDF文件
    for filename in os.listdir(input_path):
        if filename.endswith('.pdf'):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename)

            # 打开PDF文件
            with open(input_file, 'rb') as file:
                pdf = PdfReader(file)

                # 创建一个新的PDF写入对象
                output_pdf = PdfWriter()

                # 设置提取的起始页和结束页
                if end_page is None:
                    end_page = len(pdf.pages)
                start_page = min(max(start_page, 0), len(pdf.pages) - 1)
                end_page = min(max(end_page, start_page + 1), len(pdf.pages))

                # 提取指定范围的页
                for i in range(start_page, end_page):
                    output_pdf.add_page(pdf.pages[i])

                # 将提取的页面保存为新的PDF文件
                with open(output_file, 'wb') as output:
                    output_pdf.write(output)

            print(f"提取完成：{output_file}")


def merge_pdfs(input_path, output_file):
    # 创建一个PdfMerger对象
    merger = PdfMerger()

    # 遍历输入目录中的所有PDF文件
    for filename in os.listdir(input_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(input_path, filename)

            # 将PDF文件添加到merger对象中
            merger.append(file_path)

    # 合并PDF文件
    merger.write(output_file)
    merger.close()

    print(f"合并完成：{output_file}")


def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='PDF处理工具')

    # 添加命令行参数
    parser.add_argument('-m', '--mode', help='选择功能：t - 批量提取前四页，b - 合并指定文件夹的PDF', required=True)
    parser.add_argument('-i', '--input', help='输入文件夹路径', required=True)
    parser.add_argument('-o', '--output', help='输出文件夹/文件路径', required=True)
    parser.add_argument('-ps', '--start_page', type=int, help='提取范围的起始页（仅适用于提取功能）')
    parser.add_argument('-pe', '--end_page', type=int, help='提取范围的结束页（仅适用于提取功能）')

    # 解析命令行参数
    args = parser.parse_args()

    # 根据参数选择功能
    if args.mode == 't':
        extract_pages(args.input, args.output, start_page=0, end_page=4)
    elif args.mode == 'b':
        merge_pdfs(args.input, args.output)
    else:
        print('无效的模式参数！')


if __name__ == '__main__':
    print("pdfTools v1.0 by Garck3h")
    logo_encode = 'CiAgICAgICAgICAgICAgXyAgX18gXyAgICAgICAgICAgICAgXyAgICAgCiAgICAgXyBfXyAgIF9ffCB8LyBffCB8XyBfX18gICBfX18gfCB8X19fIAogICAgfCAnXyBcIC8gX2AgfCB8X3wgX18vIF8gXCAvIF8gXHwgLyBfX3wKICAgIHwgfF8pIHwgKF98IHwgIF98IHx8IChfKSB8IChfKSB8IFxfXyBcCiAgICB8IC5fXy8gXF9fLF98X3wgIFxfX1xfX18vIFxfX18vfF98X19fLwogICAgfF98CiAgICA='
    # 解码base64编码的logo
    decoded_logo_bytes = base64.b64decode(logo_encode)
    # 将解码后的字节转换为字符串
    decoded_logo = decoded_logo_bytes.decode('utf-8')
    print(decoded_logo)
    main()
