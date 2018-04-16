import subprocess
import os

data_path = f'{os.getcwd()}\PY1_Lesson_2.5\homework\\'
Result_folder_path = data_path + 'Result'
Source_folder_path = data_path + 'Source'
Converter_path = data_path + 'convert.exe'


def make_folder_for_output():
    if not os.path.exists(Result_folder_path):
        os.mkdir(Result_folder_path)


def resize_fotos():
    fotos_list = os.listdir(path=Source_folder_path)
    for foto in fotos_list:
        in_converter = str(Source_folder_path + '\\') + str(foto)
        out_converter = str(Result_folder_path + '\\') + str(foto)
        arguments = [Converter_path,
                     in_converter, '-resize', '200', out_converter]
        subprocess.run(arguments)


resize_fotos()
