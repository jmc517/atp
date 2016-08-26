# -*- coding: UTF-8 -*-
import random
import time
from behave import when, then

from actions.video import Video
from support.global_vars import d
from utils.utils import Utils


@when(u'< 打开我的视频')
def step_impl(context):
    Video().click_video_mine_ele()
@when(u'< 播放本地视频')
def step_impl(context):
    # 获取视频名称
    video_name = context.table[0]['video_name']
    Video().click_video_mine_local_video_ele()
    Video().click_video_mine_local_video_by_name(video_name)

@then(u'< 验证视频是否播放')
def step_impl(context):
    #获取参数
    chk_is_playing = context.table[0]['chk_is_playing']
    is_playing = Video().get_video_is_playing()
    if not str(chk_is_playing).lower().__eq__(str(is_playing).lower()):
        Utils().raise_Exception_info('视频播放状态不一致，期望值《'+ chk_is_playing +'》，实际值《'+ is_playing + '》')

@then(u'< 验证视频播放名称一致')
def step_impl(context):
    # 获取参数
    param = context.table[0]['chk_name']
    if param.startswith('o_'):
        chk_video_name = Utils().get_context_map(param)
    else:
        chk_video_name = param

    video_name = Video().get_video_playing_name_txt()
    if not chk_video_name.__eq__(video_name):
        Utils().raise_Exception_info('视频文件名称不一致，期望值为《' + chk_video_name + '》，实际值为《' + video_name + '》')

@when(u'< 打开视频搜索')
def step_impl(context):
    Video().click_video_search_ele()
@when(u'< 输入视频搜索关键字')
def step_impl(context):
    # 获取入参
    key_word = context.table[0]['keyword']
    Video().input_video_search_keyword_ele(key_word)
@when(u'< 从搜索结果中播放指定视频')
def step_impl(context):
    # 获取入参
    video_name = context.table[0]['video_name']
    print(video_name)
    list_view = Video().get_video_search_list_ele()
    title_ele = Video().get_video_search_list_title()


    if title_ele.wait.exists(timeout = Utils().LONG_TIME_OUT):
        if list_view.scroll.vert.to(text = video_name):
            for t in title_ele:
                if t.text.strip().__eq__(video_name):
                    t.click.wait()
                    break
        else:
            Utils().raise_Exception_info('搜索视频不存在')
    else:
        Utils().raise_Exception_info('视频搜索结果为空')
@when(u'< 清空视频搜索框并验证')
def step_impl(context):
    Video().click_video_search_clear_ele()
    if not (d(text = '热门搜索').wait.exists() and d(text = '搜索记录').wait.exists()):
        Utils().raise_Exception_info('清空搜索框返回界面不正确')

@when(u'< 从播放记录中播放指定视频')
def step_impl(context):
    #获取播放视频名称
    video_name = context.table[0]['video_name']
    # 点击播放记录控件进入播放记录界面
    Video().click_video_mine_play_his_ele()
    # 从列表中查找指定视频并播放
    ele = Video().get_video_mine_play_his_list_ele()
    if ele.wait.exists():
        if ele.scroll.vert.to(text = video_name):
            d(text = video_name).click.wait()
        else:
            Utils().raise_Exception_info('没有查找到指定《'+ video_name + '》视频')
    else:
        Utils().raise_Exception_info('播放记录为空')
@when(u'< 搜索热门搜索视频')
def step_impl(context):
    #获取接受返回值参数
    param = context.table[0]['o_result']
    video_name = Video().click_video_search_hot_ele()
    Utils().set_context_map(param, video_name)


@when(u'< 搜索搜索记录视频')
def step_impl(context):
    #获取接受返回值的参数
    param = context.table[0]['o_result']
    video_name = Video().click_video_search_his_ele()
    Utils().set_context_map(param, video_name)
@when(u'< 打开我的发现')
def step_impl(context):
    Video().click_video_find_ele()
@when(u'< 随机播放发现视频')
def step_impl(context):
    #获取接受输入的参数
    param = context.table[0]['o_result']
    # 获取我的发现视频栏目并随机点击
    ele = Video().get_video_find_channel_ele()
    if ele.wait.exists():
        size = len(ele)
        idx = random.randint(0, size - 1)
        ele[idx].click.wait()
        ele_item = Video().get_video_find_channel_item_ele()
        if ele_item.wait.exists(timeout = Utils().LONG_TIME_OUT):
            size_item = len(ele_item)
            idx_item = random.randint(0, size_item - 1)
            #获取要播放视频的文本信息并存入上下文
            e = ele_item[idx_item]
            ret = e.text.strip()
            Utils().set_context_map(param, ret)
            e.click.wait()
        else:
            Utils().raise_Exception_info('栏目列表不存在，可能是网络原因')
    else:
        Utils().raise_Exception_info('我的发现视频栏目不存在')

@when(u'< 打开爱奇艺')
def step_impl(context):
    ele = Video().get_video_aiqiyi_ele()
    if ele.wait.exists():
        ele.click.wait()
    else:
        Utils().raise_Exception_info('爱奇艺视频控件不存在')
@when(u'< 随机播放爱奇艺视频')
def step_impl(context):
    # 获取接受出参的参数
    param = context.table[0]['o_result']

    ele = Video().get_video_aiqiyi_recommend_ele()
    if ele.wait.exists():
        size = len(ele)
        idx = random.randint(0, size - 1)
        ret = ele[idx].text.strip()
        Utils().set_context_map(param, ret)
        ele[idx].click.wait()
    else:
        Utils().raise_Exception_info('爱奇艺推荐视频不存在')
@when(u'< 获取爱奇艺观看记录')
def step_impl(context):
    # 获取参数
    param = context.table[0]['o_result']

    ele = Video().get_video_aiqiyi_his_ele()
    if ele.wait.exists():
        Utils().set_context_map(param, ele.text.strip())
    else:
        Utils().raise_Exception_info('爱奇艺观看记录控件不存在')

@when(u'< 获取我的视频播放记录')
def step_impl(context):
    # 获取参数
    param = context.table[0]['o_result']

    Video().click_video_mine_play_his_ele()
    ele = Video().get_video_search_list_title()
    if ele.wait.exists():
        Utils().set_context_map(param, ele[0].text.strip())
    else:
        Utils().raise_Exception_info('我的视频播放记录不存在')
@then(u'< 验证视频搜索结果')
def step_impl(context):
    flag = False
    # 获取参数
    param = context.table[0]['search_word']
    ele = Video().get_video_search_list_title()
    for e in ele:
        if param in e.text.strip():
            flag = True
            break

    if not flag:
        Utils().raise_Exception_info('搜索视频没有期望的结果')









