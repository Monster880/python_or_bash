import os


def rename_file(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(dirs) #当前路径下所有子目录list
        print(files) #当前路径下所有非目录子文件 list

        # 1、先处理当前目录下的文件
        for file_name in files:
            if "【 微信号：itcodeba 】【微信公众号：全栈攻略】" in file_name:
                old_file_path = root + "/" + file_name
                new_file_name = file_name.replace('【 微信号：itcodeba 】【微信公众号：全栈攻略】', '')
                new_file_path = root + "/" + new_file_name
                os.rename(old_file_path, new_file_path)

        # 2、递归处理目录下的子目录及子目录中的文件
        for dir_name in dirs:
            old_dir_path = root + "/" + dir_name
            dir_path = old_dir_path
            rename_file(dir_path)




if __name__ == '__main__':
    path = '/Users/liding/Desktop/imooc-blog'
    rename_file(path)