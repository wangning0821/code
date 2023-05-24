#所谓“哨兵”就是用一个特殊的值来作为数组的边界key，可以少用一条判断语句，目的在于免去查找过程中每一步都要检测整个表是否
# 查找完毕，以达到提高程序的效率。相对于一层遍历，没有使用”哨兵“的，是有两个判断条件的
# i<array.count和if(array[i] == item)；但是使用了”哨兵“只有一个判断条件if(array[i] == item)！

def searchItemFromArray(array, item):
	if len(array) == 0:
		return -1

	index = len(array) - 1
	firstItem = array[0]

	if firstItem == item:
		# 如果第一个元素等于查找值，直接返回
		return 0

	# 把要查找的值放在数组的第一位上，作为【标兵】
	array[0] = item
	while array[index] != item:
		index -= 1

	# 查找结束，把数组的首位元素改回来
	array[0] = firstItem

	return index if(index > 0) else -1
