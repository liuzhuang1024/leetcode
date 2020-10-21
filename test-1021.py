# test-1021.py
# 问题一：mAP的计算方法
# gt: x
# pre: y
# 预测正确的数量：t， （阈值大于0.8）

# p = t / x
# recall = t / y
# f = 2pr/(p+r)
# ap = f
# mAP = (ap0+ap1+ ...+)/n

# 问题二：nms计算流程
# def nms(pre_bbox):
#     # pre_bbox shpae [n, box, 置信度]
#     # 设置置信度阈值 0.8
#     # 第一步：过滤置信度低于0.8的bbox
#     # 第二步根据置信度进行排序。
#     # 第三步：剔除top1，设置iou阈值0.8，保留小于阈值的bbox，剔除大于的bbox。
#     # 第四步：循环第三步。
#     return

# 问题三：快排算法的实现
def sort_(arr: list, left: int, right: int) -> list:
    """
    快排算法书写错误。基础不扎实。
    """
    min_ = left
    max_ = right
    p = arr[left]
    while left == right:
        while arr[right] >= p:
            right -= 1
        while arr[left] < p:
            left += 1
        arr[right], arr[left] = arr[left], arr[right]
    sort_(arr[min_:left-1], min_, left-1-min_)
    sort_(arr[left+1:max_], left+1, max_-left-1)
    return arr
# 问题四
# resnet解决了什么问题。

# 今天比较惨啊，面的很难受，知识点薄弱。自己表达能力欠佳。加油吧！实习生！

if __name__ == "__main__":

    arr = [1, 2, 4, 6]
    res = sort_(arr, left=0, right=len(arr))
    print(res)
