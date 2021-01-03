from aip import AipFace
import base64

APP_ID = "23478974"
APP_KEY = "6jzxysoEGlVRDRlcE2n31Ey5"
SECRET_KEY = "LZrDGYYG4qIB6T3Rb1NLOZ4bfxabMkt5"

aipFace = AipFace(APP_ID, APP_KEY, SECRET_KEY)

filePath = r'hg.jpg'


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')


imageType = "BASE64"

options = {}
options['face_field'] = "age,gender,beauty"

result = aipFace.detect(get_file_content(filePath), imageType, options)
print(result)
age = result['result']['face_list'][0]['age']
print("年龄预测为：{}".format(age))
gender = result['result']['face_list'][0]['gender']['type']
print("性别预测为：{}".format(gender))
beauty = result['result']['face_list'][0]['beauty']
print("性别预测为：{}".format(beauty))



