import subprocess
import os

if not os.path.exists('C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Converted_fotos'):
    os.mkdir(r'C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Converted_fotos')

# for file in 'C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Source':
process = subprocess.call('C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/convert.exe '
                          'C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Source/trump_mug.jpg '
                          '-resize 200 C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Converted_fotos')




# args = ['convert', fname, '-compress', 'none',
#             os.path.splitext(os.path.basename(fname))[0]+'.png']
#     prog_status = subprocess.call(args)
#     return "{0} processed. Exited with status code {1}".format(
#         fname, prog_status)

# convert input.jpg -resize 200 output.jpg