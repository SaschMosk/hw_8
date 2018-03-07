import subprocess
import os


def make_folder_for_output():
    if not os.path.exists('C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Result'):
        os.mkdir(r'C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Result')


def resize_fotos():
    fotos_list = os.listdir(path='C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Source')
    for foto in fotos_list:
        in_converter = str('C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Source/') + str(foto)
        out_converter = str('C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/Result/') + str(foto)
        arguments = ['C:/Users/sasch/Downloads/Python_course-master/PY1_Lesson_2.5/homework/convert.exe ',
                     in_converter, '-resize', '200', out_converter]
        subprocess.run(arguments)


resize_fotos()
