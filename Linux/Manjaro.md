# Manjaro

## 更换镜像源

> vim /etc/pacman.conf

[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

> sudo pacman-mirrors -i -c China -m rank

> sudo pacman -Syy

## Bumblebeed

### 更改boot启动参数

- vim /etc/default/grub

GRUB_CMDLINE_LINUX_DEFAULT="quiet nouveau.modeset=0 acpi_osi=! acpi_osi='Windows 2009'"

acpi_osi=! acpi_osi='Windows 2009' 设置acpi类型为windows 7，bumblebee兼容使用

nouveau.modeset=0 关闭开源nvidia驱动

### 卸载默认安装的free驱动

- mhwd -r pci video-linux(卸载开源驱动)

### 安装bumblebeed

- 依赖
sudo pacman -S virtualgl lib32-virtualgl lib32-primus primus

- 安装双显卡切换程序bumblebee
sudo mhwd -f -i pci video-hybrid-intel-nvidia-bumblebee

- 允许服务
sudo systemctl enable bumblebeed

- 添加用户
sudo gpasswd -a $USER bumblebee

### 测试

- 打开nvida面板
optirun -b none nvidia-settings -c :8

- 不依赖Bumblebee来使用CUDA
sudo tee /proc/acpi/bbswitch <<< 'ON'

- 使用完CUDA 停止NVIDIA显卡
sudo rmmod nvidia_uvm nvidia && sudo tee /proc/acpi/bbswitch <<< OFF

inxi -G # 查看显卡情况
optirun nvidia-smi # 查看CPU情况

## CUDA安装

### 安装CUDA

> sudo pacman -S cuda cudnn

> sudo mkdir /usr/local/cuda

> sudo ln -s /opt/cuda/bin /usr/local/cuda/bin

### 验证安装

完成之后，我们进入cuda的安装路径，我的路径是/opt/cuda，你可以使用下面的命令将CUDA的示例程序拷贝到你的用户主目录下，之后编译程序

cp -r /opt/cuda/samples ~
cd ~/samples
make

此时就使用nvcc编译器开始编译CUDA的sample程序，这个花费时间更长，应该在半小时左右，等待编译结束，使用下面的命令验证是否成功

cd ~/samples/bin/x86_64/linux/release
./deviceQuery
在窗口中查看最后一行的结果是否为pass，如果是则表示CUDA安装成功。

## Steam

### Dota2

启动项添加 vblank_mode=0 primusrun %command%  -perfectworld -safe_mode

vblank_mode=0 primusrun %command% 关闭垂直同步，使用primusrun启动

-safe_mode 使用默认图形依赖(opengl)

## Lutris

> sudo pacman -S wine-staging

> sudo pacman -S lutris

## fcitx-rime

> sudo pacman -S fcitx fcitx-rime fcitx-im fcitx-skin-material kcm-fcitx

> vim .xprofile

export GTK_IM_MODULE=fcitx
export QT_IM_MODELE=fcitx
export XMODIFIERS="@im=fcitx"

> vim .config/fcitx/rime/default.custom.yaml

patch:
  schema_list:
    - schema: luna_pinyin          # 朙月拼音
    - schema: luna_pinyin_simp     # 朙月拼音 简化字模式
    - schema: luna_pinyin_tw       # 朙月拼音 臺灣正體模式
    - schema: double_pinyin_flypy  # 小鶴雙拼
    - schema: emoji                # emoji 表情