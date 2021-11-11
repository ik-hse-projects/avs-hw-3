local Color = require "color"
local Point = require "point"

local Rectangle = {}
Rectangle.__index = Rectangle

function Rectangle:read(buffer)
	result = setmetatable({}, self)
	result.color = Color:read(buffer)
	result.left_top = Point:read(buffer)
	result.right_bottom = Point:read(buffer)
	return result
end

function Rectangle:show()
	return string.format("Rectangle: color=%s, top-left=(%d, %d), bottom-right=(%d, %d)",
	                     self.color,
			     self.left_top.x, self.left_top.y,
			     self.right_bottom.x, self.right_bottom.y)
end

function Rectangle:perimiter()
	height = self.right_bottom.y - self.left_top.y
        width = self.right_bottom.x - self.left_top.x
	return 2*(height + width)
end

return Rectangle
