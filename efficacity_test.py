import time
from blind_watermark.blind_watermark import WaterMark

startTimer = time.time()
bwm1 = WaterMark(password_img=1, password_wm=1)
bwm1.read_img('/usr/src/app/examples/pic/uncove_pic.webp')
wm = '0123456789'
bwm1.read_wm(wm, mode='str')
bwm1.embed('/usr/src/app/examples/output/embedded.webp')
len_wm = len(bwm1.wm_bit)
endTimer = time.time()
execTime = endTimer - startTimer
print('Executed in ', round(execTime, 2), 's')
print('- - - - - - - - - - - - - - - - - - - - - - -')
print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))
print('- - - - - - - - - - - - - - - - - - - - - - -')

# Check if WM is correctly in
bwm1 = WaterMark(password_img=1, password_wm=1)
wm_extract = bwm1.extract('/usr/src/app/examples/output/embedded.webp', wm_shape=len_wm, mode='str')
print('')
print('WaterMark extracted : ',wm_extract)
print('')