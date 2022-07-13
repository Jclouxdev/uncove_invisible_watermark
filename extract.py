from blind_watermark.blind_watermark import WaterMark

bwm1 = WaterMark(password_img=1, password_wm=1)
# image_input = input('Name.extension of the image you want to extract : ')
# user_input = input('Length of wm_bit : ')
# build_url = '/usr/src/app/examples/output/' + image_input
# print(build_url)
# wm_extract = bwm1.extract(build_url, wm_shape=int(user_input), mode='str')
wm_extract = bwm1.extract('/usr/src/app/examples/output/embedded-color-filter-10.webp', wm_shape=78, mode='str')
print('')
print('WaterMark extracted :', wm_extract)
print('')