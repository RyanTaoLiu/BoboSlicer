# BoboSlicer
Bobo slicer, a DLP Slicer for TPMS slicing.
Only need to change the parameters in TPMS-param.xlsx Excel to generate image slicing.

## prepare for env
```
conda create -n boboslicer
conda activate boboslicer
pip install numpy scipy pandas pillow tqdm uuid-utils
```

## code

```
git clone https://github.com/RyanTaoLiu/BoboSlicer.git
cd BoboSlicer
# git switch dev
mkdir out results UVtools
```

Download [UVtools](https://github.com/sn4k3/UVtools/releases) and unzip files into 'UVtools' folder.

Download [template](https://drive.google.com/drive/folders/1vbAZ3YX8BE_tgX597sKFf5MoDsxhImY4?usp=sharing) and copy files to 'template' folder.

## run it 
```
python main_np.py
```
