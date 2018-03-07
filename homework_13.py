import subprocess
import os

if not os.path.exists('C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Result'):
    os.mkdir(r'C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Result')

# for file in 'C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Source':
process = subprocess.call('C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/convert.exe '
                          'C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Source/trump_mug.jpg '
                          '-resize 200 C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Result/trump_mug.jpg')