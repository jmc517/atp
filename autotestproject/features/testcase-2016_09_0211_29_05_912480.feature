# language: zh-CN
功能: 暂停音乐并验证播放状态暂停
场景: 暂停音乐并验证播放状态暂停
当< 打开音乐应用
当< 打开我的音乐库
当< 播放本地指定音乐
|music_name|
|小城故事|
当< 播放或暂停音乐
那么< 验证音乐是否播放
|is_playing|
|false|