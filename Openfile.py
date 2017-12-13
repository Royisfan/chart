import binascii


def read_file(file_path):
    file_data = open(file_path, 'rb')
    data = []  #使用列表存储打开的文件内容
    while True:
        file_one_data = file_data.read(2)  # 每次读取两个字节的文本，即16位的二进制数
        if not file_one_data:
            break
        hex_str = binascii.b2a_hex(file_one_data)   # 转化成16进制数
        dec_str = int(hex_str, 16)  # 转化成10进制数
        # binary_str = bin(int(hex_str, 16))[2:]   #转化成2进制数
        data.append(dec_str)  #向列表里添加
    file_data.close()
    return data


