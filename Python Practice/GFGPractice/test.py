class Solution:
    #Function to merge two sorted linked list.
    def sortedMerge(self,head1, head2):
        # code here
        temp1=head1
        temp2=head2
        h1=head1
        h2=head2
    
        if(head1.data<head2.data):temp=head1
        else: temp=head2
        while temp1.next!=None and temp2.next!=None:
            temp1=h1
            temp2=h2
            if temp1.data<=temp2.data:
                temp1=temp1.next
                h1=h1.next
                last=temp1
                print(last.data)
                if temp1.next.data<temp2.data:
                    pass
                else:
                    h1=h1.next
                    temp1.next=temp2
                    last=temp2
                    
                
            elif temp2.data<temp1.data:
               temp2=temp2.next
               h2=h2.next
               last=temp2
               print("heyyy i am here")
               if temp2.next.data<temp1.data:
                    pass
                    
               else:
                   
                   h2=h2.next
                   temp2.next=temp1
                   last=temp1
                    
        
                
        return temp   
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = list(map(int, input().split()))
        input2 = list(map(int, input().split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends