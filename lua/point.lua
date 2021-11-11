local Point = {}
Point.__index = Point

function Point:read(buffer)
	local result = setmetatable({}, self)
	result.x = buffer:read_int()
	result.y = buffer:read_int()
	return result
end
function Point:distance(other)
	dx = other.x - self.x
	dy = other.y - self.y
	return math.sqrt(dx*dx + dy*dy)
end

return Point
