# 一个python小工具合集

## image_cplicer (图片拼接器)

该工具可以把`./data/images/splice/`中的图片按照一定的规则裁剪并拼接为图片，保存为`./data/images/splice/output.jpg`

### use exp

`./data/images/splice/`中存放在视频中截图获取的带有乐谱的图片
设定裁剪规则，使用该工具，即可获取完整的乐谱图片

## video_previewer (视频预览)

该工具接受一个视频输入，设定总共需要预览的帧数，该工具会将视频均等地风格成对应的帧数，并将对应帧显示或保存在`./data/images/video_previewer/`下

### use exp

在previewer.py中设置以下参数
```
preview_frames = 20 # 总共需要预览的帧数
save_frame = True # 是否保存图片，若为False则会显示图片窗口，按"n"下一张，按"q"退出
video_path = "path_to_your_video.mov" # 图片路径
save_dir = "./data/images/video_preview/" # 保存路径
```
运行即可