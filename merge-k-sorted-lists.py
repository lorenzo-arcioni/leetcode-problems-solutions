import time
start_time = time.time()

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# Generating a list of listnodes
def generate_listnode():

    H = list()
        
    for lis in range(1000):

        head = l = ListNode()

        for i in range(1000):
            
            l.next = ListNode()
            l.next.val = i
            l = l.next

        H.append(head)

    return H

# Visualizing the listnode
def visualize_listnode(list):

    if list == None:
        print([])
        exit(0)

    l = []

    while list.next != None:
        l.append(list.val)
        list = list.next
    
    print(l)

def mergeKLists1(lists):

        d = dict()

        if len(lists) == 0:
            return None

        start_time = time.time()
        for list in lists:

            if list == None:
                continue

            while list is not None:
                i = list.val
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
                list = list.next
        
        print("First step takes:", round(1000*(time.time() - start_time), 2), "ms")
        
        head = pre = ListNode()

        start_time = time.time()

        d = dict(sorted(d.items(), key=lambda x: x[0]))

        print("Second step takes:", round(1000*(time.time() - start_time), 2), "ms")

        if len(d.keys()) == 0:
            return None

        l = head

        start_time = time.time()

        for k, v in d.items():

            for _ in range(v):
                l.val  = k
                l.next = ListNode()
                pre = l
                l = l.next
        
        pre.next = None

        print("Third step takes:", round(1000*(time.time() - start_time), 2), "ms")

        return head

def mergeKLists2(lists):

        d = []

        if len(lists) == 0:
            return None

        start_time = time.time()
        for list in lists:

            if list == None:
                continue

            while list is not None:
                i = list.val
                d.append(list.val)
                list = list.next
        
        print("First step takes:", round(1000*(time.time() - start_time), 2), "ms")
        
        head = ListNode()

        start_time = time.time()

        d = sorted(d)

        d = iter(d)

        print("Second step takes:", round(1000*(time.time() - start_time), 2), "ms")

        head = pre = ListNode()

        start_time = time.time()

        for list in lists:

            if list == None:
                continue
            
            pre.next = list

            while list is not None:
                pre = list
                list.val = next(d)
                list = list.next
        
        head = head.next

        print("Third step takes:", round(1000*(time.time() - start_time), 2), "ms")

        return head

            

LN = generate_listnode()

start_time = time.time()
mergeKLists1(LN)
print(round(1000*(time.time() - start_time), 2), "ms")

print("----------------------------------------------")

LN = generate_listnode()
start_time = time.time()
mergeKLists2(LN)
print(round(1000*(time.time() - start_time), 2), "ms")
