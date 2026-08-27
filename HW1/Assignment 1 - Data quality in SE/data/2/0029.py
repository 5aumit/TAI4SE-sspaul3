#!usr/bin/env python
# -*- coding:utf-8 _*

"""
@File : build_model_2.py
@Author : ljt
@Description: xx
@Time : 2021/6/12 21:46 
"""


import numpy as np
import SimpleITK as sitk
import skimage.restoration.deconvolution
from numpy.fft import fftn, ifftn


new_img = sitk.ReadImage("../../data/ground_data/new_img.nii")
spacing = new_img.GetSpacing()
# 原始SimpleITK数据的存储形式为(Width, Height, Depth)即（X，Y，Z）
# 使用GetArrayFromImage()方法后，X轴与Z轴发生了对调
# 输出形状为：(Depth, Height, Width)即（Z,Y,X）。
new_img_array = sitk.GetArrayFromImage(new_img)

model_img_array = np.zeros((new_img_array.shape))


# [10, 19, 14]
# [15, 16, 12]
# [20, 25, 10]
# [11, 32, 9]
# [16, 16, 6]
# [11, 19, 3]
# h -> 11-41

yu = 0.1

for h in range(11,41):
    for i in range(model_img_array.shape[0]):
        for j in range(model_img_array.shape[2]):
            dis = np.sqrt(pow((13 - i), 2) + pow((9 - j), 2))
            if dis <= 2:
                model_img_array[i, h, j] = yu
            elif np.sqrt(pow((11 - i), 2) + pow((14 - j), 2)) <=2:
                model_img_array[i, h, j] = yu
            elif np.sqrt(pow((9 - i), 2) + pow((19 - j), 2)) <=2:
                model_img_array[i, h, j] = yu
            elif np.sqrt(pow((8 - i), 2) + pow((10 - j), 2)) <= 2:
                model_img_array[i, h, j] = yu
            elif np.sqrt(pow((5 - i), 2) + pow((15 - j), 2)) <= 2:
                model_img_array[i, h, j] = yu
            elif np.sqrt(pow((2 - i), 2) + pow((10 - j), 2)) <= 2:
                model_img_array[i, h, j] = yu
            # else:
            #     print(new_img_array[i, h, j])



model_img = sitk.GetImageFromArray(model_img_array)
model_img.SetSpacing(spacing)
sitk.WriteImage(model_img, "../../data/ground_data/model_img.nii")


img_array = sitk.GetArrayFromImage(sitk.ReadImage(
    "../../data/ground_data/0.709_0.5_0.75VVHR_0.236_211_211_111_60itr_1sub.nii"))

model_img_array = sitk.GetArrayFromImage(model_img)
new_img_f = fftn(new_img_array)
model_f = fftn(model_img_array)

H = new_img_f / (model_f + 0.0001)
h = np.fft.ifftn(H)
h = np.real(h)

h = (h -h.min()) / (h.max() - h.min())

h =h /  np.sum(h)
print(np.sum(h))
h_img = sitk.GetImageFromArray(h)
sitk.WriteImage(h_img, "../../data/ground_data/h.nii")
h_pad = np.lib.pad(h, ((0,img_array.shape[0] - h.shape[0]), (0, img_array.shape[1] - h.shape[1]), (0, img_array.shape[2] - h.shape[2])), 'constant', constant_values=(0))
print(h_pad)

H_pad = fftn(h_pad)



img_f = fftn(img_array)

# recon = model_f / (H + 0.0001)
recon = img_f / (H_pad + H.any().min() + 0.0001)

# print(recon)
recon = ifftn(recon)
recon = np.real(recon)


# lucy_richoid
# recon = skimage.restoration.deconvolution.richardson_lucy(img_array, h, iterations=3)


recon_img = sitk.GetImageFromArray(recon)
recon_img.SetSpacing(spacing)
sitk.WriteImage(recon_img, "../../data/ground_data/recon.nii")


