import pygame
import random
import threading
class SortableArray:
    def __init__(self, arrlen = 256):
        self.arrLen = arrlen
        self.arr = [i for i in range(self.arrLen)]
        self.arrayAccesses = 0
        self.comparisons = 0
        self.swaps = 0
        self.time = 0
        self.isSorting = False
        self.isSorted = False
        self.shouldSleep = True
        self.sort_thread = threading.Thread()
        self.simulation_speed = 3
        self.selectedIndices = []
        self.scramble()

    def draw(self):

        s_width,s_height = pygame.display.get_window_size()
        rect_width = s_width // self.arrLen
        rect_height = (s_height-50) / self.arrLen
        for i,v in enumerate(self.arr):
            color = (255,255,255)
            if i in self.selectedIndices:
                color = (255,0,0)
            if self.isSorted:
                color = (0,255,0)
            pygame.draw.rect(pygame.display.get_surface(),
                             color,
                             (i*rect_width,
                             s_height - int(rect_height*v),
                             rect_width,
                             int(rect_height*v)))
    def reset(self):
        self.arrayAccesses = 0
        self.comparisons = 0
        self.swaps = 0
        self.time = 0

    def scramble(self):
        self.isSorted = False
        random.shuffle(self.arr)

    def swapElement(self,idx1,idx2):
        self.swaps += 1
        self.arrayAccesses += 4
        temp = self.arr[idx1]
        self.arr[idx1] = self.arr[idx2]
        self.arr[idx2] = temp

    def sim_sleep(self):
        if self.isSorting and self.shouldSleep:
             pygame.time.wait(self.simulation_speed)

    def stop_sim(self):
        self.isSorting = False
        # self.sort_thread.join()

    def sim_sort(self):
        self.reset()
        self.isSorting = True
        self.sort_thread = threading.Thread(target=self.sort_func)
        self.sort_thread.start()

    def compare_idx(self, idx1,idx2):
        self.selectedIndices.clear()
        self.selectedIndices.append(idx1)
        self.selectedIndices.append(idx2)
        self.comparisons += 1
        self.arrayAccesses += 2
        return self.arr[idx1] > self.arr[idx2]

    def sort_func(self):
        raise NotImplementedError("Please implement a sorting function")
