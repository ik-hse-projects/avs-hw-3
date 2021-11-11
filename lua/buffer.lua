local buffer = {}

function buffer.Stream(file)
	local result = {
		file = file
	}
	function result:read_int(_min, _max)
		return self.file:read("*n")
	end
	return result
end

function buffer.Randomized()
	local result = {}
	function result:read_int(min, max)
		if min == nil then
			min = 0
		end
		if max == nil then
			max = 2147483647
		end
		return math.random(min, max)
	end
	return result
end

return buffer
