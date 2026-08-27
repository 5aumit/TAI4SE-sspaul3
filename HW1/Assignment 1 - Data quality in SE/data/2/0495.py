#对经fft变换的复数数据转换为极坐标形式
import numpy as np
import getopt
import sys

def main(argv):
    try:
         opts, args = getopt.getopt(sys.argv[1:], "-i:-o:-h", ["input=", "output=","help"])
    except getopt.GetoptError:
        print('将经过fft变换的音频数据，转换到极坐标')
        print('python ffttxtpolar.py -i fft_test1.txt -o fft_test1_polar.txt')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("将经过fft变换的音频数据，转换到极坐标")
            print('输入格式为：')
            print('python ffttxtpolar.py -i fft_test1.txt -o fft_test1_polar1.txt')
            print('此时幅度和相位以"@"间隔')
            print('python ffttxtpolar.py -i fft_test1.txt -o fft_test1_polar.txt')
            print('此时幅度和相位以空格间隔')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

            fft_data = np.loadtxt(input, dtype=np.complex)  #加载数据文件，读入数据
            fft_data_len = len(fft_data)  # 输入数据长度
            file = open(output, 'w+')  #打开输出文件

            for i in range(fft_data_len):
                #复数实部和虚部的平方和，再开方就是极坐标的幅度
                #Amplitude = np.abs(fft_data)  # 调包求模，即幅度
                #angle = np.rad2deg(np.angle(fft_data))  # 调包求相位，np.angle是求弧度，np.rad2deg将弧度转化为角度
                data_real = np.real(fft_data[i])  #取复数的实部
                data_imag = np.imag(fft_data[i])  #取复数的虚部
                Amplitude = np.sqrt(data_real ** 2 + data_imag ** 2) #求幅度，即模
                angle = np.arctan(data_imag / data_real )* (180 / np.pi)  # 求相位，此时为角度
                Amplitude_and_angle = str(Amplitude) + '@' + str(angle) + '\n'  #将幅度和相位数据中间加空格和@符号
                #Amplitude_and_angle = str(Amplitude) + ' ' + str(angle) + '\n'  # 将幅度和相位数据中间加空格
                file.write(Amplitude_and_angle)  #将每行数据写入文件
            file.close()


if __name__ == "__main__":
    main(sys.argv)  #调用函数


#python ffttxtpolar.py -i fft_test1.txt -o fft_test1_polar.txt
#python ffttxtpolar.py -i fft_test1.txt -o fft_test1_polar1.txt
