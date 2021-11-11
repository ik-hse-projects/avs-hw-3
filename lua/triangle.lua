local Color = require "color"
local Point = require "point"

local Triangle = {}
Triangle.__index = Triangle

function Triangle:read(buffer)
	result = setmetatable({}, self)
	result.color = Color:read(buffer)
	result.a = Point:read(buffer)
	result.b = Point:read(buffer)
	result.c = Point:read(buffer)
	setmetatable(result, Triangle)
	return result
end

function Triangle:show()
	return string.format("Triangle: color=%s, points=(%d, %d)-(%d, %d)-(%d, %d)",
	                     self.color, self.a.x, self.a.y,
			                 self.b.x, self.b.y,
			                 self.c.x, self.c.y)
end

function Triangle:perimiter()
	return self.a:distance(self.b) + self.b:distance(self.c) + self.c:distance(self.a)
end

return Triangle
