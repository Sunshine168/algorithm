let test1 = {
  val: 1,
  next: {
    val: 2,
    next: {
      val: 3,
      next: {
        val: 4,
        next: {
          val: 5,
          next: null
        }
      }
    }
  }
};

var swapNodes = function(head, k) {
  let leftCursor,
    rightCursor,
    cursor = head,
    count = 1,
    queue = [];
  while (cursor) {
    queue.unshift(cursor);
    let length = queue.length;
    if (length === k) {
      leftCursor = queue[length - 1];
    }
    cursor = cursor.next;
  }
  rightCursor = queue[k];
  // 真实需要交换的节点
  let r = rightCursor.next,
    l = leftCursor.next,
    temp = r.next;
  r.next = l.next;
  leftCursor.next = r;
  rightCursor.next = l;
  l.next = temp;
  return head;
};


console.log(JSON.stringify(swapNodes(test1,2)))