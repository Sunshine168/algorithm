(function() {
	function* flatten2(arr) {
		/* TODO */
		let array = arr || []
		array = String.prototype.split.call(arr, ','),
			array = array.map((value) => parseInt(value))
		for (let o of arr) yield o
	}

	const numbers = flatten2([1, [
		[2], 3, 4
	], 5])

	console.log(numbers.next()) // => 1
	numbers.next().value // => 2
	numbers.next().value // => 3
	numbers.next().value // => 4
	numbers.next().value // => 5
})()