import os, sys
import shutil
import datetime
import subprocess
import time

def float2strLessthan2dicemic(x:float):
    _str = '{:.2f}'.format(x)
    if _str.endswith('.00'):
        return _str[:-3]
    elif _str.endswith('.0'):
        return _str[:-2]
    elif _str.endswith('.'):
        return _str[:-1]
    elif _str.endswith('0'):
        return _str[:-1]
    else:
        return _str

class gcodeDeal:
    def __init__(self, **kwargs):
        assert 'totalLayer' in kwargs
        self.totalLayer = kwargs['totalLayer']
        self.layerThickness = 0.05 if 'layerThickness' not in kwargs else kwargs['layerThickness']

        self.cycleNumber = 0 if 'cycleNumber' not in kwargs else kwargs['cycleNumber']
        self.raftLayerNumber = 99 if 'raftLayer' not in kwargs else kwargs['raftLayer']

        self.img_name_template = lambda layer: '{}.png'.format(layer)

        with open('template/header.gcode') as f:
            self.start_gcode_template = f.read()

        with open('template/tail.gcode') as f:
            self.tail_gcode_template = f.read()

        with open('template/layerBase.gcode') as f:
            self.base_gcode_template = f.read()

        with open('template/layerPrinting.gcode') as f:
            self.layer_gcode_template = f.read()

        # sth need to calculate
        self.estimateTime = 0

    def gcode_header(self, **kwargs):
        paramaters = {
            'datetime': datetime.datetime.now().isoformat(),
            'totalLayer': kwargs['totalLayer'],
            'estimatedPrintTime': kwargs['totalLayer'] * 20 \
                if 'estimatedPrintTime' not in kwargs else kwargs['estimatedPrintTime'],
            'volume': kwargs['totalLayer'] * 10 if 'volume' not in kwargs else kwargs['volume'],
            'weight': kwargs['totalLayer'] * 10 if 'weight' not in kwargs else kwargs['weight'],
        }
        return self.start_gcode_template.format(**paramaters)

    def gcode_tail(self, **kwargs):
        paramaters = {
            'position_z': float2strLessthan2dicemic(kwargs['position_z']),
            'position_z_p8': float2strLessthan2dicemic(kwargs['position_z'] + 8),
        }
        return self.tail_gcode_template.format(**paramaters)

    def gcode_template_base(self, **kwargs):
        paramaters = {
            'layer_idx': kwargs['layerIdx'],
            'position_z': float2strLessthan2dicemic(kwargs['position_z']),
            'image_file_name': kwargs['image_file_name'],
            'position_z_p2': float2strLessthan2dicemic(kwargs['position_z'] + 2),
            'position_z_p3': float2strLessthan2dicemic(kwargs['position_z'] + 3),
            'position_z_p4': float2strLessthan2dicemic(kwargs['position_z'] + 4),
            'position_z_p5': float2strLessthan2dicemic(kwargs['position_z'] + 5),
            'position_z_p6': float2strLessthan2dicemic(kwargs['position_z'] + 6),
            'position_z_p8': float2strLessthan2dicemic(kwargs['position_z'] + 8),

            'wait_time_after_lift': 1000 if 'wait_time_after_lift' not in kwargs else kwargs['wait_time_after_lift'],
            'wait_time_before_cure': 0 if 'wait_time_before_cure' not in kwargs else kwargs['wait_time_before_cure'],
            'turn_on_led_M106_S': 255 if 'turn_on_led_M106_S' not in kwargs else kwargs['turn_on_led_M106_S'],
            'cure_time_delay': 30000 if 'cure_time_delay' not in kwargs else kwargs['cure_time_delay'],
            'wait_time_after_cure': 1000 if 'wait_time_after_cure' not in kwargs else kwargs['wait_time_after_cure'],
        }
        self.estimateTime += paramaters['wait_time_after_lift']
        self.estimateTime += paramaters['wait_time_before_cure']
        self.estimateTime += paramaters['cure_time_delay']
        self.estimateTime += paramaters['wait_time_after_cure']

        return self.base_gcode_template.format(**paramaters)

    def gcode_template_layer(self, **kwargs):
        '''
        if 'cure_time_delay' in kwargs:
            cure_time_delay = kwargs['cure_time_delay']
        elif kwargs['layerIdx'] == 6:
            cure_time_delay = 25220
        elif kwargs['layerIdx'] == 7:
            cure_time_delay = 20430
        elif kwargs['layerIdx'] == 8:
            cure_time_delay = 15650
        elif kwargs['layerIdx'] == 9:
            cure_time_delay = 10870
        elif kwargs['layerIdx'] == 10:
            cure_time_delay = 6080
        else:
            cure_time_delay = 1300
        '''
        cure_time_delay = 1300
        if 'cure_time_delay' in kwargs:
            cure_time_delay = kwargs['cure_time_delay']

        paramaters = {
            'layer_idx': kwargs['layerIdx'],
            'position_z': float2strLessthan2dicemic(kwargs['position_z']),
            'image_file_name': kwargs['image_file_name'],
            'position_z_p2': float2strLessthan2dicemic(kwargs['position_z'] + 2),
            'position_z_p3': float2strLessthan2dicemic(kwargs['position_z'] + 3),
            'position_z_p4': float2strLessthan2dicemic(kwargs['position_z'] + 4),
            'position_z_p5': float2strLessthan2dicemic(kwargs['position_z'] + 5),
            'position_z_p6': float2strLessthan2dicemic(kwargs['position_z'] + 6),
            'position_z_p8': float2strLessthan2dicemic(kwargs['position_z'] + 8),

            # wait_time_after_lift not use
            'wait_time_after_lift': 1000 if 'wait_time_after_lift' not in kwargs else kwargs['wait_time_after_lift'],
            'wait_time_before_cure': 0 if 'wait_time_before_cure' not in kwargs else kwargs['wait_time_before_cure'],
            'turn_on_led_M106_S': 255 if 'turn_on_led_M106_S' not in kwargs else kwargs['turn_on_led_M106_S'],
            'cure_time_delay': cure_time_delay,

            # wait_time_after_cure not use
            'wait_time_after_cure': 1000 if 'wait_time_after_cure' not in kwargs else kwargs['wait_time_after_cure'],
        }
        self.estimateTime += paramaters['wait_time_before_cure']
        self.estimateTime += paramaters['cure_time_delay']
        return self.layer_gcode_template.format(**paramaters)

    # just to update the printing time
    def pre_save(self):
        self.estimateTime = 0
        for zi in range(6):
            layerIdx = zi + 1
            imgfileName = self.img_name_template(layerIdx)
            _ = self.gcode_template_base(layerIdx=zi,
                                            position_z=layerIdx * self.layerThickness,
                                            image_file_name=imgfileName)
        for zi in range(6, self.totalLayer):
            layerIdx = zi + 1
            imgfileName = self.img_name_template(layerIdx)
            _ = self.gcode_template_layer(layerIdx=zi,
                                          position_z=layerIdx * self.layerThickness,
                                          image_file_name=imgfileName)
    # idx start from 1
    def save_gcode(self, savepath='out/run.gcode'):
        self.pre_save()
        with open(savepath, 'w') as f:
            # header
            _str = self.gcode_header(totalLayer=self.totalLayer, estimatedPrintTime=self.estimateTime//1000)
            f.write(_str)
            f.write('\n')

            # base layers
            for zi in range(6):
                layerIdx = zi + 1
                imgfileName = self.img_name_template(layerIdx)
                _str = self.gcode_template_base(layerIdx=zi,
                                         position_z=layerIdx*self.layerThickness,
                                         image_file_name=imgfileName)
                f.write(_str)
                f.write('\n')

            # printing layers
            for zi in range(6, self.totalLayer):
                layerIdx = zi + 1
                imgfileName = self.img_name_template(layerIdx)
                _str = self.gcode_template_layer(layerIdx=zi,
                                         position_z=layerIdx*self.layerThickness,
                                         image_file_name=imgfileName)
                f.write(_str)
                f.write('\n')
            # tails
            f.write(self.gcode_tail(position_z=layerIdx*self.layerThickness))

def remove_all_temp_files(defalutFolder='out'):
    if os.path.exists(defalutFolder):
        shutil.rmtree(defalutFolder)
    os.mkdir(defalutFolder)


def zipfile(filename: str):
    if filename.endswith('zip'):
        filename = filename.replace('.zip', '')
    shutil.make_archive(filename, 'zip', 'out')

def streamPopen(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(' ')
    while True:
        output = process.stdout.readline()
        if process.poll() is not None and output == '':
            break
        if output:
            print('type convert::' + output.strip())

    stderr_output = process.stderr.read()
    if stderr_output:
        print(stderr_output.strip(), file=sys.stderr)
    else:
        print('convert successfully!')


def postprocess(filename:str, gcode_settings, target_type=''):
    # clean envs
    # remove_all_temp_files()
    shutil.copy('template/preview.png', 'out/preview.png')
    shutil.copy('template/preview_cropping.png', 'out/preview_cropping.png')

    # generate gcode
    print('start generate gcode')
    gd = gcodeDeal(**gcode_settings)
    gd.save_gcode()

    # zip them
    zip_path = './{}.zip'.format(os.path.splitext(filename)[-2])
    zipfile(zip_path)
    # convert them in to need format
    if len(target_type) == 0:
        target_type = os.path.splitext(filename)[-1]

    print('start convert to target type')
    command = './UVtools/UVtoolsCmd.exe convert {} {} {}'.format(zip_path, target_type, filename)
    streamPopen(command)

    # remove temp zip file
    # os.remove('temp.zip')


if __name__ == '__main__':
    # test for zip file
    # zipfile('out.zip')

    # test for removing all files in a folder
    # remove_all_temp_files()

    # test for gcode_generate
    # gd = gcodeDeal(totalLayer=3000)
    #gd.save_gcode('out.gcode')



    # test for all
    gcode_settings = {'totalLayer': 2499}
    postprocess('out.prz', gcode_settings=gcode_settings)
