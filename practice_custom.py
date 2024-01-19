import sys
import random
import json
import pathlib

from PySide2 import QtCore, QtGui, QtWidgets

import importlib

import hou

import custom_ui

importlib.reload(custom_ui)


class Name:
    class Box:
        size = 'name_box_size'

    class Circle:
        rad = 'name_circle_rad'
        roty= 'name_circle_roty'
        div = 'name_circle_div'

    class Height:
        obj = 'name_height_obj'

    class Handle:
        obj = 'name_handle_obj'

"""
class Name을 쓰지 않고
        self.__data = {
            'name_box_size': [3.5, 1.5, 1.],
            'name_circle_rad': [5.25, 5.25],
            'name_circle_roty': 0,
            'name_circle_div': 50,
            'name_height_obj': 20,
            'name_handle_obj': 3
        }
이렇게 직접 문자열을 넣어도 상관이 없다! 그저 가독성을 위함이었을 뿐.
"""

class Entity:
    def __init__(self):
        self.__data = {
            Name.Box.size: [4, 0.3, 1],
            Name.Circle.rad: [5, 5],
            Name.Circle.roty: 10,
            Name.Circle.div: 50,
            Name.Height.obj: 30,
            Name.Handle.obj: 5
        }

    @property
    def data(self) -> dict:
        return self.__data

    @data.setter
    def data(self, data: dict):
        if not isinstance(data, dict):
            return
        self.__data = data

class Custom(QtWidgets.QWidget, custom_ui.Ui_Form__widget):
    def __init__(self, parent = None):
        super(Custom, self).__init__(parent)
        self.__entity = Entity()

        self.setupUi(self)

        self.__json_dir = pathlib.Path(
            '/Users/yeko/Desktop/netflix_TD/ver_04/houdini_api_with_qt/json_dir/')

        self.__node = hou.node('/obj/geo1/__CTRL__')

        self.set_combobox()

        self._signal_func()

        self.set_parm()

        self.pushButton__reset.setIcon(QtGui.QIcon(':/icons/resource/baseline_folder_black_36dp.png'))


      # TODO LIST : set combobox 마저하기!
    #    -> json 파일이 있을 경우 list로 나오고, 클릭했을 때 Load file이 되도록 구현하기!


    @property
    def entity(self):
        return self.__entity

    def save_data(self):
        files = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'Save Files',
            '/Users/yeko/Desktop/netflix_TD/ver_04/houdini_api_with_qt/json_dir/',
            'JSON (*json)'
        )
        fpath = files[0]
        if len(fpath) == 0:
            return None

        fpath = pathlib.Path(fpath)
        self.dump_file(fpath)

    def dump_file(self, fpath: pathlib.Path):
        with open(fpath.as_posix(), 'wt') as fp:
            json.dump(self.get_parm(), fp)

    def get_parm(self):
        data = {
            Name.Box.size: [
                self.doubleSpinBox__boxsize_x.value(),
                self.doubleSpinBox__boxsize_y.value(),
                self.doubleSpinBox__boxsize_z.value(),
            ],
            Name.Circle.rad: [
                self.doubleSpinBox__circle_rad_x.value(),
                self.doubleSpinBox__circle_rad_y.value()
            ],
            Name.Circle.roty: self.horizontalSlider__circle_rot_y.value(),
            Name.Circle.div: self.spinBox__circle_div.value(),
            Name.Height.obj: self.verticalSlider__ysize.value(),
            Name.Handle.obj: self.verticalSlider__handle_height.value()
        }
        return data


    def set_parm(self):

        self.doubleSpinBox__boxsize_x.setValue(self.entity.data.get(Name.Box.size)[0])
        # print(f"{self.entity.data.get(Name.Box.size)[0]}")
        self.doubleSpinBox__boxsize_y.setValue(self.entity.data.get(Name.Box.size)[1])
        self.doubleSpinBox__boxsize_z.setValue(self.entity.data.get(Name.Box.size)[2])

        self.doubleSpinBox__circle_rad_x.setValue(self.entity.data.get(Name.Circle.rad)[0])
        self.doubleSpinBox__circle_rad_y.setValue(self.entity.data.get(Name.Circle.rad)[1])
        self.horizontalSlider__circle_rot_y.setValue(self.entity.data.get(Name.Circle.roty))
        self.spinBox__circle_div.setValue(self.entity.data.get(Name.Circle.div))

        self.verticalSlider__ysize.setValue(self.entity.data.get(Name.Height.obj))
        self.verticalSlider__handle_height.setValue(self.entity.data.get(Name.Handle.obj))


    def _signal_func(self):  # slot과 signal을 연결하기 위해 connect가 꼭 필요!
        self.doubleSpinBox__boxsize_x.valueChanged.connect(self.slot_boxsize_x)
        self.doubleSpinBox__boxsize_y.valueChanged.connect(self.slot_boxsize_y)
        self.doubleSpinBox__boxsize_z.valueChanged.connect(self.slot_boxsize_z)

        self.doubleSpinBox__circle_rad_x.valueChanged.connect(self.slot_cirsize_x)
        self.doubleSpinBox__circle_rad_y.valueChanged.connect(self.slot_cirsize_y)
        self.horizontalSlider__circle_rot_y.valueChanged.connect(self.slot_cir_rotate_y)
        self.spinBox__circle_div.valueChanged.connect(self.slot_cir_div)

        self.verticalSlider__ysize.valueChanged.connect(self.slot_height_obj)
        self.verticalSlider__handle_height.valueChanged.connect(self.slot_handle_obj)

        self.toolButton__save.clicked.connect(self.save_data)

        self.pushButton__reset.clicked.connect(self.set_parm)

        self.comboBox__preset.currentIndexChanged.connect(self.slot_combobox)


        #Todo 콤보 박스의 키값을 눌렀을 때,
        # 그 경로에 있는 파일을 json.load해주는 load.file 함수를 호출하여 set parm을 해주어야 함.

    def set_combobox(self):
        json_files :list = list(self.__json_dir.glob('*.json'))
        get_name = list(map(lambda x: x.name, json_files))
        json_data = dict(zip(get_name, json_files))
        self.comboBox__preset.addItems(list(json_data.keys()))

