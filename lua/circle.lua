Color = require "color"
Point = require "point"

local Circle = {}
Circle.__index = Circle

function Circle:read(buffer)
	local result = setmetatable({}, self)
	result.color = Color:read(buffer)
	result.center = Point:read(buffer)
	result.radius = buffer:read_int()
	return result
end

function Circle:show()
	return string.format("Circle: color=%s, center=(%d, %d), radius=%d",
	                     self.color, self.center.x, self.center.y, self.radius)
end

function Circle:perimiter()
	return 2 * math.pi * self.radius
end

return Circle
