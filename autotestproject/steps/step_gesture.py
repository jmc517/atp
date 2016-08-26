# -*- coding: UTF-8 -*-
from behave import when

from actions.gesture import Gesture


@when(u'< 开始倒车')
def step_impl(context):
    Gesture().start_back_car()
@when(u'< 结束倒车')
def step_impl(context):
    Gesture().stop_back_car()