# TODO GPT helped...me
    def slot_combobox(self):
        selected_name = self.comboBox__preset.currentText()
        if selected_name:
            print(list(self.entity.data))
            selected_data = self.load_file(self.__json_dir/selected_name)
            convert_data = {}
            for key, value in selected_data.items():
                name = key.split('_')
                s_name = name[1]
                last_name = name[2]

                class_key = f"name_{s_name}_{last_name}"
                convert_data[class_key] = value
            # print(selected_data)
            # print(convert_data)
            self.entity.data = convert_data
            print(list(self.entity.data))
            # print(f"{self.entity.data.get(Name.Box.size)[0]}")
            # print(self.entity.data.items())
            self.set_parm()

    @staticmethod
    def load_file(file: pathlib.Path)-> dict:
        try:
            with open (file.as_posix(), 'rt') as fp:
                return json.load(fp)
        except FileNotFoundError as err:
            print(err)
            return {}

    @property
    def ctrl_node(self):
        if(self.__node is None) or (not isinstance(self.__node, hou.SopNode)):
            raise ValueError
        return self.__node

    @ctrl_node.setter
    def ctrl_node(self, val):
        if (val is not None) and isinstance(val, hou.SopNoe):
           self.__node = val
        else:
            raise ValueError



    def slot_boxsize_x(self, val):
        self.ctrl_node.parm('_box_sizex').set(val)

    def slot_boxsize_y(self, val):
        self.ctrl_node.parm('_box_sizey').set(val)

    def slot_boxsize_z(self, val):
        self.ctrl_node.parm('_box_sizez').set(val)

    def slot_cirsize_x(self, val):
        self.ctrl_node.parm('_circle_radiusx').set(val)

    def slot_cirsize_y(self, val):
        self.ctrl_node.parm('_circle_radiusy').set(val)

    def slot_cir_rotate_y(self, val):
        self.ctrl_node.parm('_circle_rotate_y').set(val)

    def slot_cir_div(self, val):
        self.ctrl_node.parm('_circle_div').set(val)

    def slot_height_obj(self, val):
        self.ctrl_node.parm('y_val').set(val)

    def slot_handle_obj(self, val):
        self.ctrl_node.parm('handle_height').set(val)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Custom()
    cus.show()
    sys.exit(app.exec_())