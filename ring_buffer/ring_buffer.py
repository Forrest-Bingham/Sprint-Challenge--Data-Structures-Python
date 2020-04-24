from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #FIFO, 

        #Adding to the Ring Buffer. 
        #If nothing in storage, add to head.
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        # if storage is at max and current is not at head, remove from head
        elif self.storage.length == self.capacity and self.current is not self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

        #If storage is at max and current is at head, remove from tail
        elif self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        #else: puts it in the middle
        else:
            self.storage.add_to_tail(item)
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        #Loop through the array 
        while len(list_buffer_contents) < self.storage.length:
            #Add the current value
            list_buffer_contents.append(self.current.value)

            #If there is a next, set next node to current
            if self.current.next:
                self.current = self.current.next
            #End of list
            else:
                self.current = self.storage.head
            

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
