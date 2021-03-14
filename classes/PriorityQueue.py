import heapq


# ————————————————
# Copyright statement: This article is the original article of the CSDN blogger "Ha Le Xiao".
# It follows the CC 4.0 BY-SA copyright agreement. Please attach the original source link
# and this statement for reprinting.
# Original link: https://blog.csdn.net/haolexiao/article/details/70302848

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        try:
            return heapq.heappop(self.elements)[1]
        except IndexError:
            return None
