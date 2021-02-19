from utils import common
from abc import ABC, abstractmethod


class CBehavior(ABC):
    @abstractmethod
    def find(self, all_sheep, target, herd_point):
        pass

    @abstractmethod
    def check(self, all_sheep, target, fn, theta):
        pass


class OldCBehavior(CBehavior):

    def find(self, all_sheep, target, herd_point):
        return common.find_farthest_sheep(all_sheep)

    def check(self, all_sheep, target, fn, theta):
        return common.check(all_sheep, fn)


class NewCBehavior(CBehavior):
    def find(self, all_sheep, target, herd_point):
        return common.find_max_double_dist_sheep(target, all_sheep)

    def check(self, all_sheep, target, fn, theta):
        return common.check_dist(all_sheep, target, fn) and common.check_sector(all_sheep, theta, target)


class MaxAngleCBehavior(CBehavior):
    """这里是非方向性最大角策略"""
    def find(self, all_sheep, target, herd_point):
        return common.find_max_angle_sheep(herd_point, all_sheep)

    def check(self, all_sheep, target, fn, theta):
        return common.check(all_sheep, fn)