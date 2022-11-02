def length(head): 
    el = head
    count=0
    while (el):
        count += 1
        el = el.next
    return count